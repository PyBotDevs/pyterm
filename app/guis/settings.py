### NKA Development Organization 2022. For enquiries, contact <pybotdevs@outlook.com> ###
# Imports
from tkinter import *
from tkinter import ttk

# Config
colours = [
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "black"
]


# Main Code
def run():
    # Initialize Window
    root = Tk()

    # Window Config
    root.title("PyTerm Settings")
    root.geometry("700x550")
    root.resizable(False, False)

    # GUI Mapping
    label_title = Label(root, text="Settings", font=("Segoe UI", 28, "bold"))
    label_title.place(relx=0.01, rely=0.01, anchor=NW)

    label_host_colour = Label(root, text="Host name display colour:")
    dropdown_host_colour = ttk.Combobox(root, values=colours, state="readonly", width=35)
    label_host_colour.place(relx=0.2, rely=0.2, anchor=W)
    dropdown_host_colour.place(relx=0.8, rely=0.2, anchor=E)
    label_user_colour = Label(root, text="User name display colour:")
    dropdown_user_colour = ttk.Combobox(root, values=colours, state="readonly", width=35)
    label_user_colour.place(relx=0.2, rely=0.3, anchor=W)
    dropdown_user_colour.place(relx=0.8, rely=0.3, anchor=E)

    # Window Functions
    def save():
        root.destroy()

    # Action Buttons
    button_cancel = Button(root, text="Cancel", command=root.destroy)
    button_save = Button(root, text="Save", command=save)
    button_cancel.place(relx=0.86, rely=0.95, anchor=SE)
    button_save.place(relx=0.95, rely=0.95, anchor=SE)

    # Run Built Window
    root.mainloop()
