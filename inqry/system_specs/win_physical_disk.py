import re
import subprocess

BASE_COMMAND = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Get-PhysicalDisk'


def get_physical_disk_identifiers(unique_id_output=None):
    unique_id_output = unique_id_output or list_all_ids()
    physical_disk_id_pattern = re.compile(r'(?!UniqueId)(\b.+\b|{\b.+\b}|\b.+:.+\b)')
    return re.findall(physical_disk_id_pattern, unique_id_output)


def get_physical_disk_friendly_names(friendly_name_output=None):
    friendly_name_output = friendly_name_output or list_all_friendly_names()
    friendly_name_pattern = re.compile(r'(?!FriendlyName)(\b.+\b)')
    return re.findall(friendly_name_pattern, friendly_name_output)


def get_disk_info(unique_id):
    return _get_output_of_get_physical_disk_command(arguments='-UniqueID \'{}\' | Select *'.format(unique_id))


def get_disk_info_from_friendly_name(friendly_name):
    return _get_output_of_get_physical_disk_command(arguments='-FriendlyName \'{}\' | Select *'.format(friendly_name))


def list_all_ids():
    return _get_output_of_get_physical_disk_command(arguments='"| Select UniqueId"')


def list_all_friendly_names():
    return _get_output_of_get_physical_disk_command(arguments='"| Select FriendlyName"')


def _get_output_of_get_physical_disk_command(arguments=None):
    arguments = arguments or ''
    full_command = ' '.join([BASE_COMMAND, arguments])
    return subprocess.check_output(full_command).decode('utf-8')
