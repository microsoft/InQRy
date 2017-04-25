from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''
   Device Identifier:        disk0
   Device Node:              /dev/disk0
   Whole:                    Yes
   Part of Whole:            disk0
   Device / Media Name:      APPLE SSD AP0256J

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 PCI-Express
   SMART Status:             Not Supported

   Disk Size:                251.0 GB (251000193024 Bytes) (exactly 490234752 512-Byte-Units)
   Device Block Size:        4096 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          Internal
   Removable Media:          Fixed

   Solid State:              Yes
   OS 9 Drivers:             No
   Low Level Format:         Not supported
'''

test_disk = macdisk.create_from_diskutil_output(DISKUTIL_OUTPUT)


def test_disk_is_internal():
    assert test_disk.is_internal


def test_disk_is_not_external():
    assert test_disk.is_external is False


def test_device_name_is_correct():
    assert test_disk.device_name == 'APPLE SSD AP0256J'


def test_disk_is_ssd():
    assert test_disk.is_ssd


def test_size_is_correct():
    assert test_disk.size == '251.0 GB'


def test_removable_media():
    assert test_disk.removable_media == 'Fixed'


def test_is_not_removable():
    assert test_disk.is_fixed
