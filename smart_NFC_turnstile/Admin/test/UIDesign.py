
import tkinter as tk
from tkinter import ttk


def CurrentChoice(listbox):
    print(listbox.curselection())

app = tk.Tk() 
app.geometry('350x300')

label = tk.Label(app, text = "NFC admin tool", font=14)
label.grid(column=0, row=0)

options = ["January", "February", "March", "April"]

listbox = tk.Listbox(app, font=12, height=12)

for i in options:
    listbox.insert('end', i)

listbox.grid(column=0, row=1, rowspan=10, padx=20)

frame = tk.Frame()
frame.grid(column=1, row=1)

button = tk.Button(frame, text="current choice", width=15, command=lambda:CurrentChoice(listbox))
button.grid(column=1, row=1)
button = tk.Button(frame, text="refresh", width=15, command=lambda:CurrentChoice(listbox))
button.grid(column=1, row=2)
button = tk.Button(frame, text="close", width=15, command=lambda:CurrentChoice(listbox))
button.grid(column=1, row=3)

# print(comboExample.current(), comboExample.get())

app.mainloop()

# import tkinter as tk


# window = tk.Tk()
# window.geometry("300x230")

# OptionList = [
# "Aries",
# "Taurus",
# "Gemini",
# "Cancer"
# ] 

# variable = tk.StringVar(window)
# variable.set(OptionList[0])

# opt = tk.OptionMenu(window, variable, *OptionList)
# opt.config(width=90, font=('Helvetica', 12))
# opt.pack()
# # self.host1 = tk.Label(text="Host #1")
# # self.host1.pack(pady=5)

# # self.T1 = tk.Text(height=1.4, width=20, font=10, pady=5)
# # self.T1.pack()

# # self.button1 = tk.Button(text="Add host", command=lambda:Indicator.add_host1(indicator, self.T1.get("1.0", "end").replace("\n","")))
# # self.button1.pack(pady=5)

# # self.host2 = tk.Label(text="Host #2")
# # self.host2.pack(pady=5)

# # self.T2 = tk.Text(height=1.4, width=20, font=10, pady=5)
# # self.T2.pack()

# # self.button2 = tk.Button(text="Add host", command=lambda:Indicator.add_host2(indicator,self.T2.get("1.0", "end").replace("\n","")))
# # self.button2.pack(pady=5)

# # window.mainloop()

