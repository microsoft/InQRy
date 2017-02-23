import pytest
from inqry import macdisk

diskutil_info_disk0_output = '''
   Device Identifier:        disk0
   Device Node:              /dev/disk0
   Whole:                    Yes
   Part of Whole:            disk0
   Device / Media Name:      APPLE SSD SM1024G

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 PCI
   SMART Status:             Verified

   Disk Size:                1.0 TB (1000555581440 Bytes) (exactly 1954210120 512-Byte-Units)
   Device Block Size:        512 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Not applicable (no file system)

   Device Location:          Internal
   Removable Media:          Fixed

   Solid State:              Yes
   Virtual:                  No
   OS 9 Drivers:             No
   Low Level Format:         Not supported
'''

diskutil_info_disk2_output = '''
   Device Identifier:        disk2
   Device Node:              /dev/disk2
   Whole:                    Yes
   Part of Whole:            disk2
   Device / Media Name:      HGST HTS721010A9E630

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 SATA
   SMART Status:             Verified

   Disk Size:                1.0 TB (1000204886016 Bytes) (exactly 1953525168 512-Byte-Units)
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

diskutil_info_disk3_output = '''
   Device Identifier:        disk3
   Device Node:              /dev/disk3
   Whole:                    Yes
   Part of Whole:            disk3
   Device / Media Name:      HGST HTS721010A9E630

   Volume Name:              Not applicable (no file system)
   Mounted:                  Not applicable (no file system)
   File System:              None

   Content (IOContent):      GUID_partition_scheme
   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 SATA
   SMART Status:             Verified

   Disk Size:                1.0 TB (1000204886016 Bytes) (exactly 1953525168 512-Byte-Units)
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

disk_test_data_group = [
    diskutil_info_disk0_output, diskutil_info_disk2_output, diskutil_info_disk3_output]

disk_group = macdisk.disk_factory(disk_test_data_group)


def test_disk_factory_can_be_used_with_test_data():
    assert disk_group


def test_disk_0_is_internal():
    assert disk_group[0].is_internal


def test_disk_0_not_external():
    assert disk_group[1].is_internal is False


def test_disk_1_is_external():
    assert disk_group[1].is_external


def test_disk_1_is_not_external():
    assert disk_group[1].is_internal is False


def test_device_name_2_is_correct():
    assert disk_group[2].device_name == 'HGST HTS721010A9E630'


def test_disk_2_is_ssd():
    assert disk_group[2].is_ssd is False


def test_size_disk_0_is_correct():
    assert disk_group[0].size == '1.0 TB'
