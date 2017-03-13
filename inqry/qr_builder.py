from qrcode import QRCode
from instructions import Instructions


class AssetQRCode(QRCode):
    """An AssetQRCode instance generates and displays a QR code. At the time
    of writing this. The QR code is built only by being passed a list of string
     objects using the add_data() method"""

    def __init__(self, profile):
        self.qr = QRCode()
        super(AssetQRCode, self).__init__()
        self.profile = profile
        self.code = self.build()

    def build(self):
        instructions = Instructions(self.profile.model).instructions()
        for step in instructions:
            self.qr.add_data(step)
        return self.qr

    def display(self):
        return self.qr.make_image().show()
