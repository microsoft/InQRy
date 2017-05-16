import re
import yaml
from inqry.system_specs import diskutil


def create_from_diskutil_output(output):
    return Disk(yaml.load(output))


def create_disks_from_physical_disk_ids():
    return [create_from_diskutil_output(diskutil.get_disk_info(disk_id)) for disk_id in diskutil.get_all_physical_ids()]


def get_internal_storage():
    internal_disks = create_disks_from_physical_disk_ids()
    return [disk for disk in internal_disks if disk.is_internal and not disk.is_virtual()]


class Disk:
    def __init__(self, attributes=None):
        self.attributes = attributes or {}

    @property
    def device_location(self):
        return self.attributes.get('Device Location')

    @property
    def removable_media(self):
        return self.attributes.get('Removable Media')

    @property
    def is_fixed(self):
        return self.removable_media == 'Fixed' or not self.removable_media

    @property
    def is_internal(self):
        return self.device_location != 'External'

    def is_virtual(self):
        return self.attributes.get('Virtual')

    @property
    def is_external(self):
        return self.device_location == 'External' or self.is_fixed is False

    @property
    def type(self):
        if self.is_ssd:
            return 'SSD'
        elif not self.is_ssd:
            return 'HDD'
        else:
            return 'Unknown'

    @property
    def device_name(self):
        return self.attributes.get('Device / Media Name')

    @property
    def is_ssd(self):
        return self.attributes.get('Solid State')

    @property
    def verbose_disk_size(self):
        return self.attributes.get('Disk Size') or self.attributes.get('Total Size')

    @property
    def size(self):
        disk_size_pattern = re.compile(r'(?P<disk_size>\d+\.?\d* [MGT]?B) .*$')
        disk_size_match = re.match(disk_size_pattern, self.verbose_disk_size)
        if disk_size_match:
            return disk_size_match.group('disk_size')
