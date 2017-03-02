import os
from wmi import WMI


class WindowsProfile(WMI):
    windows_system_profiler = {}

    def __init__(self):
        self.bios = self.Win32_BIOS()[0]
        self.processor = self.Win32_Processor()[0]
        self.disk_drive = self.Win32_DiskDrive()[0]
        self.logical_disk = self.Win32_LogicalDisk()[0]
        self.computer_system = self.Win32_ComputerSystem()[0]
        self.physical_memory = self.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        self.windows_system_profiler['Model'] = self.model()

    def manufacturer(self):
        return self.computer_system.Manufacturer

    def name(self):
        return self.computer_system.SystemSKUNumber

    def model(self):
        return self.computer_system.Model

    def serial(self):
        return self.bios.SerialNumber

    def cpu_name(self):
        return self.processor.Name

    def cpu_cores(self):
        return self.processor.NumberOfCores

    def memory(self):
        return self.human_readable(self.computer_system.TotalPhysicalMemory)

    def human_readable(self, component):
        return str(round(int(component) / 10 ** 9)) + " GB"

    def storage_model(self):
        return self.disk_drive.Model

    def storage_size(self):
        return self.human_readable(self.disk_drive.Size)

    def user(self):
        full_username = self.computer_system.UserName
        return full_username.split('\\')[1]
