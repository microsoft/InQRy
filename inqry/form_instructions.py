import sys
from inqry.system_specs.systemspecs import SystemSpecs
from inqry import barcode


class FormInstructions:
    def __init__(self, specs: SystemSpecs):
        self.processor = '{} {}'.format(specs.processor_speed, specs.processor_name)
        self.form_types = {'Desktop': [self.processor, specs.memory,
                                       specs.drive1, specs.drive2,
                                       specs.drive3, specs.drive4],}
        self.model_identifier = specs.model_identifier
        self.model_name = specs.model_name
        self.serial_number = specs.serial_number

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
        return barcode.textify(self.model_name) + barcode.tabify(2) + barcode.delayify(
            self.model_identifier)

    def gui_helper(self, qrcode_type, *args) -> str:
        qrcode_types = {'Create Asset': self.new_asset(*args),
                        'New Model': self.new_model()}
        return qrcode_types[qrcode_type]
