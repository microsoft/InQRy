from inqry.system_specs import systemspecs
from tests.windows.windisk.test_creating_a_disk_from_get_physical_disk_output import test_disk as disk1

HARDWARE = {'Model Name': 'Surface_Pro_3',
            'Manufacturer': 'Microsoft Corporation',
            'Serial Number (system)': '000048250353',
            'Model Identifier': 'Surface Pro 3',
            'Number of Processors': 1,
            'Total Number of Cores': 2,
            'Processor Speed': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz',
            'Memory': '8 GB',
            'Processor Name': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz'}

INTERNAL_STORAGE = [disk1]

SYSTEM_SPECS = systemspecs.SystemSpecs(HARDWARE, INTERNAL_STORAGE)


def test_system_specs_can_be_instantiated_with_test_data():
    assert SYSTEM_SPECS


def test_drive_bay_1_returns_correct_data():
    assert SYSTEM_SPECS.drive1 == '512 GB SSD (SAMSUNG MZHPV512HDGL-000H1)'
