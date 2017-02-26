import tkinter as tk
from inqry.qr_builder import AssetQRCode
from inqry import systemspecs

win = tk.Tk()
win.title("InQRy")


def click():
    asset = AssetQRCode(systemspecs.mac_os())
    asset.build()


action = tk.Button(win, text="Generate QR Code", command=click)
action.grid(column=1, row=0)

win.mainloop()
