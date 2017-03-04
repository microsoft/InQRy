import wmi


class WindowsProfile:
    """A WindowsProfile instance uses the third-party module "wmi". When instantiated, the instance gets all needed
    attribute data structures from the appropriate WMI classes."""

    def __init__(self):
        c = wmi.WMI()
        self.win32_bios = c.Win32_BIOS()[0]
        self.win32_processor = c.Win32_Processor()[0]
        self.win32_disk_drive = c.Win32_DiskDrive()[0]
        self.win32_computer_system = c.Win32_ComputerSystem()[0]
        self.win32_physical_memory = c.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        wmi_data = {'Model Name': self.win32_computer_system.Model,
                    'Manufacturer': self.win32_computer_system.Manufacturer,
                    'Serial Number (system)': self.win32_bios.SerialNumber,
                    'Model Identifier': self.win32_computer_system.SystemSKUNumber,
                    'Number of Processors': self.win32_computer_system.NumberOfProcessors,
                    'Total Number of Cores': self.win32_processor.NumberOfCores,
                    'Memory': self.human_readable(self.win32_computer_system.TotalPhysicalMemory),
                    'Processor Name': self.win32_processor.Name}
        return wmi_data

    @property
    def storage_model(self):
        return self.win32_disk_drive.Model

    @property
    def storage_size(self):
        return self.human_readable(self.win32_disk_drive.Size)

    @property
    def user(self):
        return self.split_name(self.win32_computer_system.UserName)

    @staticmethod
    def human_readable(component):
        return str(round(int(component) / 10 ** 9)) + " GB"

    @staticmethod
    def split_name(name):
        return name.split('\\')[1]


def collector():
    """Returns all components from a WindowsProfile instance a dictionary with the same keys as a Mac system profile"""
    return WindowsProfile().get_all_windows_system_components()
