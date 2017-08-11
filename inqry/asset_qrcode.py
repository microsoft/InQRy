import qrcode

from inqry.form_instructions import FormInstructions


class AssetQRCode:
    def __init__(self, instructions: FormInstructions):
        self.instructions = instructions
        self.image = self._make_qrcode_image()

    def _make_qrcode_image(self) -> qrcode.image:
        qr = qrcode.QRCode()
        for instruction in self.instructions.instruction_steps():
            qr.add_data(instruction)
        return qr.make_image()

    def save(self):
        with open('asset.png', 'wb') as fp:
            return self.image.save(fp)

    def display(self):
        self.image.show()
