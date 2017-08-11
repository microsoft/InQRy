import os
import subprocess

from tkinter import *
import qrcode
from inqry.form_instructions import FormInstructions


class InQRyGUI:
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
        alias = self.alias_entry.get()
        name = self.asset_tag_entry.get()
        file_name = alias + name
        return self.asset_qr.save(file_name, self.form_instructions.gui_helper(self.qrcode_selection.get(),
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
    if sys.platform == 'darwin':
        try:
            return subprocess.check_output(['/usr/local/bin/cfgutil', 'list'])
        except FileNotFoundError:
            print('No such file or directory: "/usr/local/bin/cfgutil"')
            return False
    else:
        pass


def mobile_capability():
    return 'active' if devices_are_attached() else 'disabled'
