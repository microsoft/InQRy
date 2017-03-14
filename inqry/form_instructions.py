class Instructions:
    """Create Instructions object"""

    def __init__(self, specs):
        self.specs = specs
        self.delay = 'delay500ms'
        self.space = '\x20'
        self.tab = '\x09'
        self.select = 'enter_key'
        self.status = 'Ready to Deploy'
        self.model = self.specs.model
        self.processor = "{} {}".format(self.specs.cpu_speed, self.specs.cpu_name)
        self.memory = self.specs.memory
        self.drive1 = self.specs.drive1
        self.drive2 = self.specs.drive2
        self.drive3 = self.specs.drive3
        self.drive4 = self.specs.drive4
        self.serial = self.specs.serial
        self.user = 'jazava'
        self.assettag = '64655638'

    def _text_box(self, field):
        return [field, self.tab]

    def _list_box(self, field):
        return [self.space, self.delay, field, self.delay, self.select, self.delay, self.tab]

    def instruction_steps(self):
        return (self._text_box(self.assettag) +
                self._list_box(self.model) +
                self._text_box(self.processor) +
                self._text_box(self.memory) +
                self._text_box(self.drive1) +
                self._text_box(self.drive2) +
                self._text_box(self.drive3) +
                self._text_box(self.drive4) +
                self._list_box(self.status) +
                self._list_box(self.user) +
                self._text_box(self.serial)
                )
