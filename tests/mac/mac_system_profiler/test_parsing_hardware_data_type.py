from inqry.system_specs import mac_system_profiler

HARDWARE_DATA_TYPE_COMMAND_OUTPUT = '''
Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro10,1
      Processor Name: Intel Core i7
      Processor Speed: 2.6 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 16 GB
      Boot ROM Version: MBP101.00EE.B0B
      SMC Version (system): 2.3f36
      Serial Number (system): C02JL3REDKQ5
      Hardware UUID: 59CA6E54-8427-544E-8287-E02A0AD40F51
'''

RESULT = mac_system_profiler.parse_command_output(HARDWARE_DATA_TYPE_COMMAND_OUTPUT)['Hardware']['Hardware Overview']


def test_parsing_hardware_data_returns_dict():
    assert isinstance(RESULT, dict)


def test_model_identifier_is_correct():
    assert RESULT['Model Identifier'] == 'MacBookPro10,1'
