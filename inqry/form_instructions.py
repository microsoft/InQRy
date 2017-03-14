class Instructions:

    def __init__(self, specs, user):
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
        self.user = user
        self.model_definitions = {"MacPro6,1":"Desktop", "MacBookPro13,3":"Desktop"}
        self.fieldsets = {"Desktop": (
                                        self._text_box(self.processor) +
                                        self._text_box(self.memory) +
                                        self._text_box(self.drive1) +
                                        self._text_box(self.drive2) +
                                        self._text_box(self.drive3) +
                                        self._text_box(self.drive4)
                                        ),

                            "Portable": (
                                        self._text_box(self.processor) +
                                        self._text_box(self.memory) +
                                        self._text_box(self.drive1)
                                        )
        }

    def _common_fields(self, unique_fields):
        return (
                self._list_box(self.model) +
                unique_fields +
                self._list_box(self.status) +
                self._list_box(self.user) +
                self._text_box(self.serial)
                )

    def _text_box(self, field):
        return [field, self.tab]

    def _list_box(self, field):
        return [self.space, self.delay, field, self.delay, self.select, self.delay, self.tab]

    def instruction_steps(self):
        return self._common_fields(self.fieldsets[self.model_definitions[self.model]])
