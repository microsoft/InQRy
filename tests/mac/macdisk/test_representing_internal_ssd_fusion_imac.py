from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''
   Device Identifier:        disk0
   Device Node:              /dev/disk0
   Whole:                    Yes
   Part of Whole:            disk0
   Device / Media Name:      APPLE SSD SM0128G

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 PCI
   SMART Status:             Verified

   Disk Size:                121.3 GB (121332826112 Bytes) (exactly 236978176 512-Byte-Units)
   Device Block Size:        512 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          Internal
   Removable Media:          Fixed

   Solid State:              Yes
   Virtual:                  No
   OS 9 Drivers:             No
   Low Level Format:         Not supported
   Device Location:          "SSD"
'''

test_disk = macdisk.create_from_diskutil_output(DISKUTIL_OUTPUT)


def test_disk_is_internal():
    assert test_disk.is_internal


def test_disk_is_not_external():
    assert test_disk.is_external is False


def test_device_name_is_correct():
    assert test_disk.device_name == 'APPLE SSD SM0128G'


def test_disk_is_ssd():
    assert test_disk.is_ssd


def test_size_is_correct():
    assert test_disk.size == '121.3 GB'


def test_removable_media():
    assert test_disk.removable_media == 'Fixed'


def test_is_not_removable():
    assert test_disk.is_fixed
