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

    def __init__(self, attributes=None):
        self.os_type = platform.system()
        self.attributes = attributes or system_profiler.collector()

    @property
    def name(self):
        return self.attributes.get('Model Name')

    @property
    def model(self):
        return self.attributes.get('Model Identifier')

    @property
    def serial(self):
        return self.attributes.get('Serial Number (system)')

    @property
    def cpu_name(self):
        return self.attributes.get('Processor Name')

    @property
    def cpu_processors(self):
        return self.attributes.get('Number of Processors')

    @property
    def cpu_cores(self):
        return self.attributes.get('Total Number of Cores')

    @property
    def cpu_speed(self):
        return self.attributes.get('Processor Speed')

    @property
    def memory(self):
        return self.attributes.get('Memory')

    @property
    def drive_count(self):
        return len(system_profiler.get_internal_storage())

    @property
    def storage(self):
        return {f'Drive {disk_count}': f'{disk.size} {disk.type} ({disk.device_name})' for disk_count, disk in
                self._get_internal_storage()}

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

    @staticmethod
    def _get_internal_storage(internal_storage=None):
        return internal_storage or enumerate(system_profiler.get_internal_storage())
