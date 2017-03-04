from qrcode import QRCode


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
        attribute_list = self.profile.list_all()
        for attribute in attribute_list:
            self.qr.add_data(attribute)
        return self.qr

    def display(self):
        return self.qr.make_image().show()
