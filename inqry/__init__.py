import os
import re
import subprocess

from tkinter import *
from tkinter import messagebox
import qrcode
from inqry.form_instructions import FormInstructions


class InQRyGUI:  # TODO: Extract GUI attributes to methods
    def __init__(self):
        self.form_instructions = FormInstructions()
        self.asset_qr = AssetQRCode()

        self.root_window = Tk()
        self.root_window.title('InQRy')

        self.alias_label = Label(self.root_window, text='Alias:')
        self.alias_label.grid(row=1, column=1, sticky=E)

        self.alias_entry = Entry(self.root_window)
        self.alias_entry.grid(row=1, column=2)

        self.asset_tag_label = Label(self.root_window, text='Asset Tag:')
        self.asset_tag_label.grid(row=2, column=1, sticky=E)

        self.asset_tag_entry = Entry(self.root_window)
        self.asset_tag_entry.grid(row=2, column=2)

        self.form_options = tuple(self.form_instructions.form_types.keys())
        self.form_selection = StringVar()
        self.form_selection.set(self.form_options[0])
        self.form_menu = OptionMenu(self.root_window, self.form_selection, *self.form_options)
        self.form_menu.grid(row=3, column=1)

        self.qrcode_options = ('Asset', 'Model')
        self.qrcode_selection = StringVar()
        self.qrcode_selection.set(self.qrcode_options[0])
        self.qrcode_menu = OptionMenu(self.root_window, self.qrcode_selection, *self.qrcode_options)
        self.qrcode_menu.grid(row=3, column=2)

        self.generate_qr_button = Button(self.root_window, text='Display', command=self.display)
        self.generate_qr_button.grid(row=4, column=1)

        self.generate_qr_button = Button(self.root_window, text='Save to Desktop', command=self.save)
        self.generate_qr_button.grid(row=4, column=2)

    def save(self):
        try:
            file_name = self.valid_alias(self.alias_entry.get()) + '-' + self.valid_asset(self.asset_tag_entry.get())
            data = self.gather_user_input()
            return self.asset_qr.save(file_name, self.form_instructions.gui_helper(*data))
        except TypeError:
            self.missing_value_message()

    def display(self):
        data = self.gather_user_input()
        return self.asset_qr.display(self.form_instructions.gui_helper(*data))

    def gather_user_input(self) -> tuple:
        return (
            self.qrcode_selection.get(), self.asset_tag_entry.get(), self.alias_entry.get(), self.form_selection.get())

    def missing_value_message(self):
        messagebox.showerror('Oops! That isn\'t a valid entry.', 'Missing Value')

    def valid_asset(self, asset_tag: str):  # TODO: Define custom exceptions inside FormInstructions
        pattern = re.compile(r'^E?\d{7}$')
        return asset_tag if bool(re.match(pattern, asset_tag)) else False

    def valid_alias(self, alias: str):  # TODO: Define custom exception inside FormInstructions
        pattern = re.compile(r'^(v\-)?[a-z]+$')
        return alias if bool(re.match(pattern, alias)) else False


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


def mobile_capability():  # TODO: Re-implement mobile_capability() into GUI
    if sys.platform == 'darwin':
        try:
            subprocess.check_output(['/usr/local/bin/cfgutil'])
            return 'active'
        except FileNotFoundError:
            print(
                '''
                No such file or directory: "/usr/local/bin/cfgutil"

                You must install cfgutil using Apple Configurator in order to
                use InQRy with a mobile device.
                ''')
            return 'disable'
    else:
        pass
