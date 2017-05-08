import tkinter as tk
from inqry.asset_qrcode import AssetQRCode
from inqry.system_specs import systemspecs
from inqry.form_instructions import FormInstructions

ROOT = tk.Tk()


def calculate_center_coordinates(screen_dimension, current_dimension):
    return (screen_dimension / 2) - (current_dimension / 2)


def obtain_default_dimensions_for_the_root_gui_object():
    return tuple(int(_) for _ in ROOT.geometry().split('+')[0].split('x'))


def click():
    data = FormInstructions(systemspecs.SystemSpecs(), alias_entry.get())
    AssetQRCode(data).display()


if __name__ == '__main__':

    ROOT.title("InQRy")

    form_factor = tk.IntVar()
    generate_qr_button = tk.Button(ROOT, text="Generate QR Code", command=click)
    desktop_radio_button = tk.Radiobutton(ROOT, text="Desktop", variable=form_factor, value=1)
    portable_radio_button = tk.Radiobutton(ROOT, text="Portable", variable=form_factor, value=2)

    alias_label = tk.Label(ROOT, text="Alias:")
    alias_entry = tk.Entry(ROOT)

    alias_label.grid(row=0, column=0, pady=5, sticky=tk.E)
    alias_entry.grid(row=0, column=1, pady=5)
    desktop_radio_button.grid(row=1, columnspan=2)
    portable_radio_button.grid(row=2, columnspan=2)
    generate_qr_button.grid(row=5, columnspan=2, pady=25)

    ROOT.focus_force()
    ROOT.mainloop()
