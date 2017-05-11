class FormInstructions:
    def __init__(self, specs, form_factor=None, user=None):
        self.short_delay = '~d'
        self.long_delay = '~d~d'
        self.tab = '~t'
        self.enter = '~e'
        self.space = '\x20'
        self.status = 'Ready'
        self.model_id = specs.model_identifier
        self.serial = specs.serial_number
        self.fieldset = form_factor or 'Desktop'
        self.user = user or ''
        self.fieldsets = {'Desktop': (self._text_box('{} {}'.format(specs.processor_speed, specs.processor_name)) +
                                      self._text_box(specs.memory) +
                                      self._text_box(specs.drive1) +
                                      self._text_box(specs.drive2) +
                                      self._text_box(specs.drive3) +
                                      self._text_box(specs.drive4)),

                          'Portable': (self._text_box('{} {}'.format(specs.processor_speed, specs.processor_name)) +
                                       self._text_box(specs.memory) +
                                       self._text_box(specs.drive1)),

                          'New Model': (self._text_box(specs.model_name) +
                                        [self.tab,
                                         self.tab,
                                         self.short_delay +
                                         self.model_id]),

                          'Mobile': (self._text_box(specs.imei) +
                                     self._text_box(specs.mobile_storage))}

    def _common_fields(self, unique_fields):
        return (self._list_box(self.model_id) +
                unique_fields +
                self._list_box(self.status) +
                [self.short_delay,
                 self.space,
                 self.short_delay,
                 self.user,
                 self.short_delay,
                 self.enter,
                 self.short_delay,
                 self.tab] +
                [self.short_delay,
                 self.serial])

    def _text_box(self, field_content):
        return [self.short_delay,
                field_content,
                self.tab]

    def _list_box(self, field_content):
        return [self.space,
                self.short_delay,
                field_content,
                self.long_delay,
                self.enter,
                self.long_delay,
                self.tab,
                self.short_delay]

    def instruction_steps(self):
        if self.fieldset == 'New Model':
            return self.fieldsets['New Model']
        else:
            return self._common_fields(self.fieldsets[self.fieldset])
