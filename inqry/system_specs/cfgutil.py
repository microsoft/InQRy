import json
import shlex
import subprocess

BASE_COMMAND = '/usr/local/bin/cfgutil --foreach --format JSON get IMEI serialNumber deviceType totalDiskCapacity'


def parse_cfgutil_output(output):
    return json.loads(output)


def get_all_device_ecids(cfgutil_output=None):
    cfgutil_output = cfgutil_output or _get_output_of_cfgutil_command()
    return parse_cfgutil_output(cfgutil_output)['Devices']


def get_hardware_overview_for_all_devices(cfgutil_output):
    return [parse_cfgutil_output(cfgutil_output)['Output'][ecid] for ecid in
            get_all_device_ecids(cfgutil_output)]


def _get_output_of_cfgutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
