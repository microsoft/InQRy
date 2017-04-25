from enum import Enum
import re
import subprocess
import yaml

BASE_COMMAND = '/usr/sbin/system_profiler'


class DataTypes(Enum):
    def __str__(self):
        return 'SP' + self.value + 'DataType'

    DEVELOPER_TOOLS = 'DeveloperTools'
    DIAGNOSTICS = 'Diagnostics'
    DISPLAYS = 'Displays'
    HARDWARE = 'Hardware'
    MEMORY = 'Memory'
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


def get_hardware_overview():
    return get_data(DataTypes.HARDWARE)['Hardware']['Hardware Overview']
