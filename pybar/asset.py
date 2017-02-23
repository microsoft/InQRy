class Asset(object):
    """
    Represents the object to be entered into a Snipe-IT inventory database.

    An Asset object is built from a SystemProfile object and it's
    attributes, which is then used to assemble the QR code.
    """

    def __init__(self, systemprofile):
        """
        Instantiates an Asset object with several attributes,
        all which can be used to build a QR code.
        """
        self.systemprofile = systemprofile
        self.cpu_name = systemprofile.cpu_name
        self.cpu_processors = systemprofile.cpu_processors
        self.cpu_speed = systemprofile.cpu_speed
        self.cpu_cores = systemprofile.cpu_cores
        self.memory = systemprofile.memory
        self.serial = systemprofile.serial
        self.model = systemprofile.model
        self.name = systemprofile.name

    @staticmethod
    def is_valid():
        """TODO"""
        return None
