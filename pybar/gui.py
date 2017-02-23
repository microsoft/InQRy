import tkinter as tk

win = tk.Tk()
win.title("PyBar")
# tk.Label()(win, text="Label").grid(column=0, row=0)
label = tk.Label(win, text="Hello")
label.grid(column=0, row=0)


def click():
    action.configure()
    label.configure(foreground="red")


action = tk.Button(win, text="Generate QR Code", command=click)
action.grid(column=1, row=0)

win.mainloop()
