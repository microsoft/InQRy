import os
import wmi

c = wmi.WMI()

bios_output = c.Win32_BIOS()[0]
processor_output = c.Win32_Processor()[0]
disk_drive_output = c.Win32_DiskDrive()[0]
logical_disk_output = c.Win32_LogicalDisk()[0]
computer_system_output = c.Win32_ComputerSystem()[0]
physical_memory_output = c.Win32_PhysicalMemory()[0]


def manufacturer():
    pass


def name():
    pass


def model():
    pass


def serial():
    pass


def cpu():
    pass


def memory():
    pass


def storage():
    pass
