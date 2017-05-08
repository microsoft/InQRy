import tkinter as tk
from inqry.asset_qrcode import AssetQRCode
from inqry.system_specs import systemspecs
from inqry.form_instructions import FormInstructions


class InQRyGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('InQRy')
        self.form_factor = tk.StringVar()
        self.new_model_selected = tk.StringVar()
        self.alias_entry = tk.Entry(self.win)
        self.alias_entry.grid(row=0, column=1, pady=5)
        self.create_widgets()

    def click(self):
        data = FormInstructions(systemspecs.SystemSpecs(), self.form_factor.get(), self.alias_entry.get())
        AssetQRCode(data).display()

    def create_widgets(self):
        generate_qr_button = tk.Button(self.win, text='Generate QR Code', command=self.click)
        generate_qr_button.grid(row=5, columnspan=2, pady=15)

        desktop_radio_button = tk.Radiobutton(self.win, text='Desktop', variable=self.form_factor, value='Desktop')
        desktop_radio_button.deselect()
        desktop_radio_button.grid(row=1, columnspan=2)

        portable_radio_button = tk.Radiobutton(self.win, text='Portable', variable=self.form_factor, value='Portable')
        portable_radio_button.deselect()
        portable_radio_button.grid(row=2, columnspan=2)

        alias_label = tk.Label(self.win, text='Alias:')
        alias_label.grid(row=0, column=0, pady=5, sticky=tk.E)

        new_model_checkbutton = tk.Checkbutton(self.win, text='New Model', variable=self.new_model_selected)
        new_model_checkbutton.deselect()
        new_model_checkbutton.grid(row=6, columnspan=2)


if __name__ == '__main__':
    main = InQRyGUI()
    main.win.mainloop()
