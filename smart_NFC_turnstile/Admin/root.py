import tkinter as tk
from tkinter import messagebox
import time
from requestHandler import *
from authWindow import AuthWindow




class Root(tk.Tk):
    """docstring for root"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Management tool")
        self.geometry('330x390')

        # label for the app
        self.label = tk.Label(self, text = "Pending card(s) to be registered.", font=14)
        self.label.grid(column=0, row=0)

        # listbox
        self.options = nonActivatedAuths()
        self.listbox = tk.Listbox(self, font=12, height=12)
        self.__loadOptions()

        self.listbox.grid(column=0, row=1, rowspan=10, padx=5)

        # frame for buttons
        self.frame = tk.Frame()
        self.frame.grid(column=1, row=1)

        # buttons in the frame
        self.registerButton = tk.Button(self.frame, text="Register", width=15, command=self.__register)
        self.registerButton.grid(column=1, row=1, pady=5)
        self.refreshButton = tk.Button(self.frame, text="Refresh", width=15, command=self.__refresh)
        self.refreshButton.grid(column=1, row=2, pady=5)
        self.closeButton = tk.Button(self.frame, text="Close", width=15, command=self.__close)
        self.closeButton.grid(column=1, row=3, pady=5)


    def __loadOptions(self):
        # load all options to the list box
        for i in self.options:
            self.listbox.insert('end', i)

    def __register(self):
        # TODO new window for authentication, 
        # Collecting the key
        # send http request to the server
        if self.listbox.curselection() == ():
            messagebox.showerror("No selection", "Please select an Auth to procede.")
        else:
            # TODO feeze the window when sending request to server
            selection = self.__selectedId()
            authWindow = AuthWindow(self, selection)
        # time.sleep(4)
        # authWindow.destroy()

    def __selectedId(self):
            # the selection is a int Id of the auth
            selection = self.listbox.get(self.listbox.curselection()).replace("Id: ", "")
            selection = int(selection)
            return selection


        
    def __refresh(self):
        # TODO delete all from the list box, reload 
        self.listbox.delete(0, len(self.options))
        self.options = nonActivatedAuths()
        self.__loadOptions()

    def __close(self):
        self.destroy()

