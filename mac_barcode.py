from data_from_system_profiler import data_from_system_profiler
from qrcode import QRCode

components = ['machine_model', 'serial_number', 'physical_memory', 'cpu_type',
              'current_processor_speed', 'machine_name',
              'com.apple.corestorage.lvg.name',
              'com.apple.corestorage.lvg.size',
              'com.apple.corestorage.lvg.freeSpace']

# hardware = system_data[0]['_items'][0]
# storage = system_data[1]['_items'][0]['com.apple.corestorage.lvg']

qr = QRCode()


def multidata_barcode():
    for component in components:
        if hardware.get(component):
            unique_component = hardware.get(component)
        else:
            unique_component = storage.get(component)
        qr.add_data(unique_component)
        qr.add_data('\x09')

    img = qr.make_image()
    img.show()


def error_code(reason):
    print(reason)


def master_scan():
    qr.code.add_data(hardware.get(data_list[1]))


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
