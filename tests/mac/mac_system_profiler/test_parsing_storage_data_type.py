from inqry.system_specs import mac_system_profiler

STORAGE_DATA_TYPE_COMMAND_OUTPUT = '''
Storage:

    Macintosh HD:

      Available: 87.54 GB (87,536,078,848 bytes)
      Capacity: 249.66 GB (249,664,372,736 bytes)
      Mount Point: /
      File System: Journaled HFS+
      Writable: Yes
      Ignore Ownership: No
      BSD Name: disk1
      Volume UUID: BFDDBF0E-8AAC-30F3-9D51-FD9FB55A8324
      Logical Volume:
          Revertible: Yes (no decryption required)
          Encrypted: No
          LV UUID: FE0F6BFA-AC2D-4395-B3B2-64C57F379F67
      Logical Volume Group:
          Name: Macintosh HD
          Size: 250.04 GB (250,035,572,736 bytes)
          Free Space: 18.9 MB (18,878,464 bytes)
          LVG UUID: 14494031-E586-49C0-8A48-BEBDAFF2548A
      Physical Volumes:
        disk0s2:
          Device Name: APPLE SSD AP0256J
          Media Name: APPLE SSD AP0256J Media
          Size: 250.04 GB (250,035,572,736 bytes)
          Medium Type: SSD
          Protocol: PCI-Express
          Internal: Yes
          Partition Map Type: GPT (GUID Partition Table)
          Status: Online
          PV UUID: F93B31BC-3637-4AA6-8E28-441F155E687C
'''

RESULT = mac_system_profiler.parse_command_output(STORAGE_DATA_TYPE_COMMAND_OUTPUT)['Storage']['Macintosh HD']
print(RESULT.keys())


def test_parsing_memory_data_returns_dict():
    assert isinstance(RESULT, dict)


def test_bank_0_is_accessible_as_expected():
    assert print(RESULT.keys())

#
#
# def test_serial_number_is_none():
#     assert RESULT['BANK 0/DIMM0']['Serial Number'] is None
