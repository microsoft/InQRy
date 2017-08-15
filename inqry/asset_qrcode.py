import os

import qrcode

from inqry import gui


class AssetQRCode(qrcode.QRCode):
    def __init__(self):
        super().__init__()

    def make_new_asset_qr(self, data) -> qrcode.image:
        self.clear()
        self.add_data(data)
        return self.make_image()

    def make_new_model_qr(self, data) -> qrcode.image:
        self.clear()
        self.add_data(data)
        return self.make_image()

    def save(self, file_name, data):
        desktop = os.path.expanduser('~/Desktop')
        qrcode_png = os.path.join(desktop, '{}.png'.format(file_name))
        self.prevent_duplicate_file(qrcode_png)
        with open(qrcode_png, 'wb') as fp:
            return self.make_new_asset_qr(data).save(fp)

    def display(self, data):
        img = self.make_new_asset_qr(data)
        img.show()

    def prevent_duplicate_file(self, file):
        if os.path.exists(file):
            gui.error_message_box('QR code already exists.')
