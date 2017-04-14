import tkinter as tk
from inqry.qr_builder import AssetQRCode
from inqry.system_specs import systemspecs
from inqry.form_instructions import Instructions

ROOT = tk.Tk()


def calculate_center_coordinates(screen_dimension, current_dimension):
    return (screen_dimension / 2) - (current_dimension / 2)


def obtain_default_dimensions_for_the_root_gui_object():
    return tuple(int(_) for _ in ROOT.geometry().split('+')[0].split('x'))


def click():
    data = Instructions(systemspecs.main(), alias_entry.get())
    AssetQRCode(data).display()


if __name__ == '__main__':
    ROOT.title("InQRy")
    generate_qr_button = tk.Button(ROOT, text="Generate QR Code", command=click)
    generate_qr_button.grid(row=1, column=1)
    tk.Label(ROOT, text="Alias").grid(row=0)
    alias_entry = tk.Entry(ROOT)
    alias_entry.grid(row=0, column=1)
    ROOT.focus_force()
    ROOT.mainloop()
