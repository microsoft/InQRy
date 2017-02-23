import re
import shlex
import subprocess

BASE_COMMAND = '/usr/sbin/diskutil'


def get_physical_disk_identifiers(diskutil_list_output=None):
    diskutil_list_output = diskutil_list_output or list_all()
    physical_disk_id_pattern = re.compile(r'(/dev/disk\d+) \(\w+, physical\).*')

    return re.findall(physical_disk_id_pattern, diskutil_list_output)


def get_disk_info(disk_identifier):
    return _get_output_of_diskutil_command(arguments=f'info {disk_identifier}')


def list_all():
    return _get_output_of_diskutil_command(arguments='list')


def _get_output_of_diskutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))

    return subprocess.check_output(full_command).decode('utf-8')
