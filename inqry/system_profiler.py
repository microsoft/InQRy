import shlex
import subprocess
import yaml

BASE_COMMAND = '/usr/sbin/system_profiler'


def _get_output_of_system_profiler_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')


def _hardware_parser(system_profiler_output):
    return yaml.load(system_profiler_output)['Hardware']['Hardware Overview']


def hardware():
    hardware_specs_dict = _get_output_of_system_profiler_command(arguments='SPHardwareDataType')
    return hardware_specs_dict
