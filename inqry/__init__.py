import os
import subprocess

from tkinter import *
import qrcode
from inqry.form_instructions import FormInstructions


class InQRyGUI:
    def __init__(self):
        self.root_window = Tk()
        self.root_window.title('InQRy')

        self.form_options = ('Desktop', 'Portable')
        self.form_selection = StringVar()
        self.form_selection.set(self.form_options[0])
        self.form_menu = OptionMenu(self.root_window, self.form_selection, *self.form_options)
        self.form_menu.grid(row=1, column=1)

        self.qrcode_options = ('Asset', 'Model')
        self.qrcode_selection = StringVar()
        self.qrcode_selection.set(self.form_options[0])
        self.qrcode_menu = OptionMenu(self.root_window, self.form_selection, *self.qrcode_options)
        self.qrcode_menu.grid(row=1, column=2)

        self.alias_label = Label(self.root_window, text='Alias:')
        self.alias_label.grid(row=2, column=2, pady=5, sticky=E)

        self.alias_entry = Entry(self.root_window)
        self.alias_entry.grid(row=2, column=1, pady=5)

        self.generate_qr_button = Button(self.root_window, text='Display', command=self.save)
        self.generate_qr_button.grid(row=3, column=1)

        self.generate_qr_button = Button(self.root_window, text='Save to Desktop', command=self.display)
        self.generate_qr_button.grid(row=3, column=2)

        self.form_instructions = FormInstructions()
        self.asset_qr = AssetQRCode()

        print(self.form_selection.get())
        print(self.qrcode_selection.get())

    def save(self):
        name = self.form_instructions.serial_number
        return self.asset_qr.save(name, self.form_instructions.gui_helper(self.qrcode_selection.get(),
                                                                          self.form_selection.get(),
                                                                          self.alias_entry.get()))

    def display(self):
        return self.asset_qr.display(self.form_instructions.gui_helper(self.qrcode_selection.get(),
                                                                       self.form_selection.get(),
                                                                       self.alias_entry.get()))

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
        with open(os.path.join(desktop, '{}.png'.format(file_name)), 'wb') as fp:
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
