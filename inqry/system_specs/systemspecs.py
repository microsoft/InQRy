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

    def list_all(self):
        """Returns all the components of a SystemSpec instance as a list. This
        method can be iterated through and added to a QR code"""
        return [self.name,
                self.model,
                self.serial,
                self.cpu_name,
                self.cpu_speed,
                self.cpu_processors,
                self.cpu_cores,
                self.memory,
                self.drive_count,
                self.drive1_model,
                self.drive2_model,
                self.drive3_model,
                self.drive4_model,
                self.drive5_model]

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
        if self.os_type == 'Darwin':
            return len(system_profiler.get_mac_internal_storage())
        else:
            pass

    @property
    def storage(self):
        storage = {}
        if self.os_type == 'Darwin':
            internal_disk_list = system_profiler.get_mac_internal_storage()
            internal_disk_count = 0
            for internal_disk in internal_disk_list:
                internal_disk_count += 1
                storage['Drive {}'.format(internal_disk_count)] = internal_disk
                return storage
        else:
            return str("")

    @property
    def drive1_model(self):
        try:
            return self.storage['Drive 1'].device_name
        except KeyError:
            return str("")

    @property
    def drive2_model(self):
        try:
            return self.storage['Drive 2'].device_name
        except KeyError:
            return str("")

    @property
    def drive3_model(self):
        try:
            return self.storage['Drive 3'].device_name
        except KeyError:
            return str("")

    @property
    def drive4_model(self):
        try:
            return self.storage['Drive 4'].device_name
        except KeyError:
            return str("")

    @property
    def drive5_model(self):
        try:
            return self.storage['Drive 5'].device_name
        except KeyError:
            return str("")


def create_specs_from_system_profiler_hardware_output(output):
    """This method is used primary for testing."""
    return SystemSpecs(output)


def main():
    return SystemSpecs(system_profiler.hardware())


if __name__ == '__main__':
    main()
