class Instructions:
    """Create Instructions object"""

    def __init__(self, specs):
        self.specs = specs

    def instruction_steps(self):
        delay = 'delay500ms'
        space = '\x20'
        tab = '\x09'
        select = 'enter_key'
        status = 'Ready to Deploy'
        user = 'jazava'
        assettag = '64655638'
        model = self.specs.model
        processor = "{} {}".format(self.specs.cpu_speed, self.specs.cpu_name)
        memory = self.specs.memory
        drive1 = self.specs.drive1
        drive2 = self.specs.drive2
        drive3 = self.specs.drive3
        drive4 = self.specs.drive4
        serial = self.specs.serial

        assettag_instructions = [assettag, tab]
        model_instructions = [space, delay, model, delay, select, delay, tab]
        processor_instructions = [processor, tab]
        memory_instructions = [memory, tab]
        drive_instructions = [drive1, tab, drive2, tab, drive3, tab, drive4, tab]

        common_instructions = assettag_instructions + model_instructions
        spec_instructions = processor_instructions + memory_instructions + drive_instructions
        status_instructions = [space, delay, status, delay, select, delay, tab]
        user_instructions = [space, delay, user, delay, select, delay, tab]
        serial_instructions = [serial, tab]

        return common_instructions + spec_instructions + status_instructions + user_instructions + serial_instructions
