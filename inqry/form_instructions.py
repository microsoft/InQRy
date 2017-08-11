from inqry.system_specs.systemspecs import SystemSpecs


class BarcodeData:
    delay = '~d'
    tab = '~t'
    enter = '~e'
    space = '\x20'

    def textify(self, value: str) -> list:
        return [self.delayify(item) for item in [value, self.tab]]

    def listify(self, value: str) -> list:
        return [self.delayify(item) for item in [self.space, value, self.enter, self.tab]]

    def delayify(self, value: str, amount=1) -> str:
        delay_count = self.delay * amount
        return delay_count + value


class FormInstructions(SystemSpecs, BarcodeData):
    def __init__(self, form_factor=None, user=None):
        super().__init__()
        self.form_factor = form_factor or 'Desktop'
        self.user = user or ''
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

    def create_asset_fieldset(self) -> list:
        try:
            asset_fieldset = self.fieldset_table[self.form_factor]
        except KeyError:
            asset_fieldset = self.fieldset_table['New Model']
        return self.boxify_components(asset_fieldset)

    def basic_fields(self, unique_fields: list, user_sequence: list, status=None) -> list:
        status = status or 'Ready'
        return self.listify(self.model_identifier) + unique_fields + \
               self.listify(status) + user_sequence + self.delayify(self.serial_number)

    def boxify_components(self, *args) -> list:
        """
        Utilizes the textify() to return a list containing appropriate data to scan data into
        a text box and wrap that data around each of the given components
        """
        return [self.textify(component) for component in args]

    def new_model_fields(self, model: str, identifier: str) -> list:
        return [self.textify(model), self.tab * 2, self.delay, identifier]

    def user_sequence_fields(self) -> list:
        user_sequence = [self.space, self.user, self.enter, self.tab]
        return [self.delayify(char) for char in user_sequence]
