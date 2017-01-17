import subprocess
from xml.etree.ElementTree import parse

processor = subprocess.call(
    ["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
     "Get-CimInstance", "Win32_Processor"])

print(processor)
