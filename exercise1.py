from tkinter import *
def finish():
    sys.exit(0)
def show():
    n1 =e1.get()
    n2 = e2.get()
    name="division not possible"
    try:
        n3=float(n1)/float(n2)
    except ValueError:
        e3.config(fg = "red")
        e3.delete(0, END)
        e3.insert(0, name)
    except ZeroDivisionError:
        e3.delete(0, END)
        e3.config(fg="blue")
        e3.insert(0, "Denominator is 0")
    else:
        e3.delete(0, END)
        e3.insert(0, n3)


root=Tk()

l1=Label(root, text="First number")
l2=Label(root, text="second name")
l3=Label(root, text="Division")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root, text='show', command=show)
b2=Button(root, text='Quit', command=finish)
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
l3.grid(row=2, column=0, columnspan=2, sticky=W)
b1.grid(row=3, column=0, sticky=W, pady=4)
b2.grid(row=3, column=2, sticky=W, pady=4)
root.mainloop()