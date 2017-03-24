class Instructions:

    def __init__(self, specs, user):
        self.delay = 'delay500ms'
        self.space = '\x20'
        self.tab = '\x09'
        self.select = 'enter_key'
        self.status = 'Ready'
        self.model = specs.model
        self.processor = "{} {}".format(specs.cpu_speed, specs.cpu_name)
        self.memory = specs.memory
        self.drive1 = specs.drive1
        self.drive2 = specs.drive2
        self.drive3 = specs.drive3
        self.drive4 = specs.drive4
        self.serial = specs.serial
        self.user = user
        self.model_definitions = {"MacBookPro13,3":"Portable", # MacBook Pro (15-inch, 2016)
                                  "MacBookPro13,2":"Portable", # MacBook Pro (13-inch, 2016, Four Thunderbolt 3 Ports)
                                  "MacBookPro13,1":"Portable", # MacBook Pro (13-inch, 2016, Two Thunderbolt 3 Ports)
                                  "MacBookPro11,5":"Portable", # MacBook Pro (Retina, 15-inch, Mid 2015)
                                  "MacBookPro11,4":"Portable", # MacBook Pro (Retina, 15-inch, Mid 2015)
                                  "MacBookPro12,1":"Portable", # MacBook Pro (Retina, 13-inch, Early 2015)
                                  "MacBookPro11,3":"Portable", # MacBook Pro (Retina, 15-inch, Mid 2014), MacBook Pro (Retina, 15-inch, Late 2013)
                                  "MacBookPro11,2":"Portable", # MacBook Pro (Retina, 15-inch, Mid 2014), MacBook Pro (Retina, 15-inch, Late 2013)
                                  "MacBookPro11,1":"Portable", # MacBook Pro (Retina, 13-inch, Mid 2014), MacBook Pro (Retina, 13-inch, Late 2013)
                                  "MacBookPro10,1":"Portable", # MacBook Pro (Retina, 15-inch, Early 2013), MacBook Pro (Retina, 15-inch, Mid 2012)
                                  "MacBookPro10,2":"Portable", # MacBook Pro (Retina, 13-inch, Early 2013), MacBook Pro (Retina, 13-inch, Late 2012)
                                  "MacBookPro9,1":"Portable", # MacBook Pro (15-inch, Mid 2012)
                                  "MacBookPro9,2":"Portable", # MacBook Pro (13-inch, Mid 2012)
                                  "MacBookPro8,3":"Portable", # MacBook Pro (17-inch, Late 2011), MacBook Pro (17-inch, Early 2011)
                                  "MacBookPro8,2":"Portable", # MacBook Pro (15-inch, Late 2011), MacBook Pro (15-inch, Early 2011)
                                  "MacBookPro8,1":"Portable", # MacBook Pro (13-inch, Late 2011), MacBook Pro (13-inch, Early 2011)
                                  "MacBookPro6,1":"Portable", # MacBook Pro (17-inch, Mid 2010)
                                  "MacBookPro6,2":"Portable", # MacBook Pro (15-inch, Mid 2010)
                                  "MacBookPro7,1":"Portable", # MacBook Pro (13-inch, Mid 2010)
                                  "MacBookPro5,2":"Portable", # MacBook Pro (17-inch, Mid 2009)
                                  "MacBookPro5,3":"Portable", # MacBook Pro (15-inch, Mid 2009)
                                  "MacBookPro5,4":"Portable", # MacBook Pro (15-inch, 2.53 GHz, Mid 2009)
                                  "MacBookPro5,5":"Portable", # MacBook Pro (13-inch, Mid 2009)
                                  "MacBookPro5,2":"Portable", # MacBook Pro (17-inch, Early 2009)
                                  "MacBookPro5,1":"Portable", # MacBook Pro (15-inch, Late 2008)
                                  "MacBookAir7,2":"Portable", # MacBook Air (13-inch, Early 2015)
                                  "MacBookAir7,1":"Portable", # MacBook Air (11-inch, Early 2015)
                                  "MacBookAir6,2":"Portable", # MacBook Air (13-inch, Early 2014), MacBook Air (13-inch, Mid 2013)
                                  "MacBookAir6,1":"Portable", # MacBook Air (11-inch, Early 2014), MacBook Air (11-inch, Mid 2013)
                                  "MacBookAir5,2":"Portable", # MacBook Air (13-inch, Mid 2012)
                                  "MacBookAir5,1":"Portable", # MacBook Air (11-inch, Mid 2012)
                                  "MacBookAir4,2":"Portable", # MacBook Air (13-inch, Mid 2011)
                                  "MacBookAir4,1":"Portable", # MacBook Air (11-inch, Mid 2011)
                                  "MacBookAir3,2":"Portable", # MacBook Air (13-inch, Late 2010)
                                  "MacBookAir3,1":"Portable", # MacBook Air (11-inch, Late 2010)
                                  "MacBook9,1":"Portable", # MacBook (Retina, 12-inch, Early 2016)
                                  "MacBook8,1":"Portable", # MacBook (Retina, 12-inch, Early 2015)
                                  "MacBook7,1":"Portable", # MacBook (13-inch, Mid 2010)
                                  "MacBook6,1":"Portable", # MacBook (13-inch, Late 2009)
                                  "Macmini7,1":"Desktop", # Mac mini (Late 2014)
                                  "Macmini6,2":"Desktop", # Mac mini (Late 2012), Mac mini Server (Late 2012)
                                  "Macmini6,1":"Desktop", # Mac mini (Late 2012)
                                  "Macmini5,3":"Desktop", # Mac mini Server (Mid 2011)
                                  "Macmini5,2":"Desktop", # Mac mini (Mid 2011)
                                  "Macmini5,1":"Desktop", # Mac mini (Mid 2011)
                                  "Macmini4,1":"Desktop", # Mac mini (Mid 2010), Mac mini Server (Mid 2010)
                                  "Macmini3,1":"Desktop", # Mac mini (Late 2009), Mac mini (Early 2009)
                                  "Macmini2,1":"Desktop", # Mac mini (Mid 2007)
                                  "MacPro6,1":"Desktop", # Mac Pro (Late 2013)
                                  "MacPro5,1":"Desktop", # Mac Pro (Mid 2012), Mac Pro (Mid 2010)
                                  "MacPro4,1":"Desktop", # Mac Pro (Early 2009)
                                  "MacPro3,1":"Desktop", # Mac Pro (Early 2008)
                                  "MacPro2,1":"Desktop", # Mac Pro (8-core)
                                  "MacPro1,1":"Desktop", # Mac Pro
                                  "iMac17,1":"Desktop", # iMac (Retina 5K, 27-inch, Late 2015)
                                  "iMac16,2":"Desktop", # iMac (Retina 4K, 21.5-inch, Late 2015), iMac (21.5-inch, Late 2015)
                                  "iMac16,1":"Desktop", # iMac (21.5-inch, Late 2015)
                                  "iMac15,1":"Desktop", # iMac (Retina 5K, 27-inch, Mid 2015), iMac (Retina 5K, 27-inch, Late 2014)
                                  "iMac14,4":"Desktop", # iMac (21.5-inch, Mid 2014)
                                  "iMac14,2":"Desktop", # iMac (27-inch, Late 2013)
                                  "iMac14,3":"Desktop", # iMac (21.5-inch, Late 2013)
                                  "iMac14,1":"Desktop", # iMac (21.5-inch, Late 2013)
                                  "iMac13,1":"Desktop", # iMac (21.5-inch, Early 2013), iMac (21.5-inch, Late 2012)
                                  "iMac13,2":"Desktop", # iMac (27-inch, Late 2012)
                                  "iMac12,1":"Desktop", # iMac (21.5-inch, Late 2011), iMac (21.5-inch, Mid 2011)
                                  "iMac12,2":"Desktop", # iMac (27-inch, Mid 2011)
                                  "iMac11,3":"Desktop", # iMac (27-inch, Mid 2010)
                                  "iMac11,2":"Desktop", # iMac (21.5-inch, Mid 2010)
                                  "iMac10,1":"Desktop", # iMac (27-inch, Late 2009), iMac (21.5-inch, Late 2009)
                                  "iMac9,1":"Desktop", # iMac (20-inch, Early 2009)
                                  "iMac8,1":"Desktop" # iMac (24-inch Early 2008)
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
                self._text_box(self.serial)
                )

    def _text_box(self, field):
        return [field, self.tab]

    def _list_box(self, field):
        return [self.space, self.delay, field, self.delay, self.select, self.delay, self.tab]

    def instruction_steps(self):
        return self._common_fields(self.fieldsets[self.model_definitions].get(self.model, 'Desktop'))

    def create_instructions_from_system_specs(specs, user):
        return Instructions(specs, user)
