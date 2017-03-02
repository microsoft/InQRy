import re
import yaml
from inqry.system_specs import diskutil


def create_from_diskutil_info_output(output):
    return Disk(yaml.load(output))


def get_all_physical_disks():
    return [
        create_from_diskutil_info_output(
            diskutil.get_disk_info(disk_identifier))
        for disk_identifier in diskutil.get_physical_disk_identifiers()
        ]


class Disk:
    def __init__(self, attributes=None):
        self.attributes = attributes or {}

    @property
    def device_location(self):
        return self.attributes.get('Device Location')

    @property
    def is_internal(self):
        return self.device_location == 'Internal'

    @property
    def is_external(self):
        return self.device_location == 'External'

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
        return self.attributes.get('Disk Size') or self.attributes.get(
            'Total Size')

    @property
    def size(self):
        disk_size_pattern = re.compile(r'(?P<disk_size>\d+\.?\d* [MGT]?B) .*$')
        disk_size_match = re.match(disk_size_pattern, self.verbose_disk_size)

        if disk_size_match:
            return disk_size_match.group('disk_size')
