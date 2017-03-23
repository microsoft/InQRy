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

    def __init__(self, attributes):
        self.os_type = platform.system()
        self.attributes = attributes

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
        storage = {}
        internal_disks = system_profiler.get_internal_storage()
        internal_disk_count = 0
        for internal_disk in internal_disks:
            internal_disk_count += 1
            storage[
                f'Drive {internal_disk_count}'] = f'{internal_disk.size} {internal_disk.type} ({internal_disk.device_name})'
        return storage

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


def create_specs_from_system_profiler_hardware_output(output):
    """This method is used primarily for testing."""
    return SystemSpecs(output)


def main():
    return SystemSpecs(system_profiler.collector())


if __name__ == '__main__':
    main()
