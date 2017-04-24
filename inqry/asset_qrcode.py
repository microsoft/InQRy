import qrcode


class AssetQRCode(qrcode.QRCode):
    """An AssetQRCode instance generates and displays a QR code. At the time
    of writing this. The QR code is built only by being passed a list of string
     objects using the add_data() method"""

    def __init__(self, instructions):
        self.qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        super(AssetQRCode, self).__init__()
        self.build(instructions)

    def build(self, instructions):
        for step in instructions.instruction_steps():
            self.qr.add_data(step)
        return self.qr

    def display(self):
        return self.qr.make_image().show()
