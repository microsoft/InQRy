import shlex
import subprocess
import yaml

BASE_COMMAND = '/usr/sbin/system_profiler'


def hardware():
    hardware_specs_dict = _hardware_parser(
        _get_system_profiler_output(arguments='SPHardwareDataType'))
    return hardware_specs_dict


def _get_system_profiler_output(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')


def _hardware_parser(system_profiler_output):
    hardware_dict = yaml.load(system_profiler_output)
    try:
        return hardware_dict['Hardware']['Hardware Overview']
    except:
        raise KeyError("Keys 'Hardware' and 'Hardware Overview' do not exist")
