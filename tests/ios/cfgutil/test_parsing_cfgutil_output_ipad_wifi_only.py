from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0x970E80428AC26":{"serialNumber":"DLXQK7WRGMLD",
"totalDiskCapacity":31708938240,"deviceType":"iPad6,7","color":"#3b3b3c"},"Errors":{"0x970E80428AC26":{"IMEI":{
"Domain":"com.apple.configurator.MobileDeviceKit.amd.error","FailureReason":"","Message":"The value is missing.",
"Code":-402653163}}}},"Type":"CommandOutput","Devices":["0x970E80428AC26"]}
'''

RESULT = cfgutil.get_device_summary_from_cfgutil_output(CFGUTIL_OUTPUT)


def test_getting_serial_using_device_value():
    ecid = '0x970E80428AC26'
    assert RESULT['Output'][ecid]['serialNumber'] == 'DLXQK7WRGMLD'


def test_getting_ecid():
    assert RESULT['Devices'] == ["0x970E80428AC26"]


def test_getting_hardware_overview_for_all_devices():
    hardware_overview = cfgutil.get_hardware_overview_for_all_devices(RESULT)
    assert hardware_overview == [{"serialNumber": "DLXQK7WRGMLD",
                                  "totalDiskCapacity": 31708938240, "deviceType": "iPad6,7", "color": "#3b3b3c"}]
