from data_from_system_profiler import system_info_for_datatype
from qrcode import QRCode


system_categories = ['SerialATA', 'Hardware', 'Network']

hardware_components = ['machine_model', 'serial_number', 'physical_memory',
                       'cpu_type', 'current_processor_speed', 'machine_name']


hardware_specs = system_info_for_datatype('Hardware')
storage_specs = system_info_for_datatype('SerialATA')
network_specs = system_info_for_datatype('Network')

hardware = hardware_specs[0]['_items'][0]
storage_keys = storage_specs[0]['_items'][0]['_items'][0].keys()
storage = storage_specs[0]['_items'][0]['_items'][0]['device_model']


# qr = QRCode()
#
#
# def generate_item_list(datatype):
#     data = system_info_for_datatype(datatype)
#     items = data[0]['_items'][0]
#     print(type(items))
#     return items
#
#
# generate_item_list('Hardware')


# for system_category in system_categories:
#     generate_item_list(system_category)

# empty_dict = {}
# for component in hardware_components:
#     unique_hardware_values = generate_item_list('Hardware')
#     empty_dict[component] = unique_hardware_values[component]
#
# for component in storage_components:
#     unique_storage_values = generate_item_list('Storage')
#     empty_dict[component] = unique_storage_values[component]


# def multidata_barcode():
#     for component in components:
#         if hardware.get(component):
#             unique_component = hardware.get(component)
#         else:
#             unique_component = storage.get(component)
#         qr.add_data(unique_component)
#         qr.add_data('\x09')
#
#     img = qr.make_image()
#     img.show()


# def error_code(reason):
#     print(reason)


# data_list = []


# def master_scan():
#     qr.code.add_data(hardware.get(data_list[1]))


# GENERIC
# Asset Tag
# Model
# Status
# Serial
# Asset Name
# Company
# Purchase Date
# Supplier
# Order Number
# Purchase Cost
# Warranty
# Notes
# Default Location

# COMPUTER
# Asset Tag
# Model
# Processor
# RAM
# Storage
# Status
# Serial
# Asset Name
# Company
# Purchase Date
# Supplier
# Order Number
# Purchase Cost
# Warranty
# Notes
# Default Location
