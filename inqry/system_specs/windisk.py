import re
from inqry.system_specs import get_physicaldisk


def create_disk_from_get_physical_disk_output(get_physical_disk_output):
    return Disk(get_physical_disk_output)


def get_all_physical_disk():
    return [create_disk_from_get_physical_disk_output(get_physicaldisk.get_disk_info(unique_disk_id)) for
            unique_disk_id in get_physicaldisk.get_physical_disk_identifiers()]


def get_internal_storage():
    internal_disks = get_all_physical_disk()
    return [disk for disk in internal_disks if disk.is_internal]


class Disk(object):
    def __init__(self, windows_disk):
        self.windows_disk = windows_disk

    @property
    def bustype(self):
        pattern = re.compile(r'(?:BusType\s+:\s)([A-Z]+)')
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
        valid_bus_types = ['SATA', 'RAID']
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
        return human_readable(re.findall(pattern, self.windows_disk)[0])


def human_readable(component):
    return str(round(int(component) / 10 ** 9)) + " GB"
