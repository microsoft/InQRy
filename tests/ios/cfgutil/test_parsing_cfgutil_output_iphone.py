from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0xA64D620D30D26":{"serialNumber":"F71SHPP0HG6W", "totalDiskCapacity":32000000000,
"deviceType":"iPhone9,1","IMEI":"359167076630320","color":"1"},"Errors":{"0xA64D620D30D26":{}}}, 
"Type":"CommandOutput","Devices":["0xA64D620D30D26"]}
'''

RESULT = cfgutil.parse_cfgutil_output(CFGUTIL_OUTPUT)


def test_getting_device_ecid():
    assert cfgutil.get_all_device_ecids(CFGUTIL_OUTPUT) == ["0xA64D620D30D26"]


def test_getting_ecid():
    assert RESULT['Devices'] == ["0xA64D620D30D26"]


def test_getting_serial_using_device_value():
    ecid = RESULT['Devices'][0]
    assert RESULT['Output'][ecid]['serialNumber'] == 'F71SHPP0HG6W'


def test_getting_device_hardware_overview():
    assert cfgutil.get_hardware_overview_for_all_devices(CFGUTIL_OUTPUT) == [{
        'serialNumber': 'F71SHPP0HG6W', 'totalDiskCapacity': 32000000000,
        'deviceType': 'iPhone9,1', 'IMEI': '359167076630320', 'color': '1'}]
