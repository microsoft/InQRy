import os
import sys
import inspect
from qrcode import QRCode

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
    inspect.getfile(inspect.currentframe()))[0],
    "/Users/erichanko/Projects/AutoInfra/mbu/modules/Infrastructure/InfraTi/Client/Environment")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from system_profiler_report_data import SystemProfilerReportData
from system_profiler import SystemProfiler

system_data = SystemProfiler().profile_for_data_type(
    ['SPHardwareDataType', 'SPStorageDataType'])


data_list = ['serial_number', 'machine_model', 'physical_memory', 'cpu_type',
             'current_processor_speed', 'machine_name',
             'com.apple.corestorage.lvg.name',
             'com.apple.corestorage.lvg.size',
             'com.apple.corestorage.lvg.freeSpace']


hardware = system_data[0]['_items'][0]
if system_data[1]['_items'][1]['com.apple.corestorage.lvg']:
    storage = system_data[1]['_items'][1]['com.apple.corestorage.lvg']
else:
    storage = system_data[1]['_items'][0]['com.apple.corestorage.lvg']


unique_component_list = []

qr_code = QRCode()


def singledata_barcode():
    for component in data_list:
        if hardware.get(component):
            unique_component = hardware.get(component)
        else:
            unique_component = storage.get(component)
        qr_code.add_data(unique_component)
        img = qr_code.make_image()
        img.show()
        qr_code.clear()


def multidata_barcode():
    for component in data_list:
        if hardware.get(component):
            unique_component = hardware.get(component)
        else:
            unique_component = storage.get(component)
        qr_code.add_data(unique_component)
        img = qr_code.make_image()
    img.show()


def error_code(reason):
    print(reason)


multidata_barcode()
