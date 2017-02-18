import subprocess
from xml.etree.ElementTree import parse

powershell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"


def xml_data(hardware_property):
    output = subprocess.call(
        ["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
         "Get-CimInstance", hardware_property, "|",
         "ConvertTo-XML", "-As", "String"])
    print(output)
    return output


def get_ciminstance(class_name, class_object):
    item = subprocess.check_output(
        [powershell, "Get-CimInstance", class_name, "|",
         "Select-Object", class_object])
    return item


def assign_variable(var, cim_args):
    subprocess.check_output(
        ["$" + var, "=", "Get-CimInstance", cim_args])
    return


variables = ["system", "bios", "os", "cpu", "hdd"]
class_objects = ["CIM_ComputerSystem", "CIM_BIOSElement",
                 "CIM_OperatingSystem", "CIM_Processor", "CIM_LogicalDisk"]


def all_variables():
    for variable, class_object in variables, class_objects:
        assign_variable(variable, class_object)


all_variables()
