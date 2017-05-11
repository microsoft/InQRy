from inqry.system_specs import _human_readable
from inqry.system_specs import cfgutil


def create_from_device_hardware_overview(hardware_overview):
    return DeviceSpecs(hardware_overview)


def create_devices_from_cfgutil_output():
    return [create_from_device_hardware_overview(device_hardware_overview) for device_hardware_overview in
            cfgutil.get_hardware_overview_for_all_devices()]


class DeviceSpecs:
    def __init__(self, device_hardware_overview):
        self.serial_number = device_hardware_overview['serialNumber']
        self.model_identifier = device_hardware_overview['deviceType']
        self.storage = _human_readable(device_hardware_overview['totalDiskCapacity'])
        self.os_type = 'iOS'

        try:
            self.imei = device_hardware_overview['IMEI']
        except KeyError:
            self.imei = None

    def get_all_ios_system_components(self):
        return {'Model Identifier': self.model_identifier,
                'Manufacturer': 'Apple',
                'Serial Number (system)': self.serial_number,
                'IMEI': self.imei}


def get_hardware_overview():
    return create_devices_from_cfgutil_output()
