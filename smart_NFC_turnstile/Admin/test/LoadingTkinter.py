# import tkinter as tk
# from time import sleep

# def task():
#     # The window will stay open until this function call ends.
#     sleep(2) # Replace this with the code you want to run
#     root.destroy()

# root = tk.Tk()
# root.title("Example")

# label = tk.Label(root, text="Waiting for task to finish.")
# label.pack()

# root.after(200, task)
# root.mainloop()

# print("Main loop is now over and we can do other stuff.")

import tkinter as tk
import time

class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")

        ## required to make window show before the program gets to the mainloop
        self.update()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # remove the window from the screen without closing it
        # self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        ## simulate a delay while loading
        time.sleep(6)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()