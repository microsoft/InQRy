from enum import Enum
import re
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil'


class PropertyNames(Enum):
    def __str__(self):
        return self.value

    COLOR = 'color'
    DEVICE_TYPE = 'deviceType'
    IMEI = 'IMEI'
    SERIAL_NUMBER = 'serialNumber'
    STORAGE = 'totalDiskCapacity'


def parse_command_output(output):
    pass


def _get_command_output(*arguments):
    return subprocess.check_output([BASE_COMMAND] + list(arguments)).decode('utf-8')


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')


class DeviceSpecs:
    def __init__(self):
        pass
