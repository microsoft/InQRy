import json
import sys

from inqry import barcode


class FormInstructions():
    def __init__(self, data: json):
        self.data = json.loads(data)
        self.hardware = self.data['hardware']
        self.storage = self.data['storage']
        self.model_identifier = self.hardware['Model Identifier']
        self.model_name = self.hardware['Model Name']
        self.memory = self.hardware['Memory']
        self.processor = '{} {}'.format(self.hardware['Processor Speed'], self.hardware['Processor Name'])
        self.serial_number = self.hardware['Serial Number (system)']
        self.drive1 = self.storage['Drive 1']
        self.drive2 = self.storage.get('Drive 2', None)
        self.drive3 = self.storage.get('Drive 3', None)
        self.drive4 = self.storage.get('Drive 4', None)

        self.form_types = {
            'Desktop': [self.processor, self.memory, self.drive1, self.drive2, self.drive3, self.drive4],
            'Portable': [self.processor, self.memory, self.drive1]}

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
