import pytest
from inqry.system_specs import diskutil

DISKUTIL_LIST_OUTPUT = '''
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         251.0 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:          Apple_CoreStorage Macintosh HD            250.0 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3

/dev/disk1 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Macintosh HD           +249.7 GB   disk1
                                 Logical Volume on disk0s2
                                 FE0F6BFA-AC2D-4395-B3B2-64C57F379F67
                                 Unencrypted

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *8.0 GB     disk2
   1:                  Apple_HFS InQRy                   8.0 GB     disk2s1
'''


def test_getting_internal_physical_drives():
    expected_internal_disks = ['/dev/disk0']
    assert expected_internal_disks == diskutil.get_internal_physical_disk_ids(DISKUTIL_LIST_OUTPUT)


def test_only_physical_drives_included():
    expected_physical_disks = ['/dev/disk2']
    assert expected_physical_disks == diskutil.get_external_physical_disk_ids(DISKUTIL_LIST_OUTPUT)


def test_all_physical_disk_identifiers():
    expected_disk_ids = ['/dev/disk0', '/dev/disk2']
    assert expected_disk_ids == diskutil.get_all_physical_ids(DISKUTIL_LIST_OUTPUT)
