import json
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil --foreach --format JSON get IMEI serialNumber deviceType totalDiskCapacity'


def parse_cfgutil_output(output):
    return json.loads(output)


def get_device_properties_from_cfgutil_output(cfgutil_output=None):
    cfgutil_output = cfgutil_output or _get_output_of_cfgutil_command()
    return parse_cfgutil_output(cfgutil_output)


def get_hardware_properties_for_attached_devices(device_properties=None):
    device_properties = device_properties or get_device_properties_from_cfgutil_output()
    return [device_properties['Output'][ecid] for ecid in device_properties['Devices']]


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
