from inqry.system_specs import ios_system_profiler

DEVICE_HARDWARE_OVERVIEW = {'serialNumber': 'F71SHPP0HG6W', 'totalDiskCapacity': 32000000000,
                            'deviceType': 'iPhone9,1', 'IMEI': '359167076630320', 'color': '1'}

test_device = ios_system_profiler.create_device_from_device_properties(DEVICE_HARDWARE_OVERVIEW)


def test_creating_device_from_hardware_overview():
    assert ios_system_profiler.create_device_from_device_properties(DEVICE_HARDWARE_OVERVIEW)


def test_getting_serial_number_from_device_specs_objects():
    assert test_device.serial_number == 'F71SHPP0HG6W'


def test_getting_imei_from_device_specs_object():
    assert test_device.imei == '359167076630320'
