import os
import subprocess

from tkinter import *
import qrcode
from inqry.form_instructions import FormInstructions


def devices_are_attached():
    try:
        return subprocess.check_output(['/usr/local/bin/cfgutil', 'list'])
    except FileNotFoundError:
        print('No such file or directory: "/usr/local/bin/cfgutil"')
        return False


def mobile_capability():
    return 'active' if devices_are_attached() else 'disabled'


class InQRyGUI:
    def __init__(self):
        super().__init__()
        self.root_window = Tk()
        self.root_window.title('InQRy')
        self.form_factor = StringVar()
        self.new_model_selected = IntVar()
        self.alias_entry = Entry(self.root_window)
        self.alias_entry.grid(row=1, column=1, pady=5)
        self.mobile_capability = mobile_capability()
        self.create_widgets()

    def click(self):
        pass

    def create_widgets(self):
        generate_qr_button = Button(self.root_window, text='Generate QR Code', command=self.click)
        generate_qr_button.grid(row=6, columnspan=2, pady=15)

        desktop_radio_button = Radiobutton(
            self.root_window, text='Desktop', variable=self.form_factor, value='Desktop')
        desktop_radio_button.select()
        desktop_radio_button.grid(row=2, columnspan=2)

        portable_radio_button = Radiobutton(
            self.root_window, text='Portable', variable=self.form_factor, value='Portable')
        portable_radio_button.deselect()
        portable_radio_button.grid(row=3, columnspan=2)

        portable_radio_button = Radiobutton(
            self.root_window, text='Mobile', variable=self.form_factor, value='Mobile', state=self.mobile_capability)
        portable_radio_button.deselect()
        portable_radio_button.grid(row=4, columnspan=2)

        alias_label = Label(self.root_window, text='Alias:')
        alias_label.grid(row=1, column=0, pady=5, sticky=E)

        new_model_checkbutton = Checkbutton(
            self.root_window, text='New Model', variable=self.new_model_selected)
        new_model_checkbutton.deselect()
        new_model_checkbutton.grid(row=0, columnspan=2)


class AssetQRCode(FormInstructions, qrcode.QRCode):
    def __init__(self):
        super().__init__()
        self.asset_data = self.new_asset()
        self.new_model_data = self.new_model()

    def make_new_asset_qr(self) -> qrcode.image:
        self.add_data(self.asset_data)
        return self.make_image()

    def make_new_model_qr(self) -> qrcode.image:
        self.add_data(self.new_model_data)
        return self.make_image()

    def save(self, file_name):
        home = os.path.expanduser('~')
        with open(os.path.join(home, f'{file_name}.png'), 'wb') as fp:
            return self.make_new_asset_qr().save(fp)

    def display(self):
        self.make_new_asset_qr().show()


if __name__ == '__main__':
    gui = InQRyGUI()
    gui.root_window.mainloop()
