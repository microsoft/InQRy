import wmi


class WindowsProfile:
    wmi_data = {}

    def __init__(self):
        c = wmi.WMI()
        self.win32_bios = c.Win32_BIOS()[0]
        self.win32_processor = c.Win32_Processor()[0]
        self.win32_disk_drive = c.Win32_DiskDrive()[0]
        self.win32_computer_system = c.Win32_ComputerSystem()[0]
        self.win32_physical_memory = c.Win32_PhysicalMemory()[0]

    def get_all_windows_system_components(self):
        self.wmi_data['Model Name'] = self.name
        self.wmi_data['Manufacturer'] = self.manufacturer
        self.wmi_data['Serial Number (system)'] = self.serial
        self.wmi_data['Model Identifier'] = self.model
        self.wmi_data['Number of Processors'] = self.cpu_processors
        self.wmi_data['Total Number of Cores'] = self.cpu_cores
        self.wmi_data['Processor Speed'] = self.cpu_name
        self.wmi_data['Memory'] = self.memory
        self.wmi_data['Processor Name'] = self.cpu_name
        return self.wmi_data

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
        return self.human_readable(self.win32_computer_system.TotalPhysicalMemory)

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


def hardware():
    win = WindowsProfile()
    return win.get_all_windows_system_components()
