from inqry.system_specs.systemspecs import SystemSpecs


class FormInstructions(SystemSpecs):
    def __init__(self, form_factor=None, user=None):
        super().__init__()
        self.processor = self.format_processor()
        self.short_delay = '~d'
        self.long_delay = '~d~d'
        self.tab = '~t'
        self.enter = '~e'
        self.space = '\x20'
        self.status = 'Ready'
        self.form_factor = form_factor or 'Desktop'
        self.user = user or ''
        self.fieldsets = {'Desktop': (self._text_box(self.processor) +
                                      self._text_box(self.memory) +
                                      self._text_box(self.drive1) +
                                      self._text_box(self.drive2) +
                                      self._text_box(self.drive3) +
                                      self._text_box(self.drive4)),

                          'Portable': (self._text_box(self.processor) +
                                       self._text_box(self.memory) +
                                       self._text_box(self.drive1)),

                          'New Model': (self._text_box(self.model_name) +
                                        [self.tab,
                                         self.tab,
                                         self.short_delay +
                                         self.model_identifier]),

                          'Mobile': (self._text_box(self.imei) +
                                     self._text_box(self.mobile_storage))}

    def get_instructions(self):
        if self.form_factor == 'New Model':
            return self.fieldsets['New Model']
        else:
            fieldset = self.fieldsets[self.form_factor]
            return self._common_fields(fieldset)

    def format_processor(self):
        return '{} {}'.format(self.processor_speed, self.processor_name)

    def _common_fields(self, unique_fields):
        user_sequence = [self.short_delay, self.space,
                         self.short_delay, self.user,
                         self.short_delay, self.enter,
                         self.short_delay, self.tab]
        return (self._list_box(self.model_identifier) + unique_fields + self._list_box(self.status) + user_sequence + [
            self.short_delay, self.serial_number])

    def _text_box(self, field_content):
        return [self.short_delay, field_content, self.tab]

    def _list_box(self, field_content):
        return [self.space, self.short_delay, field_content, self.long_delay, self.enter, self.long_delay, self.tab,
                self.short_delay]
