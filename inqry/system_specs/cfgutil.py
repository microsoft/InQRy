from enum import Enum
import json
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil --foreach --format JSON get totalDiskCapacity color IMEI serialNumber deviceType'


class DeviceSpecs:
    def __init__(self, device_hardware_overview):
        self.serial_number = device_hardware_overview['serialNumber']
        self.device_type = device_hardware_overview['deviceType']
        self.imei = device_hardware_overview['IMEI']
        self.storage = device_hardware_overview['totalDiskCapacity']


def get_device_ecids(cfgutil_output):
    return parse_command_output(cfgutil_output)['Devices']


def parse_command_output(output):
    return json.loads(output)


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
