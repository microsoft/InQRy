from inqry.system_specs import macdisk

DISKUTIL_OUTPUT = '''   Device Identifier:        disk1
   Device Node:              /dev/disk1
   Whole:                    Yes
   Part of Whole:            disk1
   Device / Media Name:      APPLE SSD AP0256J

   Volume Name:              Macintosh HD
   Mounted:                  Yes
   Mount Point:              /

   Content (IOContent):      Apple_HFS
   File System Personality:  Journaled HFS+
   Type (Bundle):            hfs
   Name (User Visible):      Mac OS Extended (Journaled)
   Journal:                  Journal size 24576 KB at offset 0xfa0000
   Owners:                   Enabled

   OS Can Be Installed:      Yes
   Recovery Disk:            disk0s3
   Media Type:               Generic
   Protocol:                 PCI-Express
   SMART Status:             Not Supported
   Volume UUID:              BFDDBF0E-8AAC-30F3-9D51-FD9FB55A8324
   Disk / Partition UUID:    FE0F6BFA-AC2D-4395-B3B2-64C57F379F67

   Disk Size:                249.7 GB (249664372736 Bytes) (exactly 487625728 512-Byte-Units)
   Device Block Size:        4096 Bytes

   Volume Total Space:       249.7 GB (249664372736 Bytes) (exactly 487625728 512-Byte-Units)
   Volume Used Space:        193.8 GB (193815617536 Bytes) (exactly 378546128 512-Byte-Units) (77.6%)
   Volume Available Space:   55.8 GB (55848755200 Bytes) (exactly 109079600 512-Byte-Units) (22.4%)
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
   LV UUID:                  FE0F6BFA-AC2D-4395-B3B2-64C57F379F67
   LVF UUID:                 DA6A0D85-F308-41D5-95BA-9774B0A3A713
   LVG UUID:                 14494031-E586-49C0-8A48-BEBDAFF2548A
   PV UUID (disk):           F93B31BC-3637-4AA6-8E28-441F155E687C (disk0s2)
   Fusion Drive:             No
   Encrypted:                No
'''

test_disk = macdisk.create_from_diskutil_output(DISKUTIL_OUTPUT)


def test_disk_is_internal():
    assert test_disk.is_internal


def test_disk_is_virtual():
    assert test_disk.is_virtual()


def test_device_name_is_correct():
    assert test_disk.device_name == 'APPLE SSD AP0256J'


def test_disk_is_ssd():
    assert test_disk.is_ssd


def test_size_is_correct():
    assert test_disk.size == '249.7 GB'


def test_removable_media():
    assert test_disk.removable_media == 'Fixed'
