from inqry.system_specs import ios_system_profiler

IPHONE_PROPERTIES = {"serialNumber": "F71SHPP0HG6W", "totalDiskCapacity": 32000000000,
                     "deviceType": "iPhone9,1", "IMEI": "359167076630320", "color": "1"}

IPAD_PROPERTIES = {"serialNumber": "DLXQK7WRGMLD",
                   "totalDiskCapacity": 31708938240, "deviceType": "iPad6,7", "color": "#3b3b3c"}

test_device_iphone = ios_system_profiler.create_device_from_device_properties(IPHONE_PROPERTIES)
test_device_ipad = ios_system_profiler.create_device_from_device_properties(IPAD_PROPERTIES)


def test_getting_serial_number_from_device_specs_objects():
    assert test_device_ipad.serial_number == 'DLXQK7WRGMLD'


def test_getting_non_existent_imei_from_ipad():
    assert test_device_ipad.imei is None


def test_getting_non_existent_imei_from_iphone():
    assert test_device_ipad.imei == '359167076630320'


def test_getting_storage_returns_as_human_readable_string():
    assert test_device_iphone.mobile_storage == '32 GB'


def test_getting_storage_returns_as_human_readable_string_from_second_device():
    assert test_device_ipad.mobile_storage == '32 GB'
