from inqry.system_specs import mac_system_profiler

MEMORY_DATA_TYPE_COMMAND_OUTPUT = '''Memory:

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

RESULT = mac_system_profiler.parse_command_output(MEMORY_DATA_TYPE_COMMAND_OUTPUT)['Memory']['Memory Slots']


def test_parsing_memory_data_returns_dict():
    assert isinstance(RESULT, dict)


def test_bank_0_is_accessible_as_expected():
    assert RESULT['BANK 0/DIMM0']


def test_serial_number_is_none():
    assert RESULT['BANK 0/DIMM0']['Serial Number'] is None
