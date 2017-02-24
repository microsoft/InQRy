import pytest
from inqry import system_profiler
from inqry import systemspecs


# noinspection PyUnusedLocal
@pytest.fixture(scope="session")
def hw_data_fixture():
    """Used as data for testing with system profiler output"""
    return system_profiler.hardware()


# noinspection PyShadowingNames,PyUnusedLocal
@pytest.fixture(scope="session")
def profile_fixture(hw_data_fixture):
    """Used as data for testing with a system profiler object"""
    return systemspecs.create_specs_from_system_profiler_hardware_output(
        hw_data_fixture)


# noinspection PyShadowingNames
def test_getting_value_from_key(hw_data_fixture):
    assert hw_data_fixture.get('Boot ROM Version') == 'MBP112.0138.B21'


# noinspection PyShadowingNames
def test_profile_instantiation_works():
    systemspecs.SystemSpecs(hw_data_fixture)


# noinspection PyShadowingNames
def test_operating_system_attribute(profile_fixture):
    assert hasattr(profile_fixture, "operating_system")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_storage_attribute(profile_fixture):
    assert hasattr(profile_fixture, "storage")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_serial_attribute(profile_fixture):
    assert hasattr(profile_fixture, "serial")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_name_attribute(profile_fixture):
    assert hasattr(profile_fixture, "cpu_name")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_speed_attribute(profile_fixture):
    assert hasattr(profile_fixture, "cpu_speed")


# noinspection PyShadowingNames
def test_that_system_profile_object_has_cpu_processors_attribute(
        profile_fixture):
    assert hasattr(profile_fixture, "cpu_processors")


# noinspection PyShadowingNames
def test_system_profiler_has_os_type_attribute(profile_fixture):
    assert bool(profile_fixture.os_type) is True


# noinspection PyShadowingNames
@pytest.mark.skip
def test_operating_system_fails_when_os_is_not_darwin_or_windows(
        profile_fixture):
    profile_fixture.os_type = 'Linux'
    with pytest.raises(OSError):
        profile_fixture.operating_system()


@pytest.mark.skip
def test_when_ios_device_is_connected():
    pass


@pytest.mark.skip
def test_ability_to_get_components_from_system_profile_object():
    pass


def test_mac_hardware_method_output_data_type_is_system_specs_class():
    assert isinstance(systemspecs.get_mac_hardware(), systemspecs.SystemSpecs)
