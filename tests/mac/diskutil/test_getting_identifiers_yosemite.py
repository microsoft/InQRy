from inqry.system_specs import diskutil

DISKUTIL_LIST_OUTPUT = '''/dev/disk0
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *42.9 GB    disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                  Apple_HFS Macintosh HD            42.1 GB    disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
'''


def test_all_disk_identifiers():
    expected_disk_ids = ['/dev/disk0']
    assert expected_disk_ids == diskutil.get_all_physical_ids(DISKUTIL_LIST_OUTPUT)
