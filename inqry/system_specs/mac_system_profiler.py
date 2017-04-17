from enum import Enum
import re
import subprocess
import yaml
from inqry.system_specs import macdisk

BASE_COMMAND = '/usr/sbin/system_profiler'


class DataTypes(Enum):
    def __str__(self):
        return 'SP' + self.value + 'DataType'

    DEVELOPER_TOOLS = 'DeveloperTools'
    DIAGNOSTICS = 'Diagnostics'
    DISPLAYS = 'Displays'
    HARDWARE = 'Hardware'
    MEMORY = 'Memory'
    # SERIAL_ATA = 'SerialATA'
    SOFTWARE = 'Software'
    STORAGE = 'Storage'
    THUNDERBOLT = 'Thunderbolt'


def get_data(data_type):
    """
    Returns system_profiler data on macOS as a dictionary

    `data_type` must be one of `DataTypes`, i.e.

        get_data(DataTypes.HARDWARE)

    :param data_type:
    :type data_type: DataTypes
    :return dict:
    """
    return parse_command_output(_get_command_output(str(data_type)))


def parse_command_output(output):
    return yaml.load(_yamlize_output(output))


def _get_command_output(*arguments):
    return subprocess.check_output([BASE_COMMAND] + list(arguments)).decode('utf-8')


def _yamlize_output(output):
    return '\n'.join([_yamlize_line(line) for line in output.split('\n')])


def _yamlize_line(line):
    line = _remove_dash_after_first_colon(line)

    eight_spaces = '        '
    line = line[2:] if line.startswith(eight_spaces) else line

    return line


def _remove_dash_after_first_colon(line):
    return re.sub(pattern=r'(.+: )-', repl=r'\1', string=line)


def collector():
    return get_data(DataTypes.HARDWARE)['Hardware']['Hardware Overview']


def get_internal_storage():
    internal_disks = macdisk.get_all_physical_disks()
    return [disk for disk in internal_disks if disk.is_internal]


def internal_storage_from_system_profiler():
    storage_data = get_data(DataTypes.STORAGE)['Storage']

    for drive in storage_data.keys():
        for prop in storage_data[drive].keys():
            if prop == 'Physical Drive' or 'Physical Volumes':
                print(storage_data[drive].keys(), storage_data[drive][prop])
