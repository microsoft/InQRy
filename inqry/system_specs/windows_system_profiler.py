import wmi
from inqry.system_specs import windisk


class WindowsProfile:
    """A WindowsProfile instance uses the third-party module "wmi". When instantiated, the instance gets all needed
    attribute data structures from the appropriate WMI classes."""

    def __init__(self):
        c = wmi.WMI()
        self.win32_bios = c.Win32_BIOS()[0]
        self.win32_processor = c.Win32_Processor()[0]
        self.win32_disk_drive = c.Win32_DiskDrive()
        self.win32_computer_system = c.Win32_ComputerSystem()[0]
        self.win32_physical_memory = c.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        return {'Model Name': self.win32_computer_system.Model,
                'Model Number': self.win32_computer_system.SystemSKUNumber,
                'Manufacturer': self.win32_computer_system.Manufacturer,
                'Serial Number (system)': self.win32_bios.SerialNumber,
                'Model Identifier': self.win32_computer_system.SystemSKUNumber,
                'Number of Processors': self.win32_computer_system.NumberOfProcessors,
                'Total Number of Cores': self.win32_processor.NumberOfCores,
                'Memory': human_readable(self.win32_computer_system.TotalPhysicalMemory),
                'Processor Name': self.win32_processor.Name}

    @property
    def user(self):
        return split_name(self.win32_computer_system.UserName)

    @staticmethod
    def size(disk):
        return human_readable(disk)


def collector():
    """Returns all components from a WindowsProfile instance a dictionary with the same keys as a Mac system profile"""
    return WindowsProfile().get_all_windows_system_components()


def get_internal_storage():
    internal_disks = windisk.get_all_physical_disk()
    return [disk for disk in internal_disks if disk.is_internal]


def human_readable(component):
    return str(round(int(component) / 10 ** 9)) + " GB"


def split_name(name):
    return name.split('\\')[1]
