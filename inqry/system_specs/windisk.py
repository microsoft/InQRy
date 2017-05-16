import re
from inqry.system_specs import win_physical_disk


def get_all_physical_disks_from_friendly_names():
    friendly_names = win_physical_disk.get_physical_disk_friendly_names()
    return [Disk(win_physical_disk.get_disk_info_from_friendly_name(friendly_name))
            for friendly_name in friendly_names]


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
        valid_bus_types = ['SATA', 'RAID', 'NVMe', 'ATA']
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
