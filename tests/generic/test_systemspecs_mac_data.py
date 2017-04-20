from inqry.system_specs import systemspecs
from tests.mac.macdisk.test_representing_internal_hdd_fusion_imac import test_disk as disk1
from tests.mac.macdisk.test_representing_internal_ssd_fusion_imac import test_disk as disk2

HARDWARE = {'Model Name': 'Mac Pro',
            'Model Identifier': 'MacPro6,1',
            'Processor Name': 'Quad-Core Intel Xeon E5',
            'Processor Speed': '3.7 GHz',
            'Number of Processors': 1,
            'Total Number of Cores': 4,
            'L2 Cache (per Core)': '256 KB',
            'L3 Cache': '10 MB',
            'Memory': '32 GB',
            'Boot ROM Version': 'MP61.0116.B21',
            'SMC Version (system)': '2.20f18',
            'Illumination Version': '1.4a6',
            'Serial Number (system)': 'F5KQH0P9F9VN',
            'Hardware UUID': '4D4C19C7-19C4-5678-A936-A419C4609AFD'}

INTERNAL_STORAGE = [disk1, disk2]

SYSTEM_SPECS = systemspecs.SystemSpecs(HARDWARE, INTERNAL_STORAGE)


def test_system_specs_can_be_instantiated_with_test_data():
    assert SYSTEM_SPECS


def test_assert_system_specs_storage():
    assert SYSTEM_SPECS.storage


def test_drive_bay_1_returns_correct_data():
    assert SYSTEM_SPECS.drive1 == '3.0 TB HDD (APPLE HDD ST3000DM001)'
