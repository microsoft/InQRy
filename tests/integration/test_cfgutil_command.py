from inqry.system_specs import cfgutil

hardware_overview = cfgutil.get_hardware_overview_for_all_devices()
device_properties = cfgutil.get_device_properties_from_cfgutil_output()


def test_get_hardware_overview_for_all_devices():
    assert hardware_overview


def test_get_device_properties_for_all_devices():
    assert device_properties


def test_hardware_overview_keys_are_correct_for_attached_device():
    first_device = hardware_overview[0]
    assert str(first_device.keys()) == "dict_keys(['serialNumber', 'totalDiskCapacity', 'IMEI', 'deviceType'])"


def test_device_property_keys_are_correct_for_attached_device():
    assert str(device_properties.keys()) == "dict_keys(['Command', 'Output', 'Type', 'Devices'])"
