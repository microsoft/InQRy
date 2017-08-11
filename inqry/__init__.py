import os
import subprocess

from tkinter import *
import qrcode
from inqry.form_instructions import FormInstructions


class InQRyGUI:
    def __init__(self):
        super().__init__()
        self.root_window = Tk()
        self.root_window.title('InQRy')
        self.form_type = StringVar()
        self.new_model_selected = IntVar()
        self.alias = Entry(self.root_window)
        self.alias.grid(row=1, column=1, pady=5)
        self.mobile_capability = mobile_capability()
        self.create_widgets()
        self.form_instructions = FormInstructions(self.form_type.get(), self.alias.get())
        self.asset_qr = AssetQRCode()

    def save(self):
        name = self.form_instructions.serial_number
        return self.asset_qr.save(name, self.form_instructions.new_model())

    def display(self):
        return self.asset_qr.display(self.form_instructions.new_model())

    def create_widgets(self):
        generate_qr_button = Button(self.root_window, text='Display QR Code', command=self.display)
        generate_qr_button.grid(row=6, columnspan=2)

        generate_qr_button = Button(self.root_window, text='Save QR Code to Desktop', command=self.save)
        generate_qr_button.grid(row=7, columnspan=2)

        desktop_radio_button = Radiobutton(
            self.root_window, text='Desktop', variable=self.form_type, value='Desktop')
        desktop_radio_button.select()
        desktop_radio_button.grid(row=2, columnspan=2)

        portable_radio_button = Radiobutton(
            self.root_window, text='Portable', variable=self.form_type, value='Portable')
        portable_radio_button.deselect()
        portable_radio_button.grid(row=3, columnspan=2)

        portable_radio_button = Radiobutton(
            self.root_window, text='Mobile', variable=self.form_type, value='Mobile', state=self.mobile_capability)
        portable_radio_button.deselect()
        portable_radio_button.grid(row=4, columnspan=2)

        alias_label = Label(self.root_window, text='Alias:')
        alias_label.grid(row=1, column=0, pady=5, sticky=E)

        new_model_checkbutton = Checkbutton(
            self.root_window, text='New Model', variable=self.new_model_selected)
        new_model_checkbutton.deselect()
        new_model_checkbutton.grid(row=0, columnspan=2)


class AssetQRCode(qrcode.QRCode):
    def __init__(self):
        super().__init__()

    def make_new_asset_qr(self, data) -> qrcode.image:
        self.add_data(data)
        return self.make_image()

    def make_new_model_qr(self, data) -> qrcode.image:
        self.add_data(data)
        return self.make_image()

    def save(self, file_name, data):
        desktop = os.path.expanduser('~/Desktop')
        with open(os.path.join(desktop, f'{file_name}.png'), 'wb') as fp:
            return self.make_new_asset_qr(data).save(fp)

    def display(self, data):
        img = self.make_new_asset_qr(data)
        img.show()


def devices_are_attached():
    try:
        return subprocess.check_output(['/usr/local/bin/cfgutil', 'list'])
    except FileNotFoundError:
        print('No such file or directory: "/usr/local/bin/cfgutil"')
        return False


def mobile_capability():
    return 'active' if devices_are_attached() else 'disabled'
