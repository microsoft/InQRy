import tkinter as tk
from inqry.qr_builder import AssetQRCode
from inqry.system_specs import systemspecs

asset = AssetQRCode(systemspecs.main())
root = tk.Tk()


def center():  # Not used at this time
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))


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
