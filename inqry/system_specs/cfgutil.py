from enum import Enum
import json
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil --foreach --format JSON get totalDiskCapacity color IMEI serialNumber deviceType'


class PropertyNames(Enum):
    def __str__(self):
        return self.value

    COLOR = 'color'
    DEVICE_TYPE = 'deviceType'
    IMEI = 'IMEI'
    SERIAL_NUMBER = 'serialNumber'
    STORAGE = 'totalDiskCapacity'


def parse_command_output(output):
    return json.loads(output)


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
