import pytest
from inqry.system_specs import cfgutil


@pytest.mark.skip
def test_get_hardware_overview_for_all_devices():
    assert cfgutil.get_hardware_overview_for_all_devices()


@pytest.mark.skip
def test_get_device_properties_for_all_devices():
    assert cfgutil.get_device_properties_from_cfgutil_output()


@pytest.mark.skip
def test_hardware_overview_keys_are_correct_for_attached_device():
    first_device = cfgutil.get_hardware_overview_for_all_devices()[0]
    assert str(first_device.keys()) == "dict_keys(['serialNumber', 'totalDiskCapacity', 'IMEI', 'deviceType'])"


@pytest.mark.skip
def test_device_property_keys_are_correct_for_attached_device():
    assert str(
        cfgutil.get_device_properties_from_cfgutil_output().keys()) == "dict_keys(['Command', 'Output', 'Type', 'Devices'])"
