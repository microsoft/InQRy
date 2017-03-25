import tkinter as tk
from inqry.qr_builder import AssetQRCode
from inqry.system_specs import systemspecs
from inqry.form_instructions import Instructions

ASSET = AssetQRCode(Instructions(systemspecs.main(), "jazava"))
ROOT = tk.Tk()


def get_dimensions_to_center_window():
    pass


def calculate_center_coordinates(screen_dimension, current_dimension):
    return (screen_dimension / 2) - (current_dimension / 2)


def obtain_default_dimensions_for_the_root_gui_object():
    return tuple(int(_) for _ in ROOT.geometry().split('+')[0].split('x'))


# def center():  # Not used at this time
#     ROOT.update_idletasks()
#     size = obtain_default_dimensions_for_the_root_gui_object()
#     height = size[0]
#
#     x = calculate_center_coordinates(ROOT.winfo_screenwidth(), height)
#     y = calculate_center_coordinates(ROOT.winfo_screenheight(), width)
#     ROOT.geometry(f'{height}x{width}+{x}+{y}')


def click():
    ASSET.display()


def main():
    ROOT.title("InQRy")
    button = tk.Button(ROOT, text="Generate QR Code", command=click)
    button.grid(column=1, row=0)
    ROOT.focus_force()
    ROOT.mainloop()


if __name__ == '__main__':
    main()
