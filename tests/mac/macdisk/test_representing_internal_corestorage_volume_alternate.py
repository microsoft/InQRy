from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''   Device Identifier:        disk1
   Device Node:              /dev/disk1
   Whole:                    Yes
   Part of Whole:            disk1
   Device / Media Name:      APPLE SSD SM1024G

   Volume Name:              Macintosh HD
   Mounted:                  Yes
   Mount Point:              /

   Content (IOContent):      Apple_HFS
   File System Personality:  Journaled HFS+
   Type (Bundle):            hfs
   Name (User Visible):      Mac OS Extended (Journaled)
   Journal:                  Journal size 81920 KB at offset 0x1d1f000
   Owners:                   Enabled

   OS Can Be Installed:      Yes
   Recovery Disk:            disk0s3
   Media Type:               Generic
   Protocol:                 PCI
   SMART Status:             Not Supported
   Volume UUID:              9B99BFB4-9D42-3C3C-9521-A2500A94522D
   Disk / Partition UUID:    05F5DF37-4C54-4810-82CE-9BF556A85116

   Disk Size:                999.3 GB (999334739968 Bytes) (exactly 1951825664 512-Byte-Units)
   Device Block Size:        512 Bytes

   Volume Total Space:       999.3 GB (999334739968 Bytes) (exactly 1951825664 512-Byte-Units)
   Volume Used Space:        652.6 GB (652630675456 Bytes) (exactly 1274669288 512-Byte-Units) (65.3%)
   Volume Available Space:   346.7 GB (346704064512 Bytes) (exactly 677156376 512-Byte-Units) (34.7%)
   Allocation Block Size:    4096 Bytes

   Read-Only Media:          No
   Read-Only Volume:         No

   Device Location:          Internal
   Removable Media:          Fixed

   Solid State:              Yes
   Virtual:                  Yes
   OS 9 Drivers:             No
   Low Level Format:         Not supported

   This disk is a Core Storage Logical Volume (LV).  Core Storage Information:
   LV UUID:                  05F5DF37-4C54-4810-82CE-9BF556A85116
   LVF UUID:                 8E4EEDC2-E576-4B2A-A6A0-35E0BA7AD239
   LVG UUID:                 264A357C-39D9-4F2A-AFE8-C606F0D7DAFF
   PV UUID (disk):           CDA3869A-FD99-4452-BF7F-D3360682D0BD (disk0s2)
   Fusion Drive:             No
   Encrypted:                Yes
'''

test_disk = macdisk.create_from_diskutil_output(DISKUTIL_OUTPUT)


def test_disk_is_internal():
    assert test_disk.is_internal


def test_disk_is_virtual():
    assert test_disk.is_virtual()


def test_device_name_is_correct():
    assert test_disk.device_name == 'APPLE SSD SM1024G'


def test_disk_is_ssd():
    assert test_disk.is_ssd


def test_size_is_correct():
    assert test_disk.size == '999.3 GB'


def test_removable_media():
    assert test_disk.removable_media == 'Fixed'
