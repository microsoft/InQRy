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


def get_ciminstance(args, component):
    item = subprocess.check_output(
        [powershell, "Get-CimInstance", args, "|", "Select-Object", component])
    return item


print(get_ciminstance("CIM_ComputerSystem", "Name"))
print(get_ciminstance("CIM_BIOSElement", "SerialNumber"))
