import tkinter as tk
from os import path, name
import requests
from FactoringToolbox import *

# if os == "windows":
#     if path.exists("c:\Python\py.ico"):
#         pass
#     else:
#         url = "https://drive.google.com/uc?export=download&id=1QJN6bN3aH3vt6NDAtAWZmG4KStBep12z"
#         r = requests.get(url, allow_redirects=True)
#         open("c:\Python\py.ico", "wb").write(r.content)


root= tk.Tk()
root.title("Trinomial Factoring and Graphing Toolbox")
# if os.name == windows:
#     root.iconbitmap(r"c:\Python\py.ico")

screen = tk.Canvas(root, width = 400, height = 300)
screen.pack()


label1 = tk.Label(root, text="Trinomial Factoring and Graphing Toolbox")
label1.config(font=("helvetica", 14))
screen.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Enter your Trinomial:")
label2.config(font=("helvetica", 10))
screen.create_window(200, 100, window=label2)

trinomialEntry = tk.Entry (root)
screen.create_window(200, 140, window=trinomialEntry)



def output():

    erase = tk.Label(root,text="                                                                                ")
    screen.create_window(200,170,window=erase)
    x = trinomialEntry.get()
    output = factor(x)
    label3 = tk.Label(root,text=output)
    screen.create_window(200,170,window=label3)

button = tk.Button(text = "Enter", bg = "white", fg = "brown",font = ("helvetica", 9, "bold"), command = output)
screen.create_window(200,200, window=button)










root.mainloop()
