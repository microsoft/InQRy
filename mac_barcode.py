import re
import barcode
from sh import system_profiler

hardware_data = str(system_profiler("SPHardwareDataType"))

def get_component_list():
    serial = re.findall(r"Serial\sNumber\s\(system\):\s([A-Z0-9]{12})", hardware_data)
    serial = serial[0]
    return serial

def generate_barcode():
    component = get_component_list()
    final = barcode.generate('code39', component[0], output='%s' % component)
    return final

generate_barcode()
