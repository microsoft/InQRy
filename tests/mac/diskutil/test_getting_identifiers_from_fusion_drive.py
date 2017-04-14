from inqry.system_specs import diskutil

DISKUTIL_LIST_OUTPUT_FUSION = """/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *121.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:          Apple_CoreStorage Macintosh HD            121.0 GB   disk0s2
   3:                 Apple_Boot Boot OS X               134.2 MB   disk0s3

/dev/disk1 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *3.0 TB     disk1
   1:                        EFI EFI                     209.7 MB   disk1s1
   2:          Apple_CoreStorage Macintosh HD            289.5 GB   disk1s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk1s3
   4:                  Apple_HFS Data                    2.7 TB     disk1s4

/dev/disk2 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Macintosh HD           +404.6 GB   disk2
                                 Logical Volume on disk0s2, disk1s2
                                 876DB79C-8794-4804-A4F2-B6D168CADECB
                                 Unencrypted Fusion Drive

/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *8.0 GB     disk3
   1:                        EFI EFI                     209.7 MB   disk3s1
   2:                  Apple_HFS InQRy                   7.7 GB     disk3s2"""


def test_only_physical_drives_included():
    expected_physical_disks_multiple_disks = ['/dev/disk0', '/dev/disk1', '/dev/disk3']
    identifiers = diskutil.get_physical_disk_identifiers(DISKUTIL_LIST_OUTPUT_FUSION)
    assert expected_physical_disks_multiple_disks == identifiers
