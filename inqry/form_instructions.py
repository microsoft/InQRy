import sys

from inqry import barcode
from inqry.system_specs.systemspecs import SystemSpecs


class FormInstructions(SystemSpecs):
    def __init__(self):
        super().__init__()
        self.form_types = {
            'Desktop': [self.processor, self.memory, self.drive1, self.drive2, self.drive3, self.drive4],
            'Portable': [self.processor, self.memory, self.drive1],
            'Mobile': [self.imei, self.mobile_storage]}

    @property
    def processor(self) -> str:
        return '{} {}'.format(self.processor_speed, self.processor_name)

    def get_asset_sequence(self, form_type) -> str:
        try:
            asset_data = self.form_types[form_type]
            return ''.join([barcode.textify(component) for component in asset_data])
        except TypeError('Form type is required.'):
            sys.exit(1)

    def get_user_sequence(self, user) -> str:
        try:
            user_sequence = [barcode.SPACE, user, barcode.ENTER, barcode.TAB]
            return ''.join([barcode.delayify(char) for char in user_sequence])
        except TypeError('User entry is required.'):
            sys.exit(1)

    def new_asset(self, asset_tag, user, form_type) -> str:
        status = 'Ready'
        return barcode.textify(asset_tag) + barcode.listify(self.model_identifier) + self.get_asset_sequence(
                form_type) + barcode.listify(status) + self.get_user_sequence(user) + barcode.delayify(
            self.serial_number)

    def new_model(self) -> str:
        return barcode.textify(self.model_name) + barcode.tabify(2) + barcode.delayify(self.model_identifier)

    def gui_helper(self, qrcode_type, *args) -> str:
        qrcode_types = {'Create Asset': self.new_asset(*args),
                        'New Model': self.new_model()}
        return qrcode_types[qrcode_type]
