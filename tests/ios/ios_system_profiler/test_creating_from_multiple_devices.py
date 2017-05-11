from inqry.system_specs import ios_system_profiler

DEVICE_1_HARDWARE_OVERVIEW = {"serialNumber": "F71SHPP0HG6W", "totalDiskCapacity": 32000000000,
                              "deviceType": "iPhone9,1", "IMEI": "359167076630320", "color": "1"}

DEVICE_2_HARDWARE_OVERVIEW = {"serialNumber": "DLXQK7WRGMLD",
                              "totalDiskCapacity": 31708938240, "deviceType": "iPad6,7", "color": "#3b3b3c"}

test_device_1 = ios_system_profiler.create_from_device_hardware_overview(DEVICE_1_HARDWARE_OVERVIEW)
test_device_2 = ios_system_profiler.create_from_device_hardware_overview(DEVICE_2_HARDWARE_OVERVIEW)


def test_getting_serial_number_from_device_specs_objects():
    assert test_device_2.serial_number == 'DLXQK7WRGMLD'


def test_getting_storage_returns_as_human_readable_string():
    assert test_device_1.mobile_storage == '32 GB'


def test_getting_storage_returns_as_human_readable_string_from_second_device():
    assert test_device_2.mobile_storage == '32 GB'
