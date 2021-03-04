import tkinter as tk
from tkinter import messagebox
import time
import serialReader
from requestHandler import registerCardId




class AuthWindow(tk.Toplevel):
    def __init__(self, parent, selection):
        tk.Toplevel.__init__(self, parent)
        self.title("auth")
        self.geometry('250x250')

        self.selection = selection

        # Username
        self.usernameL = tk.Label(self, text="username: ")
        self.usernameL.pack(pady=5)

        self.usernameT = tk.Text(self, height=1.4, width=20, font=10, pady=5)
        self.usernameT.pack()

        # Password
        self.passwordL = tk.Label(self, text="password: ")
        self.passwordL.pack(pady=5)

        self.passwordE = tk. Entry(self, width=20, font=10, show="*")
        self.passwordE.pack(pady=5)

        # Password button
        self.registerB = tk.Button(self, text="Register the key", command=self.__registerKey)
        self.registerB.pack(pady=5)

        ## required to make window show before the program gets to the mainloop
        self.update()

    def __registerKey(self):
        # TODO call the API with auth info, read from console for the ID
        username = self.usernameT.get("1.0", "end").replace('\n','')
        password = self.passwordE.get()
        keyUID = serialReader.readSerial()
        foo, bar = registerCardId(username, password, self.selection, keyUID)
        if foo == "error":
            messagebox.showerror(foo, bar)
        else:
            messagebox.showinfo(foo, bar)
        


    # def __getAuthId(self):
    #     # TODO multithreading to read the serial input



    #     # _thread.start_new_thread( __sleep, (self,) )
    #     # TODO complete the loading graphics
    #     time.sleep(6)

    #     # TODO send http request to the authen API

    #     # TODO the error handler    

    #     print(self.authId)

