import os
import wmi


class WindowsProfile:
    windows_system_profiler = {}

    def __init__(self):
        c = wmi.WMI()
        self.win32_bios = c.Win32_BIOS()[0]
        self.win32_processor = c.Win32_Processor()[0]
        self.win32_disk_drive = c.Win32_DiskDrive()[0]
        self.win32_logical_disk = c.Win32_LogicalDisk()[0]
        self.win32_computer_system = c.Win32_ComputerSystem()[0]
        self.win32_physical_memory = c.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        self.windows_system_profiler['Model Name'] = self.name
        self.windows_system_profiler['Manufacturer'] = self.manufacturer
        self.windows_system_profiler['Serial Number (system'] = self.serial
        self.windows_system_profiler['Model Identifier'] = self.model
        self.windows_system_profiler['Number of Processors'] = self.cpu_processors
        self.windows_system_profiler['Total Number of Cores'] = self.cpu_cores
        self.windows_system_profiler['Processor Speed'] = self.cpu_name
        self.windows_system_profiler['Memory'] = self.memory
        return self.windows_system_profiler

    @property
    def manufacturer(self):
        return self.win32_computer_system.Manufacturer

    @property
    def name(self):
        return self.win32_computer_system.SystemSKUNumber

    @property
    def model(self):
        return self.win32_computer_system.Model

    @property
    def serial(self):
        return self.win32_bios.SerialNumber

    @property
    def cpu_name(self):
        return self.win32_processor.Name

    @property
    def cpu_cores(self):
        return self.win32_processor.NumberOfCores

    @property
    def cpu_processors(self):
        return self.win32_computer_system.NumberOfProcessors

    @property
    def memory(self):
        return self._human_readable(self.win32_computer_system.TotalPhysicalMemory)

    @property
    def storage_model(self):
        return self.win32_disk_drive.Model

    @property
    def storage_size(self):
        return self._human_readable(self.win32_disk_drive.Size)

    @property
    def user(self):
        full_username = self.win32_computer_system.UserName
        return full_username.split('\\')[1]

    @staticmethod
    def _human_readable(component):
        return str(round(int(component) / 10 ** 9)) + " GB"
