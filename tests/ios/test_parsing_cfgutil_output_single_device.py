CFGUTIL_OUTPUT = '''totalDiskCapacity:
32000000000

color:
1

IMEI:
359167076630320

serialNumber:
F71SHPP0HG6W

deviceType:
iPhone9,1

'''

RESULT = cfgutil.parse_command_output(CFGUTIL_OUTPUT)


def test_model_identifier_is_correct():
    assert RESULT['Model Identifier'] == 'MacBookPro10,1'


def test_serial_number_is_correct():
    assert RESULT['Serial Number (system)'] == 'C02JL3REDKQ5'