class Asset(object):
    """
    Represents the object to be entered into a Snipe-IT inventory database.

    An Asset object is built from a SystemSpecs object and it's
    attributes, which is then used to assemble the QR code.
    """

    def __init__(self, systemspecs):
        """
        Instantiates an Asset object with several attributes,
        all which can be used to build a QR code.
        """
        self.systemprofile = systemspecs
        self.cpu_name = systemspecs.cpu_name
        self.cpu_processors = systemspecs.cpu_processors
        self.cpu_speed = systemspecs.cpu_speed
        self.cpu_cores = systemspecs.cpu_cores
        self.memory = systemspecs.memory
        self.serial = systemspecs.serial
        self.model = systemspecs.model
        self.name = systemspecs.name

    @staticmethod
    def is_valid():
        """TODO"""
        return None
