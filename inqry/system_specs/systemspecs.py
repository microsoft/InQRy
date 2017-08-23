import json
import platform

from inqry.system_specs import diskutility
from inqry.system_specs import system_profiler


class SystemSpecs(object):
    """Represents the machine's system specifications. A SystemSpec instance
     has several machine components that are accessible via simple property
     methods.

    A SystemSpecs object should also be able to be used the same way,
    regardless of which operating system the specs were generated from.

    A SystemSpecs instance is platform agnostic, but does contain the os_type
    attribute"""

    def __init__(self, hardware_overview=None, internal_storage=None, os_type=None):
        self.os_type = os_type or platform.system()
        self.hardware_overview = hardware_overview or system_profiler.get_hardware_overview()
        self.internal_storage = internal_storage or diskutility.get_internal_storage()

    def summary(self):
        return {'os_type': self.os_type, 'hardware': self.hardware_overview, 'storage': self.storage}

    def to_json(self):
        return json.dumps(self.summary())

    @property
    def model_name(self):
        return self.hardware_overview.get('Model Name')

    @property
    def model_identifier(self):
        return self.hardware_overview.get('Model Identifier')

    @property
    def serial_number(self):
        return self.hardware_overview.get('Serial Number (system)')

    @property
    def processor_name(self):
        return self.hardware_overview.get('Processor Name')

    @property
    def processor_speed(self):
        return self.hardware_overview.get('Processor Speed')

    @property
    def memory(self):
        return self.hardware_overview.get('Memory')

    @property
    def drive_count(self):
        return len(self.storage)

    @property
    def imei(self):
        return self.hardware_overview.get('IMEI')

    def mobile_storage(self):
        return self.hardware_overview.get('Storage')

    @property
    def storage(self):
        return {'Drive {}'.format(disk_count): '{} {} ({})'.format(disk.size, disk.type, disk.device_name) for
                disk_count, disk in enumerate(self.internal_storage, 1)}

    @property
    def drive1(self):
        return self.storage.get('Drive 1')

    @property
    def drive2(self):
        return self.storage.get('Drive 2')

    @property
    def drive3(self):
        return self.storage.get('Drive 3')

    @property
    def drive4(self):
        return self.storage.get('Drive 4')
