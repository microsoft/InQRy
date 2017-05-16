from inqry.system_specs import ios_system_profiler

DEVICE_HARDWARE_OVERVIEW = {'serialNumber': 'DLXQK7WRGMLD', 'totalDiskCapacity': 31708938240,
                            'deviceType': 'iPad6,7', 'color': '#3b3b3c'}

test_device = ios_system_profiler.create_device_from_device_properties(DEVICE_HARDWARE_OVERVIEW)


def test_imei_value_is_none():
    assert test_device.imei is None


def test_device_type_is_correct():
    assert test_device.model_identifier == 'iPad6,7'
