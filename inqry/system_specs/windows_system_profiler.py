import re
import wmi


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
                'Memory': self.get_memory_in_gigabytes(self.win32_computer_system.TotalPhysicalMemory),
                'Processor Name': self.get_cpu_name(self.win32_processor.Name),
                'Processor Speed': self.get_cpu_speed(self.win32_processor.Name)}

    @staticmethod
    def _human_readable(component):
        return str(round(int(component) / 1024 ** 3)) + " GB"

    @staticmethod
    def _split_processor(name):
        pattern = re.compile(r' @ ')
        return re.split(pattern, name)

    @staticmethod
    def get_cpu_name(full_cpu_name):
        return WindowsProfile._split_processor(full_cpu_name)[0]

    @staticmethod
    def get_cpu_speed(full_cpu_name):
        return WindowsProfile._split_processor(full_cpu_name)[1]

    @staticmethod
    def get_memory_in_gigabytes(memory_bytes):
        return WindowsProfile._human_readable(memory_bytes)


def get_hardware_overview():
    """
    Returns all components from a WindowsProfile instance a dictionary with the same keys as a Mac system profile
    :return: dict:
    """
    return WindowsProfile().get_all_windows_system_components()
