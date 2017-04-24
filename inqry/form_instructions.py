import re


class FormInstructions:
    def __init__(self, specs, user=None):
        self.delay = '~d'
        self.tab = '~t'
        self.enter = '~e'
        self.space = '\x20'
        self.status = 'Deploy'
        self.model = specs.model
        self.processor = "{} {}".format(specs.cpu_speed, specs.cpu_name)
        self.memory = specs.memory
        self.drive1 = specs.drive1
        self.drive2 = specs.drive2
        self.drive3 = specs.drive3
        self.drive4 = specs.drive4
        self.serial = specs.serial
        self.user = user or ""
        self.fieldsets = {'Desktop': (self._text_box(self.processor) + self._text_box(self.memory) +
                                      self._text_box(self.drive1) + self._text_box(self.drive2) +
                                      self._text_box(self.drive3) + self._text_box(self.drive4)),
                          'Portable': (self._text_box(self.processor) + self._text_box(self.memory) +
                                       self._text_box(self.drive1))}
        self.os = specs.os_type

    def identify_model(self):
        return self._identify_mac_model() if self.os == 'Darwin' else self._identify_pc_model()

    def _identify_mac_model(self):
        mac_portable_pattern = re.compile(r'MacBook(Pro|Air|)([0-9]|[1-9][0-9]),[1-9]')
        return 'Portable' if re.match(mac_portable_pattern, self.model) else 'Desktop'

    def _identify_pc_model(self):
        pc_portable_pattern = re.compile(r'')
        return 'Portable' if re.match(pc_portable_pattern, self.model) else 'Desktop'

    def _common_fields(self, unique_fields):
        return (self._list_box(self.model) + unique_fields + self._list_box(self.status) +
                self._list_box(self.user) + [self.delay, self.serial])

    def _text_box(self, field):
        return [self.delay, field, self.tab]

    def _list_box(self, field):
        return [self.space, self.delay, field, self.delay, self.enter, self.delay, self.tab]

    def instruction_steps(self):
        return self._common_fields(self.fieldsets[self.identify_model()])
