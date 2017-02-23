import re
import yaml
from inqry import diskutil


def get_all_physical_disks():
    return [diskutil.get_disk_info(disk_identifier)
            for disk_identifier in diskutil.get_physical_disk_identifiers()]


def disk_factory(diskutil_info_output_list):
        return [Disk(yaml.load(output)) for output in diskutil_info_output_list]


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
