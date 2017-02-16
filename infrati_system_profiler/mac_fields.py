from data_from_system_profiler import system_info_for_datatype
from qrcode import QRCode

# Hardware
hardware_specs = system_info_for_datatype('Hardware')
hardware_list = hardware_specs[0]['_items'][0]

# Asset Name
machine_name = hardware_list['machine_name']
print(machine_name)

# CPU Count/Type
cpu_type = hardware_list['cpu_type']
print(cpu_type)

# CPU Speed
processor_speed = hardware_list['current_processor_speed']
print(processor_speed)

# RAM
memory = hardware_list['physical_memory']
print(memory)

# Drive Count
# Capacity - Drive 1
# Model - Drive 1
# Serial # - Drive 1
# Capacity - Drive 2
# Model - Drive 2
# Serial # - Drive 2
# Capacity - Drive 3
# Model - Drive 3
# Serial # - Drive 3
# Capacity - Drive 4
# Model - Drive 4
# Serial # - Drive 4
# Capacity - Drive 5
# Model - Drive 5
# Serial # - Drive 5
# Drive Capacity - Internal
# Drive Capacity - Attached
# NIC Port Count - Fiber
# NIC Port Count - Copper
# IMEI
# Mobile Storage
# OS Version
# Display Size
# Display Port Count
# HDMI Count
# DVI Count
# VGA Count
# Mouse Asset #
# Mouse Serial #
# Num Pad Asset #
# Num Pad Serial #
