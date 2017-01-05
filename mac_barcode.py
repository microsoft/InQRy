import os
import sys
import inspect
from qrcode import QRCode

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
    inspect.getfile(inspect.currentframe()))[0],
    "/Users/erichanko/Dropbox/Projects/AutoInfra/mbu/modules/Infrastructure/InfraTi/Client/Environment")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from system_profiler_report_data import SystemProfilerReportData
from system_profiler import SystemProfiler

system_data = SystemProfiler().profile_for_data_type(
    ['SPHardwareDataType', 'SPStorageDataType'])


data_list = ['machine_model', 'serial_number', 'physical_memory', 'cpu_type',
             'current_processor_speed', 'machine_name',
             'com.apple.corestorage.lvg.name',
             'com.apple.corestorage.lvg.size',
             'com.apple.corestorage.lvg.freeSpace']


hardware = system_data[0]['_items'][0]
storage = system_data[1]['_items'][1]['com.apple.corestorage.lvg']

qr = QRCode()


def singledata_barcode():
    for component in data_list:
        if hardware.get(component):
            unique_component = hardware.get(component)
        else:
            unique_component = storage.get(component)
        qr.add_data(unique_component)
        img = qr.make_image()
        img.show()
        qr.clear()


def multidata_barcode():
    for component in data_list:
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

singledata_barcode()

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
