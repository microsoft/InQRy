from inqry.system_specs import _human_readable
from inqry.system_specs import cfgutil


def create_device_from_device_properties(properties):
    return DeviceSpecs(properties)


def create_devices_from_cfgutil_output():
    return [create_device_from_device_properties(properties) for properties in
            cfgutil.get_hardware_properties_for_attached_devices()]


class DeviceSpecs:
    def __init__(self, device_properties):
        self.serial_number = device_properties.get('serialNumber')
        self.model_identifier = device_properties.get('deviceType')
        self.mobile_storage = _human_readable(device_properties.get('totalDiskCapacity'))
        self.imei = device_properties.get('IMEI')
        self.os_type = 'iOS'
        self.processor_speed = None
        self.processor_name = None
        self.model_name = None
        self.memory = None
        self.drive1 = None
        self.drive2 = None
        self.drive3 = None
        self.drive4 = None

    def get_all_device_components(self):
        return {'Model Identifier': self.model_identifier,
                'Manufacturer': 'Apple',
                'Serial Number (system)': self.serial_number,
                'IMEI': self.imei,
                'Storage': self.mobile_storage}


def get_hardware_overview():
    return create_devices_from_cfgutil_output()
