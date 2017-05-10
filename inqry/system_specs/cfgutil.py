import json
import shlex
import subprocess

from inqry.system_specs import _human_readable

BASE_COMMAND = '/usr/local/bin/cfgutil --foreach --format JSON get color IMEI serialNumber deviceType totalDiskCapacity'


def parse_cfgutil_output(output):
    return json.loads(output)


def get_all_device_ecids(cfgutil_output):
    return parse_cfgutil_output(cfgutil_output)['Devices']


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')


def get_hardware_overview_for_all_devices(cfgutil_output):
    return [parse_cfgutil_output(cfgutil_output)['Output'][ecid] for ecid in get_all_device_ecids(cfgutil_output)]


class DeviceSpecs:
    def __init__(self, device_hardware_overview):
        self.serial_number = device_hardware_overview['serialNumber']
        self.model_identifier = device_hardware_overview['deviceType']
        self.storage = _human_readable(device_hardware_overview['totalDiskCapacity'])
        self.color = device_hardware_overview['color']

        try:
            self.imei = device_hardware_overview['IMEI']
        except KeyError:
            self.imei = None


def create_from_device_hardware_overview(cfgutil_output):
    return [DeviceSpecs(device_hardware_overview) for device_hardware_overview in
            get_hardware_overview_for_all_devices(cfgutil_output)]
