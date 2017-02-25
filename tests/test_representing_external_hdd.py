from inqry import macdisk

diskutil_output = '''
   Device Identifier:        disk5
   Device Node:              /dev/disk5
   Whole:                    Yes
   Part of Whole:            disk2
   Device / Media Name:      G-DRIVE PRO Thunderbolt

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 SATA
   SMART Status:             Verified

   Disk Size:                2.0 TB (2000179691520 Bytes) (exactly \
   3906600960 512-Byte-Units)
   Device Block Size:        512 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          External
   Removable Media:          Fixed

   Solid State:              No
   Virtual:                  No
   OS 9 Drivers:             No
   Low Level Format:         Not supported
   '''

test_disk = macdisk.create_from_diskutil_info_output(diskutil_output)


def test_disk_is_not_internal():
    assert test_disk.is_internal is False


def test_disk_is_external():
    assert test_disk.is_external


def test_device_name_is_correct():
    assert test_disk.device_name == 'G-DRIVE PRO Thunderbolt'


def test_disk_is_not_ssd():
    assert test_disk.is_ssd is False


def test_size_is_correct():
    assert test_disk.size == '2.0 TB'
