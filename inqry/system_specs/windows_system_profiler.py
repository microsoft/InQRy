import os
import wmi

c = wmi.WMI()

bios = c.Win32_BIOS()[0]
processor = c.Win32_Processor()[0]
disk_drive = c.Win32_DiskDrive()[0]
logical_disk = c.Win32_LogicalDisk()[0]
computer_system = c.Win32_ComputerSystem()[0]
physical_memory = c.Win32_PhysicalMemory()[0]


def manufacturer():
    return computer_system.Manufacturer


def name():
    return computer_system.SystemSKUNumber


def model():
    return computer_system.Model


def serial():
    return bios.SerialNumber


def cpu_name():
    return processor.Name


def cpu_cores():
    return processor.NumberOfCores


def memory():
    return human_readable(computer_system.TotalPhysicalMemory)


def human_readable(component):
    return str(round(int(component) / 10 ** 9)) + " GB"


def storage_model():
    return disk_drive.Model


def storage_size():
    return human_readable(disk_drive.Size)


def user():
    full_username = computer_system.UserName
    return full_username.split('\\')[1]
