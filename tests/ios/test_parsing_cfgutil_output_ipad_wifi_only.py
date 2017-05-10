from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0x970E80428AC26":{"serialNumber":"DLXQK7WRGMLD",
"totalDiskCapacity":31708938240,"deviceType":"iPad6,7","color":"#3b3b3c"},"Errors":{"0x970E80428AC26":{"IMEI":{
"Domain":"com.apple.configurator.MobileDeviceKit.amd.error","FailureReason":"","Message":"The value is missing.",
"Code":-402653163}}}},"Type":"CommandOutput","Devices":["0x970E80428AC26"]}
'''

RESULT = cfgutil.parse_command_output(CFGUTIL_OUTPUT)


def test_getting_device_ecid():
    assert cfgutil.get_device_ecids(RESULT) == ["0x970E80428AC26"]


def test_getting_serial_using_device_value():
    ecid = RESULT['Devices'][0]
    assert RESULT['Output'][ecid]['serialNumber'] == 'DLXQK7WRGMLD'
