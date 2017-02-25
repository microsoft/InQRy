import platform
import yaml
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


def get_mac_hardware():
    return create_specs_from_system_profiler_hardware_output(
        system_profiler.hardware())


def mac_storage():
    """
    This function is used as the primary means of obtaining a Mac's
    physical storage information.
    """
    return macdisk.get_all_physical_disks()


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

    @property
    def storage(self):
        disk_list = mac_storage()
        internal_disks = []
        for disk in disk_list:
            if disk.is_internal == True:
                internal_disks.append(disk)
        assert isinstance(internal_disks, list)
        return internal_disks

    def operating_system(self):
        pass

    @property
    def serial(self):
        # assert isinstance(serial, str)
        return self.attributes.get('Serial Number (system)')

    @property
    def cpu_name(self):
        name = self.attributes.get('Processor Name')
        assert isinstance(name, str)
        return name

    @property
    def cpu_processors(self):
        processors = self.attributes.get('Number of Processors')
        assert isinstance(processors, int)
        return processors

    @property
    def cpu_cores(self):
        cores = self.attributes.get('Total Number of Cores')
        assert isinstance(cores, int)
        return cores

    @property
    def cpu_speed(self):
        speed = self.attributes.get('Processor Speed')
        assert isinstance(speed, str)
        return speed

    @property
    def memory(self):
        memory = self.attributes.get('Memory')
        return memory

    @property
    def model(self):
        model = self.attributes.get('Model Identifier')
        return model

    @property
    def name(self):
        name = self.attributes.get('Model Name')
        return name
