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

    v = tk.IntVar()
    generate_qr_button = tk.Button(ROOT, text="Generate QR Code", command=click)
    desktop_radio_button = tk.Radiobutton(ROOT, text="Desktop", variable=v, value=1)
    portable_radio_button = tk.Radiobutton(ROOT, text="Portable", variable=v, value=2)

    alias_entry = tk.Entry(ROOT)
    alias_label = tk.Label(ROOT, text="Alias")

    alias_entry.grid(row=0, column=1)
    alias_label.grid(row=1, column=1)
    desktop_radio_button.grid(row=2, column=1)
    portable_radio_button.grid(row=3, column=1)
    generate_qr_button.grid(row=4, column=1)

    ROOT.focus_force()
    ROOT.mainloop()
