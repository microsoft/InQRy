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
    def __init__(self, form_type=None, user=None):
        super().__init__()
        self.form_type = form_type or 'Desktop'
        self.user = user or ''
        self.form_types = {
            'Desktop': [self.processor, self.memory, self.drive1, self.drive2, self.drive3, self.drive4],
            'Portable': [self.processor, self.memory, self.drive1],  # TODO: Use enumerate() for storage
            'Mobile': [self.imei, self.mobile_storage]}

    @property
    def processor(self) -> str:
        return '{} {}'.format(self.processor_speed, self.processor_name)

    def get_form_type_data(self) -> list:
        return self.form_types[self.form_type]

    def get_asset_sequence(self) -> str:
        asset_data = self.get_form_type_data()
        return ''.join([self.textify(component) for component in asset_data])

    def get_user_sequence(self) -> str:
        user_sequence = [self.space, self.user, self.enter, self.tab]
        return ''.join([self.delayify(char) for char in user_sequence])

    def new_asset(self, status=None) -> str:
        status = status or 'Ready'
        return self.listify(self.model_identifier) + self.get_asset_sequence() + self.listify(
            status) + self.get_user_sequence() + self.delayify(self.serial_number)

    def new_model(self) -> str:
        return self.textify(self.model_name) + self.tab * 2 + self.delayify(self.model_identifier)
