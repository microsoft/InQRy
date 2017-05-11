import tkinter
import subprocess
import sys
from inqry.asset_qrcode import AssetQRCode
from inqry.system_specs import systemspecs
from inqry.form_instructions import FormInstructions


def machine_has_cfgutil():
    return subprocess.getstatusoutput(['type', '/usr/local/bin/cfgutil'])


def devices_are_attached():
    return subprocess.check_output(['/usr/local/bin/cfgutil', 'list'])


def operating_system_is_macos():
    return sys.platform == 'darwin'


def mobile_device_capability():
    return 'active' if operating_system_is_macos() and machine_has_cfgutil() and devices_are_attached() else 'disabled'


class InQRyGUI:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.title('InQRy')
        self.form_factor = tkinter.StringVar()
        self.new_model_selected = tkinter.IntVar()
        self.alias_entry = tkinter.Entry(self.root_window)
        self.alias_entry.grid(row=1, column=1, pady=5)
        self.systemspecs = systemspecs.SystemSpecs()
        self.mobile_device_capability = mobile_device_capability()
        self.create_widgets()

    def click(self):
        if self.new_model_selected.get():
            form_instructions = FormInstructions(self.systemspecs, 'New Model')
            AssetQRCode(form_instructions).display()
        else:
            form_instructions = FormInstructions(self.systemspecs, self.form_factor.get(), self.alias_entry.get())
            AssetQRCode(form_instructions).display()

    def create_widgets(self):
        generate_qr_button = tkinter.Button(self.root_window, text='Generate QR Code', command=self.click)
        generate_qr_button.grid(row=6, columnspan=2, pady=15)

        desktop_radio_button = tkinter.Radiobutton(self.root_window, text='Desktop', variable=self.form_factor,
                                                   value='Desktop')
        desktop_radio_button.select()
        desktop_radio_button.grid(row=2, columnspan=2)

        portable_radio_button = tkinter.Radiobutton(self.root_window, text='Portable', variable=self.form_factor,
                                                    value='Portable')
        portable_radio_button.deselect()
        portable_radio_button.grid(row=3, columnspan=2)

        portable_radio_button = tkinter.Radiobutton(self.root_window, text='Mobile', variable=self.form_factor,
                                                    value='Mobile', state=self.mobile_device_capability)
        portable_radio_button.deselect()
        portable_radio_button.grid(row=4, columnspan=2)

        alias_label = tkinter.Label(self.root_window, text='Alias:')
        alias_label.grid(row=1, column=0, pady=5, sticky=tkinter.E)

        new_model_checkbutton = tkinter.Checkbutton(self.root_window, text='New Model',
                                                    variable=self.new_model_selected)
        new_model_checkbutton.deselect()
        new_model_checkbutton.grid(row=0, columnspan=2)


if __name__ == '__main__':
    gui = InQRyGUI()
    gui.root_window.mainloop()
