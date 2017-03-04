import pytest
from inqry.system_specs import systemspecs

HW_TEST_DATA = {'Model Name': 'Surface_Pro_3',
                'Manufacturer': 'Microsoft Corporation',
                'Serial Number (system)': '000048250353',
                'Model Identifier': 'Surface Pro 3',
                'Number of Processors': 1, 'Total Number of Cores': 2,
                'Processor Speed': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz',
                'Memory': '8 GB',
                'Processor Name': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz'}


# noinspection PyShadowingNames
@pytest.fixture(scope='session')
def systemspec_object():
    """Used as data for testing with a system profiler object"""
    return systemspecs.create_specs_from_system_profiler_hardware_output(HW_TEST_DATA)


# noinspection PyShadowingNames
def test_getting_value_from_key():
    assert HW_TEST_DATA.get('Manufacturer') == 'Microsoft Corporation'


# noinspection PyShadowingNames
def test_profile_instantiation_works():
    systemspecs.SystemSpecs(HW_TEST_DATA)


# noinspection PyShadowingNames
def test_operating_system_attribute(systemspec_object):
    assert hasattr(systemspec_object, "os_type")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_storage_attribute(systemspec_object):
    assert hasattr(systemspec_object, "storage")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_serial_attribute(systemspec_object):
    assert hasattr(systemspec_object, "serial")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_name_attribute(systemspec_object):
    assert hasattr(systemspec_object, "cpu_name")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_speed_attribute(systemspec_object):
    assert hasattr(systemspec_object, "cpu_speed")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_processors_attribute(systemspec_object):
    assert hasattr(systemspec_object, "cpu_processors")


# noinspection PyShadowingNames
def test_system_profiler_has_os_type_attribute(systemspec_object):
    assert bool(systemspec_object.os_type) is True


# noinspection PyShadowingNames
def test_model_is_string(systemspec_object):
    assert isinstance(systemspec_object.model, str)


# noinspection PyShadowingNames
def test_serial_is_string(systemspec_object):
    assert isinstance(systemspec_object.serial, str)


# noinspection PyShadowingNames
def test_name_is_string(systemspec_object):
    assert isinstance(systemspec_object.cpu_name, str)


# noinspection PyShadowingNames
def test_processors_is_integer(systemspec_object):
    assert isinstance(systemspec_object.cpu_processors, int)


# noinspection PyShadowingNames
def test_speed_is_string(systemspec_object):
    assert isinstance(systemspec_object.cpu_speed, str)


# noinspection PyShadowingNames
def test_cores_is_integer(systemspec_object):
    assert isinstance(systemspec_object.cpu_cores, int)


# noinspection PyShadowingNames
@pytest.mark.skip
def test_operating_system_fails_when_os_is_not_darwin_or_windows(systemspec_object):
    systemspec_object.os_type = 'Linux'
    with pytest.raises(OSError):
        systemspec_object.operating_system()


@pytest.mark.skip
def test_when_ios_device_is_connected():
    pass


@pytest.mark.skip
def test_ability_to_get_components_from_system_profile_object():
    pass


# def test_if_disk_list_is_list(test_disk):
#     assert hasattr(systemspecs.storage.internal_disks, list)


def test_asset_qr_code_as_list_all_method():
    assert hasattr(systemspec_object(), 'list_all')
