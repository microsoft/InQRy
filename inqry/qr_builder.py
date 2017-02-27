from qrcode import QRCode


class AssetQRCode(QRCode):
    """TODO"""

    def __init__(self, profile):
        self.qr = QRCode()
        super(AssetQRCode, self).__init__()
        self.profile = profile

    def build(self):
        attribute_list = self.profile.list_all()
        for attribute in attribute_list:
            self.qr.add_data(attribute)
        return self.qr.make_image().show()
