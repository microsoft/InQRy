import pytest
from inqry.systemprofile import SystemProfile, mac_hardware

hardware_test_data_as_dict = {
    'Hardware':
        {
            'Hardware Overview':
                {
                    'Model Name': 'MacBook Pro',
                    'Model Identifier': 'MacBookPro11,2',
                    'Processor Name': 'Intel Core i7',
                    'Processor Speed': '2.2 GHz',
                    'Number of Processors': 1,
                    'Total Number of Cores': 4,
                    'L2 Cache (per Core)': '256 KB',
                    'L3 Cache': '6 MB', 'Memory': '16 GB',
                    'Boot ROM Version': 'MBP112.0138.B21',
                    'SMC Version (system)': '2.18f15',
                    'Serial Number (system)': 'C02NT9WJG3QC',
                    'Hardware UUID': '7BE2608D-6373-52C7-B5FB-442C261A71A4'}}}

hardware_test_data_as_yaml = """
    Hardware:

        Hardware Overview:

          Model Name: Mac Pro
          Model Identifier: MacPro6,1
          Processor Name: Quad-Core Intel Xeon E5
          Processor Speed: 3.7 GHz
          Number of Processors: 1
          Total Number of Cores: 4
          L2 Cache (per Core): 256 KB
          L3 Cache: 10 MB
          Memory: 32 GB
          Boot ROM Version: MP61.0116.B21
          SMC Version (system): 2.20f18
          Illumination Version: 1.4a6
          Serial Number (system): F5KQH0P9F9VN
          Hardware UUID: 4D4C19C7-19C4-5678-A936-A419C4609AFD"""


def test_empty_profile_instantiation_works():
    SystemProfile()


def test_that_system_profile_object_operating_system_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "operating_system")


def test_that_system_profile_object_has_storage_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "storage")


def test_that_system_profile_object_has_serial_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "serial")


def test_that_system_profile_object_has_cpu_name_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "cpu_name")


def test_that_system_profile_object_has_cpu_speed_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "cpu_speed")


def test_that_system_profile_object_has_cpu_processors_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "cpu_processors")


def test_that_system_profile_object_has_cpu_cores_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "cpu_cores")


def test_that_system_profile_object_has_model_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "model")


def test_that_system_profile_object_has_name_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "name")


def test_that_system_profile_object_has_memory_attribute():
    sp = SystemProfile()
    assert hasattr(sp, "memory")


@pytest.mark.skip
def test_when_ios_device_is_connected():
    pass


@pytest.mark.skip
def test_ability_to_get_components_from_system_profile_object():
    pass


def test_mac_hardware_method_output_data_type_is_dictionary():
    assert isinstance(mac_hardware(), dict)


def test_system_profiler_has_os_type_attribute():
    sp = SystemProfile()
    assert sp.os_type


def test_operating_system_method_fails_when_operating_system_is_not_darwin_or_windows():
    sp = SystemProfile()
    sp.os_type = 'Linux'
    with pytest.raises(OSError):
        sp.operating_system()
