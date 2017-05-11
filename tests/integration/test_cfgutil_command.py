from inqry.system_specs import cfgutil


def test_get_hardware_overview_for_all_devices():
    device_summary = cfgutil.get_hardware_overview_for_all_devices()
    assert str(device_summary[0].keys()) == "dict_keys(['serialNumber', 'totalDiskCapacity', 'IMEI', 'deviceType'])"


def test_get_device_properties_from_cfgutil_output():
    hardware_overview = cfgutil.get_device_properties_from_cfgutil_output()
    assert str(hardware_overview.keys()) == "dict_keys(['Command', 'Output', 'Type', 'Devices'])"
