import subprocess
from xml.etree.ElementTree import parse


def xml_data(hardware_property):
    subprocess.call(
        ["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
         "Get-CimInstance", hardware_property, "|",
         "ConvertTo-XML", "-As", "String"])


processor = xml_data("Win32_Processor")
print(processor)
