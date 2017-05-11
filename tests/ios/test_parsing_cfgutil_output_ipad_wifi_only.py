from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0x970E80428AC26":{"serialNumber":"DLXQK7WRGMLD",
"totalDiskCapacity":31708938240,"deviceType":"iPad6,7","color":"#3b3b3c"},"Errors":{"0x970E80428AC26":{"IMEI":{
"Domain":"com.apple.configurator.MobileDeviceKit.amd.error","FailureReason":"","Message":"The value is missing.",
"Code":-402653163}}}},"Type":"CommandOutput","Devices":["0x970E80428AC26"]}
'''

DEVICE_HARDWARE_OVERVIEW = {'serialNumber': 'DLXQK7WRGMLD', 'totalDiskCapacity': 31708938240,
                            'deviceType': 'iPad6,7', 'color': '#3b3b3c'}

RESULT = cfgutil.parse_cfgutil_output(CFGUTIL_OUTPUT)

test_device = cfgutil.create_from_device_hardware_overview(DEVICE_HARDWARE_OVERVIEW)


def test_getting_device_ecid():
    assert cfgutil.get_all_device_ecids(CFGUTIL_OUTPUT) == ["0x970E80428AC26"]


def test_getting_serial_using_device_value():
    ecid = RESULT['Devices'][0]
    assert RESULT['Output'][ecid]['serialNumber'] == 'DLXQK7WRGMLD'


def test_getting_ecid():
    assert RESULT['Devices'] == ["0x970E80428AC26"]


def test_getting_device_hardware_overview():
    assert cfgutil.get_hardware_overview_for_all_devices(CFGUTIL_OUTPUT) == [{
        'serialNumber': 'DLXQK7WRGMLD', 'totalDiskCapacity': 31708938240,
        'deviceType': 'iPad6,7', 'color': '#3b3b3c'}]


def test_imei_value_is_none():
    assert test_device.imei is None


def test_device_type_is_correct():
    assert test_device.model_identifier == 'iPad6,7'
