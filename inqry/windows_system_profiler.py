import os
import wmi

c = wmi.WMI()

SYSINFO = c.Win32_ComputerSystem()[0]
OSINFO = c.Win32_OperatingSystem()[0]
CPUINFO = c.Win32_Processor()[0]
HDDINFO = c.Win32_LogicalDisk()[0]
RAMINFO = c.Win32_PhysicalMemory()[0]


RAMTOTAL = int(SYSINFO.TotalPhysicalMemory)
HDDTOTAL = int(HDDINFO.size)
RAMSIZE = round(RAMTOTAL)
HDDSIZE = round(HDDTOTAL)

os.system('cls')
# print("Model: " + MANUFACTURER + " " + MODEL)
# print("\r")
# print("HDD: " + str(HDDTOTAL) + "GB")
# print("RAM: " + str(RAMTOTAL) + "GB")
# print("CPU: " + CPUINFO.name)
# print("OS: " + OSINFO.caption)


print()


def serial():
    serial = c.Win32_BIOS()[0].SerialNumber
    return print(serial)


def manufacturer():
    sysinfo = c.Win32_ComputerSystem()[0].Manufacturer
    return sysinfo.Manufacturer


def model():
    sysinfo = c.Win32_ComputerSystem()[0].Model
    return sysinfo.Model
