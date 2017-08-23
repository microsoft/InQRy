import re
import subprocess
import sys
from tkinter import Button, E, Entry, Label, OptionMenu, StringVar, Tk, W, messagebox

from inqry.asset_qrcode import AssetQRCode
from inqry.form_instructions import FormInstructions
from inqry.system_specs.systemspecs import SystemSpecs


class InQRyGUI:  # TODO: Extract GUI attributes to methods
    def __init__(self):
        self.specs = SystemSpecs()
        self.form_instructions = FormInstructions(self.specs)
        self.asset_qr = AssetQRCode()

        self.root_window = Tk()
        self.root_window.title('InQRy')

        self.form_options_label = Label(self.root_window, text='Form Factor:')
        self.form_options_label.grid(row=1, column=1, sticky=E)

        self.form_options = tuple(self.form_instructions.form_types.keys())[0:2]
        self.form_selection = StringVar()
        self.form_selection.set(self.form_options[0])
        self.form_menu = OptionMenu(self.root_window, self.form_selection, *self.form_options)
        self.form_menu.grid(row=1, column=2, sticky=W)

        self.qrcode_options_label = Label(self.root_window, text='QR Code Type:')
        self.qrcode_options_label.grid(row=2, column=1, sticky=E)

        self.qrcode_options = ['Create Asset']
        self.qrcode_selection = StringVar()
        self.qrcode_selection.set(self.qrcode_options[0])
        self.qrcode_menu = OptionMenu(self.root_window, self.qrcode_selection, *self.qrcode_options)
        self.qrcode_menu.grid(row=2, column=2, sticky=W)

        self.alias_label = Label(self.root_window, text='Alias:')
        self.alias_label.grid(row=3, column=1, sticky=E)

        self.alias_entry = Entry(self.root_window)
        self.alias_entry.grid(row=3, column=2)

        self.asset_tag_label = Label(self.root_window, text='Asset Tag:')
        self.asset_tag_label.grid(row=4, column=1, sticky=E)

        self.asset_tag_entry = Entry(self.root_window)
        self.asset_tag_entry.grid(row=4, column=2)

        self.generate_qr_button = Button(self.root_window, text='Show QR Code', command=self.display)
        self.generate_qr_button.grid(row=5, column=1)

        self.generate_qr_button = Button(self.root_window, text='Save QR Code to Desktop', command=self.save)
        self.generate_qr_button.grid(row=5, column=2)

    def save(self):
        data = self.gather_user_input()
        filename = data[2] + '-' + data[1]
        try:
            return self.asset_qr.save(filename, self.form_instructions.gui_helper(*data))
        except TypeError:
            print('Improper formatting.')
        except FileExistsError:
            error_message_box('File already exists.')

    def display(self):
        data = self.gather_user_input()
        return self.asset_qr.display(self.form_instructions.gui_helper(*data))

    def gather_user_input(self) -> tuple:
        return self.qrcode_selection.get(), self.get_asset_tag(), self.get_alias(), self.form_selection.get()

    def validate(self, contents, field):
        patterns = {'Alias': re.compile(r'^(v\-)?[A-Za-z]+$'),
                    'Asset Tag': re.compile(r'^E?\d{7}$')}
        return contents if bool(re.match(patterns[field], contents)) else error_message_box(
                '{} is not properly formatted.'.format(field))

    def get_alias(self):
        return self.validate(self.alias_entry.get(), 'Alias')

    def get_asset_tag(self):
        return self.validate(self.asset_tag_entry.get(), 'Asset Tag')

    def obtain_default_dimensions_for_the_root_gui_object(self):
        return tuple(int(_) for _ in self.root_window.geometry().split('+')[0].split('x'))

    def calculate_center_coordinates(self, screen_dimension, current_dimension):
        return (screen_dimension // 2) - (current_dimension // 2)

    def center(self):
        self.root_window.update_idletasks()
        size = self.obtain_default_dimensions_for_the_root_gui_object()
        height = size[0]
        width = size[1]

        x = self.calculate_center_coordinates(self.root_window.winfo_screenwidth(), height)
        y = self.calculate_center_coordinates(self.root_window.winfo_screenheight(), width)
        self.root_window.geometry('{}x{}+{}+{}'.format(height, width, x, y))


def error_message_box(message: str):
    messagebox.showerror('Oops!', message)


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
