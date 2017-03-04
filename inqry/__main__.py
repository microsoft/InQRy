import tkinter as tk
from inqry.qr_builder import AssetQRCode
from inqry.system_specs import systemspecs

asset = AssetQRCode(systemspecs.main())
root = tk.Tk()


def get_dimensions_to_center_window():
    pass


def calculate_center_coordinates(screen_dimension, current_dimension):
    return (screen_dimension / 2) - (current_dimension / 2)


def obtain_default_dimensions_for_the_root_gui_object():
    return tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))


def center():  # Not used at this time
    root.update_idletasks()
    size = obtain_default_dimensions_for_the_root_gui_object()
    height = size[0]
    width = size[1]
    x = calculate_center_coordinates(root.winfo_screenwidth(), height)
    y = calculate_center_coordinates(root.winfo_screenheight(), width)
    root.geometry(f'{height}x{width}+{x}+{y}')


def click():
    asset.display()


def main():
    root.title("InQRy")
    button = tk.Button(root, text="Generate QR Code", command=click)
    button.grid(column=1, row=0)
    root.focus_force()
    root.mainloop()


if __name__ == '__main__':
    main()
