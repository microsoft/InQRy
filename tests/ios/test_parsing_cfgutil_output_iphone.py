from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0xA64D620D30D26":{"serialNumber":"F71SHPP0HG6W", "totalDiskCapacity":32000000000,
"deviceType":"iPhone9,1","IMEI":"359167076630320","color":"1"},"Errors":{"0xA64D620D30D26":{}}}, 
"Type":"CommandOutput","Devices":["0xA64D620D30D26"]}
'''

RESULT = cfgutil.parse_command_output(CFGUTIL_OUTPUT)


def test_getting_device_ecid():
    assert RESULT['Devices'] == ["0xA64D620D30D26"]


def test_getting_serial_using_device_value():
    ecid = RESULT['Devices'][0]
    assert RESULT['Output'][ecid]['serialNumber'] == 'F71SHPP0HG6W'
