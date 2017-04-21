import re
import shlex
import subprocess

BASE_COMMAND = '/usr/sbin/diskutil'


def get_external_physical_disk_ids(diskutil_list_output=None):
    diskutil_list_output = diskutil_list_output or list_all()
    pattern = re.compile(r'(/dev/disk\d+) \(external(?:, physical|)\).*')
    return re.findall(pattern, diskutil_list_output)


def get_internal_physical_disk_ids(diskutil_list_output=None):
    diskutil_list_output = diskutil_list_output or list_all()
    pattern = re.compile(r'(/dev/disk\d+) \(internal(?:, physical|)\).*')
    return re.findall(pattern, diskutil_list_output)


def get_all_physical_ids(diskutil_list_output=None):
    diskutil_list_output = diskutil_list_output or list_all()
    return get_internal_physical_disk_ids(diskutil_list_output) + get_external_physical_disk_ids(diskutil_list_output)


def get_disk_info(disk_id):
    return _get_output_of_diskutil_command(arguments='info {}'.format(disk_id))


def list_all():
    return _get_output_of_diskutil_command(arguments='list')


def _get_output_of_diskutil_command(arguments=None):
    arguments = arguments or ''
    full_command = shlex.split(' '.join([BASE_COMMAND, arguments]))
    return subprocess.check_output(full_command).decode('utf-8')
