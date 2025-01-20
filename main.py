import tkinter as tk
from tkinter import *

def golden_number () :
    Number = entry.get()
    a = 1
    b = 1
    v = 1

    for i in range(1, int(Number)+1) :
        c = a+b
        a=b
        b=c
        v=b/a
        print(b, a)
        print("V", i, "=", round(v, 5))
        results = "V" + str(i) + " = " + str(round(v, 5)) + "\n"

        text.insert('1.0', results)






root = tk.Tk()

# Setting some window properties
root.title("Tk Example")
root.configure(background="white")

text_gui = Label( root, text = "Entrez valeur" )
text_gui.pack( side = LEFT )
entry = Entry( root, bd = 5 )
entry.pack( side = RIGHT )

button= Button(root, text="Enter", command=golden_number)
button.pack()

text = Text(root, state='disabled', width=44, height=5)
text.configure(state='normal')
text.pack()

root.mainloop()