from tkinter import *

fields = ('Number 1', 'Number 2')


def add(entries):
    num1 = (float(entries['Number 1'].get()))
    num2 = (float(entries['Number 2'].get()))
    add = num1 + num2
    print("Add:", float(add))
    listbox.insert(END, add)


def subtract(entries):
    num1 = (float(entries['Number 1'].get()))
    num2 = (float(entries['Number 2'].get()))
    sub = num1 - num2
    print("Subtract:", float(sub))
    listbox.insert(END, sub)


def multiply(entries):
    num1 = (float(entries['Number 1'].get()))
    num2 = (float(entries['Number 2'].get()))
    mult = num1 * num2
    print("Multiply:", float(mult))
    listbox.insert(END, mult)


def divide(entries):
    num1 = (float(entries['Number 1'].get()))
    num2 = (float(entries['Number 2'].get()))
    div = num1 / num2
    print("Divide:", float(div))
    listbox.insert(END, div)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    b1 = Button(root, text='Add',
                command=(lambda e=ents: add(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Subtract',
                command=(lambda e=ents: subtract(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Multiply',
                command=(lambda e=ents: multiply(e)))
    b3.pack(side=LEFT, padx=5, pady=5)
    b4 = Button(root, text='Divide',
                command=(lambda e=ents: divide(e)))
    b4.pack(side=LEFT, padx=5, pady=5)
    b5 = Button(root, text='Quit', command=root.quit)
    b5.pack(side=LEFT, padx=5, pady=5)
    listbox = Listbox(root)
    listbox.pack()

    root.mainloop()
