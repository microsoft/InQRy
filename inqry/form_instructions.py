import sys
from inqry.system_specs.systemspecs import SystemSpecs


class BarcodeData:
    delay = '~d'
    tab = '~t'
    enter = '~e'
    space = '\x20'

    def textify(self, value: str) -> str:
        return ''.join([self.delayify(item) for item in [value, self.tab] if item is not None])

    def listify(self, value: str) -> str:
        return ''.join([self.delayify(item) for item in [self.space, value, self.enter, self.tab]])

    def delayify(self, value: str, amount=1) -> str:
        delay_count = self.delay * amount
        return delay_count + value


class FormInstructions(SystemSpecs, BarcodeData):
    def __init__(self):
        super().__init__()
        self.form_types = {
            'Desktop': [self.processor, self.memory, self.drive1, self.drive2, self.drive3, self.drive4],
            'Portable': [self.processor, self.memory, self.drive1],  # TODO: Use enumerate() for storage
            'Mobile': [self.imei, self.mobile_storage]}

    @property
    def processor(self) -> str:
        return '{} {}'.format(self.processor_speed, self.processor_name)

    def get_asset_sequence(self, form_type) -> str:
        try:
            asset_data = self.form_types[form_type]
            return ''.join([self.textify(component) for component in asset_data])
        except TypeError('Form type is required.'):
            sys.exit(1)

    def get_user_sequence(self, user) -> str:
        try:
            user_sequence = [self.space, user, self.enter, self.tab]
            return ''.join([self.delayify(char) for char in user_sequence])
        except TypeError('User entry is required.'):
            sys.exit(1)

    def new_asset(self, asset_tag, form_type, user, status=None) -> str:
        status = status or 'Ready'
        return self.textify(asset_tag) + self.listify(self.model_identifier) + self.get_asset_sequence(
            form_type) + self.listify(status) + self.get_user_sequence(user) + self.delayify(self.serial_number)

    def new_model(self) -> str:
        return self.textify(self.model_name) + self.tab * 2 + self.delayify(self.model_identifier)

    def gui_helper(self, qrcode_type, asset_tag, form_type, user, status=None) -> str:
        gui_options = {'Asset': self.new_asset(asset_tag, form_type, user, status),
                       'Model': self.new_model()}
        return gui_options[qrcode_type]
