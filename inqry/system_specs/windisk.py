import re
from inqry.system_specs import win_physical_disk
import subprocess


def create_disk_from_win_physical_disk_output(win_physical_disk_output):
    return Disk(win_physical_disk_output)


def get_all_physical_disks_from_friendly_names():
    return [create_disk_from_win_physical_disk_output(win_physical_disk.get_physical_disk_friendly_names(friendlyname))
            for friendlyname in win_physical_disk.get_physical_disk_friendly_names()]


def get_internal_storage():
    internal_disks = get_all_physical_disks_from_friendly_names()
    return [disk for disk in internal_disks if disk.is_internal]


class Disk(object):
    def __init__(self, windows_disk):
        self.windows_disk = windows_disk

    @property
    def bustype(self):
        pattern = re.compile(r'(?:BusType\s+:\s)([a-zA-Z]+)')
        return re.findall(pattern, self.windows_disk)[0]

    @property
    def device_location(self):
        return 'Internal' if self.is_internal else 'External'

    @property
    def device_name(self):
        pattern = re.compile(r'(?:FriendlyName\s+:\s)([\w\d\-._ ]+)')
        return re.findall(pattern, self.windows_disk)[0]

    @property
    def is_internal(self):
        valid_bus_types = ['SATA', 'RAID', 'NVMe']
        return self.bustype in valid_bus_types

    @property
    def is_external(self):
        return self.is_internal is False

    @property
    def type(self):
        pattern = re.compile(r'(?:MediaType\s+:\s)([A-Z]+)')
        return re.findall(pattern, self.windows_disk)[0]

    @property
    def is_ssd(self):
        return self.type == 'SSD'

    @property
    def size(self):
        pattern = re.compile(r'(?:Size\s+:\s)([\d]+)')
        return self._human_readable(re.findall(pattern, self.windows_disk)[0])

    @staticmethod
    def _human_readable(component):
        size = round(int(component) / 10 ** 9)
        if size >= 1000:
            return str(size / 1000) + " TB"
        else:
            return str(size) + " GB"
