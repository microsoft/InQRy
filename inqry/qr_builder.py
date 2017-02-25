from qrcode import QRCode


class AssetQRCode(QRCode):
    """TODO"""

    def __init__(self, profile):
        self.qr = QRCode()
        super(AssetQRCode, self).__init__()
        self.profile = profile

    def build_serial(self):
        self.qr.add_data(self.profile.serial)
        return self.qr.make_image().show()

    def build_more(self):
        for prop in self.profile:
            self.qr.add_data(prop)
            return self.qr
        return self.qr.make_image.show()
