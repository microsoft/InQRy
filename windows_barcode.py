import subprocess
from xml.etree.ElementTree import parse

subprocess.call(['Get-CimInstance', 'Win32_Processor', '|' 'ConvertTo-XML'])
