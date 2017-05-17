from tkinter import *
import subprocess
from inqry.asset_qrcode import AssetQRCode
from inqry.system_specs.systemspecs import SystemSpecs
from inqry.system_specs import ios_system_profiler
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
        self.root_window = Tk()
        self.root_window.title('InQRy')
        self.form_factor = StringVar()
        self.new_model_selected = IntVar()
        self.alias_entry = Entry(self.root_window)
        self.alias_entry.grid(row=1, column=1, pady=5)
        self.systemspecs = SystemSpecs()
        self.mobile_capability = mobile_capability()
        self.create_widgets()

    def click(self):
        if self.new_model_selected.get():
            form_instructions = FormInstructions(self.systemspecs, 'New Model')
            AssetQRCode(form_instructions).display()
        elif self.form_factor.get() == 'Mobile':
            for devicespecs in ios_system_profiler.get_hardware_overview():
                form_instructions = FormInstructions(devicespecs, self.form_factor.get(), self.alias_entry.get())
                AssetQRCode(form_instructions).display()
        else:
            form_instructions = FormInstructions(self.systemspecs, self.form_factor.get(), self.alias_entry.get())
            AssetQRCode(form_instructions).display()

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


if __name__ == '__main__':
    gui = InQRyGUI()
    gui.root_window.mainloop()
