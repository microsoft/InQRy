import platform
from inqry.system_specs import system_profiler


class SystemSpecs(object):
    """Represents the machine's system specifications. A SystemSpec instance
     has several machine components that are accessible via simple property
     methods.

    A SystemSpecs object should also be able to be used the same way,
    regardless of which operating system the specs were generated from.

    A SystemSpecs instance is platform agnostic, but does contain the os_type
    attribute"""

    def __init__(self, hardware_overview=None, internal_storage=None):
        self.os_type = platform.system()
        self.internal_storage = internal_storage or system_profiler.get_internal_storage()
        self.hardware_overview = hardware_overview or system_profiler.get_hardware_overview()

    @property
    def name(self):
        return self.hardware_overview.get('Model Name')

    @property
    def model(self):
        return self.hardware_overview.get('Model Identifier')

    @property
    def serial(self):
        return self.hardware_overview.get('Serial Number (system)')

    @property
    def cpu_name(self):
        return self.hardware_overview.get('Processor Name')

    @property
    def cpu_processors(self):
        return self.hardware_overview.get('Number of Processors')

    @property
    def cpu_cores(self):
        return self.hardware_overview.get('Total Number of Cores')

    @property
    def cpu_speed(self):
        return self.hardware_overview.get('Processor Speed')

    @property
    def memory(self):
        return self.hardware_overview.get('Memory')

    @property
    def drive_count(self):
        return len(self.storage)

    @property
    def storage(self):
        return {f'Drive {disk_count}': f'{disk.size} {disk.type} ({disk.device_name})' for disk_count, disk in
                enumerate(self.internal_storage, 1)}

    @property
    def drive1(self):
        try:
            return self.storage['Drive 1']
        except KeyError:
            return str("")

    @property
    def drive2(self):
        try:
            return self.storage['Drive 2']
        except KeyError:
            return str("")

    @property
    def drive3(self):
        try:
            return self.storage['Drive 3']
        except KeyError:
            return str("")

    @property
    def drive4(self):
        try:
            return self.storage['Drive 4']
        except KeyError:
            return str("")
