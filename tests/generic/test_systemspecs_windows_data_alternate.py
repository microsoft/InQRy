import pytest
from inqry.system_specs import systemspecs
from tests.windows.windisk.test_representing_desktop_sata_ssd import test_disk as disk1

HARDWARE = {'Model Name': '',
            'Manufacturer': 'Microsoft Corporation',
            'Serial Number (system)': '',
            'Model Identifier': '',
            'Number of Processors': 1,
            'Total Number of Cores': 2,
            'Processor Speed': '1.70GHz',
            'Memory': '8 GB',
            'Processor Name': 'Intel(R) Core(TM) i7-4650U CPU'}

INTERNAL_STORAGE = [disk1]

OS_TYPE = 'win32'

WINDOWS_SYSTEM_SPECS = systemspecs.SystemSpecs(HARDWARE, INTERNAL_STORAGE, OS_TYPE)


def test_system_specs_can_be_instantiated_with_test_data():
    assert WINDOWS_SYSTEM_SPECS


def test_assert_system_specs_storage():
    assert WINDOWS_SYSTEM_SPECS.storage


def test_assert_blank_model_raises_assertion_error():
    with pytest.raises(AssertionError):
        assert WINDOWS_SYSTEM_SPECS.model_identifier


def test_assert_blank_name_raises_assertion_error():
    with pytest.raises(AssertionError):
        assert WINDOWS_SYSTEM_SPECS.model_name


def test_assert_blank_serial_raises_assertion_error():
    with pytest.raises(AssertionError):
        assert WINDOWS_SYSTEM_SPECS.serial_number


def test_system_specs_drive_count_returns_correct_amount():
    assert WINDOWS_SYSTEM_SPECS.drive_count == 1


def test_drive_bay_1_returns_correct_data():
    assert WINDOWS_SYSTEM_SPECS.drive1 == '512 GB SSD (SAMSUNG MZHPV512HDGL-000H1)'


def test_processor_speed_is_parsed_correctly():
    assert WINDOWS_SYSTEM_SPECS.processor_speed == '1.70GHz'


def test_processor_name_returns_name():
    assert WINDOWS_SYSTEM_SPECS.processor_name == 'Intel(R) Core(TM) i7-4650U CPU'


def test_system_specs_os_type():
    assert WINDOWS_SYSTEM_SPECS.os_type == 'win32'


def test_instructions_defaults_to_desktop_without_pc_model():
    assert WINDOWS_SYSTEM_SPECS.form_factor == 'Desktop'
