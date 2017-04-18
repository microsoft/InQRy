from inqry.system_specs import mac_system_profiler

STORAGE_DATA_TYPE_COMMAND_OUTPUT = '''
Storage:

    ChangeOS:

      Available: 89.96 GB (89,955,459,072 bytes)
      Capacity: 120.99 GB (120,988,852,224 bytes)
      Mount Point: /Volumes/ChangeOS
      File System: Journaled HFS+
      Writable: Yes
      Ignore Ownership: No
      BSD Name: disk0s2
      Volume UUID: 371EE253-4D3D-3674-B1A8-78C8BC2EF3B8
      Physical Drive:
          Device Name: APPLE SSD SM128E
          Media Name: APPLE SSD SM128E Media
          Medium Type: SSD
          Protocol: SATA
          Internal: Yes
          Partition Map Type: GPT (GUID Partition Table)
          S.M.A.R.T. Status: Verified

    Mac OS X:

      Available: 965.17 GB (965,173,051,392 bytes)
      Capacity: 999.86 GB (999,860,912,128 bytes)
      Mount Point: /
      File System: Journaled HFS+
      Writable: Yes
      Ignore Ownership: No
      BSD Name: disk1s2
      Volume UUID: 2AE94EB9-0ECE-3E3A-87AE-B3A5E717D2E9
      Physical Drive:
          Device Name: APPLE HDD HTS541010A9E662
          Media Name: APPLE HDD HTS541010A9E662 Media
          Medium Type: Rotational
          Protocol: SATA
          Internal: Yes
          Partition Map Type: GPT (GUID Partition Table)
          S.M.A.R.T. Status: Verified

    1TB LaCie:

      Available: 349.39 GB (349,390,594,048 bytes)
      Capacity: 999.86 GB (999,860,912,128 bytes)
      Mount Point: /Volumes/1TB LaCie
      File System: Journaled HFS+
      Writable: Yes
      Ignore Ownership: Yes
      BSD Name: disk2s2
      Volume UUID: 0CCC608A-8679-33FE-9996-70A48555046A
      Physical Drive:
          Device Name: LaCie
          Media Name: LaCie Rugged FW/USB Media
          Protocol: FireWire
          Internal: No
          Partition Map Type: GPT (GUID Partition Table)

    1.5TB External:

      Available: 10.4 GB (10,400,120,832 bytes)
      Capacity: 1.5 TB (1,499,957,936,128 bytes)
      Mount Point: /Volumes/1.5TB External
      File System: HFS+
      Writable: Yes
      Ignore Ownership: Yes
      BSD Name: disk3s2
      Volume UUID: FE2E1EC6-FB63-3634-BE24-923260FA5187
      Physical Drive:
          Device Name: External USB 3.0
          Media Name: TOSHIBA External USB 3.0 Media
          Protocol: USB
          Internal: No
          Partition Map Type: GPT (GUID Partition Table)
'''

RESULT = mac_system_profiler.parse_command_output(STORAGE_DATA_TYPE_COMMAND_OUTPUT)['Storage']


def test_parsing_storage_data_returns_dict():
    assert isinstance(RESULT, dict)
