from inqry.system_specs.systemspecs import SystemSpecs


class BarcodeData:
    def __init__(self):
        self.delay = '~d'
        self.tab = '~t'
        self.enter = '~e'
        self.space = '\x20'

    def textify(self, value: str) -> list:
        return [self.delay, value, self.tab]

    def listify(self, value: str) -> list:
        return [self.delayify(item) for item in [self.space, value, self.enter, self.tab]]

    def delayify(self, value: str, amount=1) -> str:
        delay_count = self.delay * amount
        return delay_count + value


class FormInstructions(SystemSpecs, BarcodeData):
    def __init__(self, form_factor=None, user=None):
        super().__init__()
        self.status = 'Ready'
        self.form_factor = form_factor or 'Desktop'
        self.user_sequence = [self.space, user, self.enter, self.tab]
        self.fieldset_table = {
            'Desktop': [self.processor, self.memory, self.drive1, self.drive2, self.drive3, self.drive4],
            'Portable': [self.processor, self.memory, self.drive1],  # TODO: Use enumerate() for storage
            'Mobile': [self.imei, self.mobile_storage],
            'New Model': [self.model_name, self.model_identifier]}

    @property
    def processor(self) -> str:
        return '{} {}'.format(self.processor_speed, self.processor_name)

    def instruction_steps(self) -> list:
        asset_fieldset = self.create_asset_fieldset()
        user_fieldset = self.user_sequence_fields()
        return self.basic_fields(asset_fieldset, user_fieldset)

    def create_asset_fieldset(self):
        try:
            asset_fieldset = self.fieldset_table[self.form_factor]
        except KeyError:
            asset_fieldset = self.fieldset_table['New Model']
        return self.add_text_to_components(asset_fieldset)

    def basic_fields(self, unique_fields: list, user_sequence: list) -> list:
        return self.listify(self.model_identifier) + unique_fields + \
               self.listify(self.status) + user_sequence + self.delayify(self.serial_number)

    def add_text_to_components(self, *args) -> list:
        return [self.textify(component) for component in args]

    def new_model_fields(self, model: str, identifier: str):
        return [self.textify(model), self.tab * 2, self.delay, identifier]

    def user_sequence_fields(self):
        return [self.delayify(char) for char in self.user_sequence]
