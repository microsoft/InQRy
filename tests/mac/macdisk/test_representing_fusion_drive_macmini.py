import pytest
from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''
   Device Identifier:        disk0
   Device Node:              /dev/disk0
   Whole:                    Yes
   Part of Whole:            disk0
   Device / Media Name:      APPLE SSD SM128E

   Volume Name:              Not applicable (no file system)

   Mounted:                  Not applicable (no file system)

   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 SATA
   SMART Status:             Verified

   Total Size:               121.3 GB (121332826112 Bytes) (exactly 236978176 512-Byte-Units)
   Volume Free Space:        Not applicable (no file system)
   Device Block Size:        512 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          Internal
   Removable Media:          No

   Solid State:              Yes
   Virtual:                  No
   OS 9 Drivers:             No
   Low Level Format:         Not supported
   Device Location:          "Lower"
'''


@pytest.fixture(scope="session")
def test_disk():
    return macdisk.create_from_diskutil_info_output(DISKUTIL_OUTPUT)


def test_disk_is_internal(test_disk):
    assert test_disk.is_internal


def test_disk_is_not_external(test_disk):
    assert test_disk.is_external is False


def test_device_name_is_correct(test_disk):
    assert test_disk.device_name == 'APPLE SSD SM128E'


def test_disk_is_ssd(test_disk):
    assert test_disk.is_ssd


def test_size_is_correct(test_disk):
    assert test_disk.size == '121.3 GB'


def test_removable_media(test_disk):
    assert test_disk.removable_media is False


def test_is_not_removable(test_disk):
    assert test_disk.is_fixed
