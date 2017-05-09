import re
import subprocess

BASE_COMMAND = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Get-PhysicalDisk'


def get_physical_disk_identifiers(unique_id_output=None):
    unique_id_output = unique_id_output or list_all()
    physical_disk_id_pattern = re.compile(r'(?!UniqueId)(\b.+\b|{.*})(?=-*)')
    return re.findall(physical_disk_id_pattern, unique_id_output)


def get_disk_info(unique_id):
    return _get_output_of_get_physical_disk_command(arguments='-UniqueID \'{}\' | Select *'.format(unique_id))


def list_all():
    return _get_output_of_get_physical_disk_command(arguments='"| Select UniqueId"')


def _get_output_of_get_physical_disk_command(arguments=None):
    arguments = arguments or ''
    full_command = ' '.join([BASE_COMMAND, arguments])
    return subprocess.check_output(full_command).decode('utf-8')
