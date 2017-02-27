from inqry import mac_system_profiler

memory_data_type_command_output = '''Memory:

    Memory Slots:

      ECC: Disabled
      Upgradeable Memory: No

        BANK 0/DIMM0:

          Size: 8 GB
          Type: DDR3
          Speed: 1600 MHz
          Status: OK
          Manufacturer: 0x80AD
          Part Number: 0x484D5434314753364D465238432D50422020
          Serial Number: -

        BANK 1/DIMM0:

          Size: 8 GB
          Type: DDR3
          Speed: 1600 MHz
          Status: OK
          Manufacturer: 0x80AD
          Part Number: 0x484D5434314753364D465238432D50422020
          Serial Number: -
'''

result = mac_system_profiler.parse_command_output(memory_data_type_command_output)['Memory']['Memory Slots']


def test_parsing_memory_data_returns_dict():
    assert isinstance(result, dict)


def test_bank_0_is_accessible_as_expected():
    assert result['BANK 0/DIMM0']


def test_serial_number_is_none():
    assert result['BANK 0/DIMM0']['Serial Number'] is None
