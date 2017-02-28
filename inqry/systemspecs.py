import platform
from inqry import system_profiler
from inqry import macdisk


# import sys
# if sys.platform == 'win32':
#   import win32_sysinfo as sysinfo
# elif sys.platform == 'darwin':
#   import mac_sysinfo as sysinfo
# elif 'linux' in sys.platform:
#   import linux_sysinfo as sysinfo
#  etc

def create_specs_from_system_profiler_hardware_output(output):
    return SystemSpecs(output)


def mac_os():
    """
    This function is used as the primary means of obtaining basic Mac
    hardware components.
    """
    return create_specs_from_system_profiler_hardware_output(
        system_profiler.hardware())


def _get_mac_internal_storage():
    disk_list = macdisk.get_all_physical_disks()
    internal_disks = [disk for disk in disk_list if disk.is_internal]
    return internal_disks

def windows():
    """
    This function is used as the primary means of obtaining basic Windows
    machine hardware components.
    """
    pass


class SystemSpecs(object):
    """Represents the machine's system specifications before it's data is used
    to form an asset object.

    A SystemSpecs object should be able to be used to access several system
    profile specs, even if they are not used by the Asset class.

    A SystemSpecs object should also be able to be used the same way,
    regardless of which operating system the specs were generated from"""

    def __init__(self, attributes):
        """TODO"""
        self.os_type = platform.system()
        self.attributes = attributes

    def list_all(self):
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
        name = self.attributes.get('Model Name')
        return name

    @property
    def model(self):
        model = self.attributes.get('Model Identifier')
        return model

    @property
    def serial(self):
        return self.attributes.get('Serial Number (system)')

    @property
    def cpu_name(self):
        hw = self.attributes
        return hw.get('Processor Name')

    @property
    def cpu_processors(self):
        processors = self.attributes.get('Number of Processors')
        return processors

    @property
    def cpu_cores(self):
        cores = self.attributes.get('Total Number of Cores')
        return cores

    @property
    def cpu_speed(self):
        speed = self.attributes.get('Processor Speed')
        return speed

    @property
    def memory(self):
        memory = self.attributes.get('Memory')
        return memory

    @property
    def drive_count(self):
        if self.os_type == 'Darwin':
            return len(_get_mac_internal_storage())
        else:
            pass

    @property
    def storage(self):
        storage = {}
        if self.os_type == 'Darwin':
            internal_disk_list = _get_mac_internal_storage()
            internal_disk_count = 0
            for internal_disk in internal_disk_list:
                internal_disk_count += 1
                storage['Drive {}'.format(internal_disk_count)] = internal_disk
                return storage
        else:
            pass

    @property
    def drive1_model(self):
        try:
            return self.storage['Drive 1'].device_name
        except KeyError:
            return None

    @property
    def drive2_model(self):
        try:
            return self.storage['Drive 2'].device_name
        except KeyError:
            return None

    @property
    def drive3_model(self):
        try:
            return self.storage['Drive 3'].device_name
        except KeyError:
            return None

    @property
    def drive4_model(self):
        try:
            return self.storage['Drive 4'].device_name
        except KeyError:
            return None

    @property
    def drive5_model(self):
        try:
            return self.storage['Drive 5'].device_name
        except KeyError:
            return None
