from inqry.system_specs import diskutil

DISKUTIL_LIST_OUTPUT = '''
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *751.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:          Apple_CoreStorage Macintosh HD            750.4 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.1 MB   disk0s3
/dev/disk1 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Macintosh HD           +750.1 GB   disk1
                                 Logical Volume on disk0s2
                                 2F555A8B-D884-485F-985A-3B7ADF7BFCB5
                                 Unlocked Encrypted

/dev/disk2 (disk image):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     Apple_partition_scheme                        +19.8 MB    disk2
   1:        Apple_partition_map                         32.3 KB    disk2s1
   2:                  Apple_HFS Flash Player            19.7 MB    disk2s2

/dev/disk3 (disk image):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        +35.8 MB    disk3
   1:                  Apple_HFS Synergy                 35.8 MB    disk3s1

/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *2.0 TB     disk4
   1:               Windows_NTFS My Passport             2.0 TB     disk4s1

/dev/disk5 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *2.0 TB     disk5
   1:                        EFI EFI                     209.7 MB   disk5s1
   2:                  Apple_HFS Builds                  1.5 TB     disk5s2
   3:                  Apple_HFS Source                  499.7 GB   disk5s3

/dev/disk6 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk6
   1:                        EFI EFI                     209.7 MB   disk6s1
   2:                 Apple_RAID                         999.9 GB   disk6s2
   3:                 Apple_Boot Boot OS X               134.2 MB   disk6s3

/dev/disk7 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk7
   1:                        EFI EFI                     209.7 MB   disk7s1
   2:                 Apple_RAID                         999.9 GB   disk7s2
   3:                 Apple_Boot Boot OS X               134.2 MB   disk7s3
   
/dev/disk8 (external, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS RedBackup              +2.0 TB     disk8

'''


def test_all_physical_disk_identifiers():
    expected_disk_ids = ['/dev/disk0', '/dev/disk1', '/dev/disk2', '/dev/disk3', '/dev/disk4', '/dev/disk5',
                         '/dev/disk6', '/dev/disk7', '/dev/disk8']
    assert expected_disk_ids == diskutil.get_all_physical_ids(DISKUTIL_LIST_OUTPUT)
