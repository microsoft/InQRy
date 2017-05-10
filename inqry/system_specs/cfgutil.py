from enum import Enum
import re
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil'


class Properties(Enum):
    def __str__(self):
        return self.value

    DEVICE_TYPE = 'deviceType'
    STORAGE = 'totalDiskCapacity'
    COLOR = 'color'
    IMEI = 'IMEI'
    SERIAL_NUMBER = 'serialNumber'


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
