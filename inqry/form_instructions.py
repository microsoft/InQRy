class Instructions:
    def __init__(self, specs, user):
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
        self.user = user
        self.model_definitions = {"MacBookPro13,3": "Portable",
                                  "MacBookPro13,2": "Portable",
                                  "MacBookPro13,1": "Portable",
                                  "MacBookPro11,5": "Portable",
                                  "MacBookPro11,4": "Portable",
                                  "MacBookPro12,1": "Portable",
                                  "MacBookPro11,3": "Portable",
                                  "MacBookPro11,2": "Portable",
                                  "MacBookPro11,1": "Portable",
                                  "MacBookPro10,1": "Portable",
                                  "MacBookPro10,2": "Portable",
                                  "MacBookPro9,1": "Portable",
                                  "MacBookPro9,2": "Portable",
                                  "MacBookPro8,3": "Portable",
                                  "MacBookPro8,2": "Portable",
                                  "MacBookPro8,1": "Portable",
                                  "MacBookPro6,1": "Portable",
                                  "MacBookPro6,2": "Portable",
                                  "MacBookPro7,1": "Portable",
                                  "MacBookPro5,2": "Portable",
                                  "MacBookPro5,4": "Portable",
                                  "MacBookPro5,5": "Portable",
                                  "MacBookPro5,1": "Portable",
                                  "MacBookAir7,2": "Portable",
                                  "MacBookAir7,1": "Portable",
                                  "MacBookAir6,2": "Portable",
                                  "MacBookAir6,1": "Portable",
                                  "MacBookAir5,2": "Portable",
                                  "MacBookAir5,1": "Portable",
                                  "MacBookAir4,2": "Portable",
                                  "MacBookAir4,1": "Portable",
                                  "MacBookAir3,2": "Portable",
                                  "MacBookAir3,1": "Portable",
                                  "MacBook9,1": "Portable",
                                  "MacBook8,1": "Portable",
                                  "MacBook7,1": "Portable",
                                  "MacBook6,1": "Portable",
                                  "Macmini7,1": "Desktop",
                                  "Macmini6,2": "Desktop",
                                  "Macmini6,1": "Desktop",
                                  "Macmini5,3": "Desktop",
                                  "Macmini5,2": "Desktop",
                                  "Macmini5,1": "Desktop",
                                  "Macmini4,1": "Desktop",
                                  "Macmini3,1": "Desktop",
                                  "Macmini2,1": "Desktop",
                                  "MacPro6,1": "Desktop",
                                  "MacPro5,1": "Desktop",
                                  "MacPro4,1": "Desktop",
                                  "MacPro3,1": "Desktop",
                                  "MacPro2,1": "Desktop",
                                  "MacPro1,1": "Desktop",
                                  "iMac17,1": "Desktop",
                                  "iMac16,2": "Desktop",
                                  "iMac16,1": "Desktop",
                                  "iMac15,1": "Desktop",
                                  "iMac14,4": "Desktop",
                                  "iMac14,2": "Desktop",
                                  "iMac14,3": "Desktop",
                                  "iMac14,1": "Desktop",
                                  "iMac13,1": "Desktop",
                                  "iMac13,2": "Desktop",
                                  "iMac12,1": "Desktop",
                                  "iMac12,2": "Desktop",
                                  "iMac11,3": "Desktop",
                                  "iMac11,2": "Desktop",
                                  "iMac10,1": "Desktop",
                                  "iMac9,1": "Desktop",
                                  "iMac8,1": "Desktop"
                                  }

        self.fieldsets = {"Desktop": (self._text_box(self.processor) +
                                      self._text_box(self.memory) +
                                      self._text_box(self.drive1) +
                                      self._text_box(self.drive2) +
                                      self._text_box(self.drive3) +
                                      self._text_box(self.drive4)
                                      ),
                          "Portable": (self._text_box(self.processor) +
                                       self._text_box(self.memory) +
                                       self._text_box(self.drive1)
                                       )}

    def _common_fields(self, unique_fields):
        return (
                self._list_box(self.model) +
                unique_fields +
                self._list_box(self.status) +
                self._list_box(self.user) +
                [self.delay, self.serial]
                )

    def _text_box(self, field):
        return [self.delay, field, self.tab]

    def _list_box(self, field):
        return [self.space, self.delay, field, self.delay, self.enter, self.delay, self.tab]

    def instruction_steps(self):
        return self._common_fields(self.fieldsets[self.model_definitions.get(self.model, 'Desktop')])


def create_instructions_from_system_specs(specs, user):
    return Instructions(specs, user)
