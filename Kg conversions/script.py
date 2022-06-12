from tkinter import *

window = Tk()


def convert():
    kg = float(x.get())
    pounds = kg * 2.22
    grams = kg *1000
    ounces = kg *35.27
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

b1 = Button(window, text="Execute", command = convert)
b1.grid(row = 0, column = 2)

l1 = Label(window, text = "kg")
l1.grid(row=0, column=0)
x = StringVar()
e1 = Entry(window, textvariable=x)
e1.grid(row=0,column=1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row=1,column=0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row=1,column=1)

t3 = Text(window,height = 1, width = 20)
t3.grid(row=1,column=2)

window.mainloop()
