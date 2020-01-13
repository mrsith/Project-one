from tkinter import *
import tkinter
import tkinter.messagebox
top = Tk()

top.title("Kalkus")

L0 = Label(top, text="Liczydelko",).grid(row=0,column=1)

L1 = Label(top, text="Podaj liczbe 1:",).grid(row=1,column=0)
E1 = Entry(top, bd =3)
E1.grid(row=1,column=1)

L2 = Label(top, text="Podaj liczbe 2:",).grid(row=2,column=0)
E2 = Entry(top, bd=3)
E2.grid(row=2,column=1)

L3 = Label(top, text="Wynik:",).grid(row=3,column=0)
E3 = Entry(top, bd=3)
E3.grid(row=3,column=1)

def entry1():
        num1 = Entry.get(E1)
        try:
         num1 = float(num1)
        except:
         clear_result()
         Entry.insert(E3, 0, "Nie da rady")
        else:
          return num1

def entry2():
        num2 = Entry.get(E2)
        try:
         num2 = float(num2)
        except:
         clear_result()
         Entry.insert(E3, 0, "Nie da rady")
        else:
          return num2


def clear_result():
    E3.delete(0, END)

def add():
     num1 = entry1()
     num2 = entry2()
     sumadd = num1 + num2
     clear_result()
     Entry.insert(E3,0,sumadd)

def sub():
    num1 = entry1()
    num2 = entry2()
    sumsub=(num1 - num2)
    clear_result()
    Entry.insert(E3,0,sumsub)

def mul():
    num1 = entry1()
    num2 = entry2()
    summul=(num1 * num2)
    clear_result()
    Entry.insert(E3,0,summul)

def div():
    num1 = entry1()
    num2 = entry2()
    try:
     sumdiv=(num1 / num2)
     clear_result()
     Entry.insert(E3,0,sumdiv)
    except:
        clear_result()
        Entry.insert(E3,0,"ERROR!")


B1 = Button(top, text="+", command=add, height=1, width=3).grid(row=4, column=1, sticky=W)
B2 = Button(top, text ="-", command=sub, height = 1, width = 3).grid(row=4,column=1,)
B3 = Button(top, text ="*", command=mul, height = 1, width = 3).grid(row=5,column=1, sticky =W)
B4 = Button(top, text ="/", command=div, height = 1, width = 3).grid(row=5,column=1,)


top.mainloop()