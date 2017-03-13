class Instructions:
    """Create Instructions object"""

    def __init__(self, specs):
        self.specs = specs

    def instructions(self):
        delay = 'delay500ms'
        space = '\x20'
        tab = '\x09'
        select = 'enter_key'
        status = 'Ready to Deploy'
        user = 'maclab'
        assettag = '64655638'
        model = self.specs.model

        assettag_instructions = [assettag, tab]
        model_instructions = [space, delay, model, delay, select, delay, tab]

        # processor_instructions = [processor, tab]
        # memory_instructions = [memory, tab]
        # drive1_instructions = [drive1, tab]
        # drive2_instructions = [drive2, tab]
        # drive3_instructions = [drive3, tab]
        # drive4_instructions = [drive4, tab]

        instructions = assettag_instructions + model_instructions
        # self.qr.add_data(assetnum) #asset field content
        # self.qr.add_data(tab) #tab out of asset field
        # self.qr.add_data(space, delay, model, delay, select, delay, tab) #initialize model dropdown
        # self.qr.add_data(delay) #wait for model dropdown to populate
        # self.qr.add_data(self.profile.model) #model field content
        # self.qr.add_data(delay) #wait for dropdown to match model
        # self.qr.add_data(select) #select model match from dropdown
        # self.qr.add_data(delay) #wait for match to be set
        # self.qr.add_data(tab) #tab out of model field
        # self.qr.add_data("{} {}".format(self.profile.cpu_speed, self.profile.cpu_name)) #processor field content
        # self.qr.add_data('\x09') #tab out of processor field
        # self.qr.add_data(self.profile.memory) #memory field content
        # self.qr.add_data('\x09') #tab out of memory field
        # self.qr.add_data(self.profile.drive1_model)
        # self.qr.add_data('\x09')
        # self.qr.add_data(self.profile.drive2_model)
        # self.qr.add_data('\x09')
        # self.qr.add_data(self.profile.drive3_model)
        # self.qr.add_data('\x09')
        # self.qr.add_data(self.profile.drive4_model)
        # self.qr.add_data('\x09')
        # self.qr.add_data('delay500ms')
        # self.qr.add_data('\x20')
        # self.qr.add_data('delay500ms')
        # self.qr.add_data('Ready to Deploy')
        # self.qr.add_data('enter_key')
        # self.qr.add_data('delay500ms')
        # self.qr.add_data('\x09')
        # self.qr.add_data('\x09')
        # self.qr.add_data('\x20')
        # self.qr.add_data('delay500ms')
        # self.qr.add_data('maclab')
        # self.qr.add_data('enter_key')
        # self.qr.add_data('\x09')
        # self.qr.add_data('\x09')
        # self.qr.add_data(self.profile.serial)
        # self.qr.add_data('\x09')
        # self.qr.add_data(self.profile.name)
        # self.qr.add_data('enter_key')
        return instructions
