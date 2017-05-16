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
        self.win32_computer_system_product = c.Win32_ComputerSystemProduct()[0]
        self.win32_physical_memory = c.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        return {'Model Name': self._get_model_name(),
                'Model Identifier': self._get_model_identifier(),
                'Manufacturer': self.win32_computer_system.Manufacturer,
                'Serial Number (system)': self._get_serial_number(),
                'Number of Processors': self.win32_computer_system.NumberOfProcessors,
                'Total Number of Cores': self.win32_processor.NumberOfCores,
                'Memory': self.get_memory_in_gigabytes(self.win32_computer_system.TotalPhysicalMemory),
                'Processor Name': self.get_processor_name(self.win32_processor.Name),
                'Processor Speed': self.get_processor_speed(self.win32_processor.Name)}

    @staticmethod
    def _human_readable(component):
        return str(round(int(component) / 1024 ** 3)) + ' GB'

    @staticmethod
    def _split_processor(name):
        pattern = re.compile(r' @ ')
        return re.split(pattern, name)

    def _get_model_name(self):
        return self.win32_computer_system_product.Name or self.win32_computer_system.Model

    def _get_model_identifier(self):
        try:
            return self.win32_computer_system.SystemSKUNumber or self.win32_computer_system_product.Version
        except AttributeError:
            return self._get_model_name()

    def _get_serial_number(self):
        return self.win32_bios.SerialNumber or self.win32_computer_system_product.IdentifyingNumber

    @staticmethod
    def _remove_extra_processor_data(processor):
        pattern = re.compile(r'\(\w\)')
        return re.sub(pattern, '', processor)

    @staticmethod
    def get_processor_name(full_cpu_name):
        return WindowsProfile._remove_extra_processor_data(WindowsProfile._split_processor(full_cpu_name)[0])

    @staticmethod
    def get_processor_speed(full_processor_name):
        return WindowsProfile._split_processor(full_processor_name)[1]

    @staticmethod
    def get_memory_in_gigabytes(memory_bytes):
        return WindowsProfile._human_readable(memory_bytes)


def get_hardware_overview():
    """
    Returns all components from a WindowsProfile instance a dictionary with the same keys as a Mac system profile
    :return: dict:
    """
    return WindowsProfile().get_all_windows_system_components()
