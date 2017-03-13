from qrcode import QRCode
from form_instructions import Instructions


class AssetQRCode(QRCode):
    """An AssetQRCode instance generates and displays a QR code. At the time
    of writing this. The QR code is built only by being passed a list of string
     objects using the add_data() method"""

    def __init__(self, instructions):
        self.qr = QRCode()
        super(AssetQRCode, self).__init__()
        self.Instructions = instructions
        self.code = self.build()

    def build(self):
        instructions = self.Instructions.instruction_steps()
        for step in instructions:
            self.qr.add_data(step)
        return self.qr

    def display(self):
        return self.qr.make_image().show()
