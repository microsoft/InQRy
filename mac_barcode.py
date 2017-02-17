from data_from_system_profiler import system_info_for_datatype
from qrcode import QRCode


system_categories = ['SerialATA', 'Hardware', 'Network']

# hardware_components = ['machine_model', 'serial_number', 'machine_name',
#                        'physical_memory', 'cpu_type',
#                        'current_processor_speed']

# Hardware
hardware_specs = system_info_for_datatype('Hardware')
hardware_list = hardware_specs[0]['_items'][0]

# Hardware - components
machine_model = hardware_list['machine_model']
serial_number = hardware_list['serial_number']
machine_name = hardware_list['machine_name']
memory = hardware_list['physical_memory']
cpu_type = hardware_list['cpu_type']
processor_speed = hardware_list['current_processor_speed']

# Storage
storage_specs = system_info_for_datatype('SerialATA')
storage_bay_1 = storage_specs[0]['_items'][0]['_items'][0]['device_model']
# storage_bay_2 = storage_specs[0]['_items'][0]['_items'][0]['device_model']
# storage_bay_3 = storage_specs[0]['_items'][0]['_items'][0]['device_model']
# storage_bay_4 = storage_specs[0]['_items'][0]['_items'][0]['device_model']
storage_keys = storage_specs[0]['_items'][0]['_items'][0].keys()

qr = QRCode()


def mac_desktop():
    qr.add_data('64655638')
    qr.add_data('\x09')
    qr.add_data('delay500ms')
    qr.add_data('\x20')
    qr.add_data('delay500ms')
    qr.add_data(machine_model)
    qr.add_data('delay500ms')
    qr.add_data('enter_key')
    qr.add_data('delay500ms')
    qr.add_data('\x09')
    qr.add_data('\x09')
    qr.add_data(memory)
    qr.add_data('\x09')
    qr.add_data(processor_speed)
    qr.add_data('\x09')
    qr.add_data(cpu_type)
    qr.add_data('\x09')
    qr.add_data(storage_bay_1)
    qr.add_data('\x09')
    qr.add_data('delay500ms')
    qr.add_data('\x20')
    qr.add_data('delay500ms')
    qr.add_data('Ready to Deploy')
    qr.add_data('enter_key')
    qr.add_data('delay500ms')
    qr.add_data('\x09')
    qr.add_data('\x09')
    qr.add_data('\x20')
    qr.add_data('delay500ms')
    qr.add_data('maclab')
    qr.add_data('enter_key')
    qr.add_data('\x09')
    qr.add_data('\x09')
    qr.add_data(serial_number)
    qr.add_data('\x09')
    qr.add_data(machine_name)
    qr.add_data('enter_key')
    img = qr.make_image()
    img.show()


def mac_laptop():
    pass


def ios_device():
    pass
