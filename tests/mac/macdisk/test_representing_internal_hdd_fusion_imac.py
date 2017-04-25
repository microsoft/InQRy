from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''
   Device Identifier:        disk0
   Device Node:              /dev/disk0
   Whole:                    Yes
   Part of Whole:            disk0
   Device / Media Name:      APPLE HDD ST3000DM001

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 SATA
   SMART Status:             Verified

   Disk Size:                3.0 TB (3000592982016 Bytes) (exactly 5860533168 512-Byte-Units)
   Device Block Size:        512 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          Internal
   Removable Media:          Fixed

   Solid State:              No
   Virtual:                  No
   OS 9 Drivers:             No
   Low Level Format:         Not supported
   '''

test_disk = macdisk.create_from_diskutil_output(DISKUTIL_OUTPUT)


def test_disk_is_not_internal():
    assert test_disk.is_internal


def test_disk_is_external():
    assert test_disk.is_external is False


def test_device_name_is_correct():
    assert test_disk.device_name == 'APPLE HDD ST3000DM001'


def test_disk_is_not_ssd():
    assert test_disk.is_ssd is False


def test_size_is_correct():
    assert test_disk.size == '3.0 TB'


def test_removable_media():
    assert test_disk.removable_media == 'Fixed'
