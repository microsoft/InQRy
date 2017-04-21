from inqry.system_specs import systemspecs
from tests.windows.windisk.test_creating_a_disk_from_get_physical_disk_output import test_disk as disk1

HARDWARE = {'Model Name': 'Surface_Pro_3',
            'Manufacturer': 'Microsoft Corporation',
            'Serial Number (system)': '000048250353',
            'Model Identifier': 'Surface Pro 3',
            'Number of Processors': 1,
            'Total Number of Cores': 2,
            'Processor Speed': '1.70GHz',
            'Memory': '8 GB',
            'Processor Name': 'Intel(R) Core(TM) i7-4650U CPU'}

INTERNAL_STORAGE = [disk1]

SYSTEM_SPECS = systemspecs.SystemSpecs(HARDWARE, INTERNAL_STORAGE)


def test_system_specs_can_be_instantiated_with_test_data():
    assert SYSTEM_SPECS


def test_assert_system_specs_storage():
    assert SYSTEM_SPECS.storage


def test_system_specs_drive_count_returns_correct_amount():
    assert SYSTEM_SPECS.drive_count == 1


def test_drive_bay_1_returns_correct_data():
    assert SYSTEM_SPECS.drive1 == '512 GB SSD (SAMSUNG MZHPV512HDGL-000H1)'


def test_cpu_speed_is_parsed_correctly():
    assert SYSTEM_SPECS.cpu_speed == '1.70GHz'


def test_cpu_name_returns_name():
    assert SYSTEM_SPECS.cpu_name == 'Intel(R) Core(TM) i7-4650U CPU'
