from tkinter import *

window = Tk()  # to create a window


def km_to_miles():
    km = float(x.get())
    y = km/1.609
    t1.insert(END, y)        # end is used to insert at the end of texts


b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)  # to display the button

x = StringVar()
e1 = Entry(window, textvariable=x)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=25)
t1.grid(row=1, column=0, columnspan=2)

window.mainloop()  # so that the window doesn't close off automatically
