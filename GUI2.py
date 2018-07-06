#Q1
from tkinter import *
root = Tk()
root.title('My App')
frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack( side = RIGHT, fill = Y )
list = Listbox(frame, yscrollcommand = scrollbar.set )
dict={"abc":6039284100,"xyz":7895443030,"amit":7394059384,"rahul":777777381,"sumit":9847563210,\
      "rohan":89293743210,"wxy":99998889789,"sohan":8907897689,"ttt":90876675,"zzz":9411343434 }
for item in dict:
    list.insert(END,"Key Is : " + str(item))
    list.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = list.yview )
mainloop()

#Q2
from tkinter import *
dict={"abc":6039284100,"xyz":7895443030,"amit":7394059384,"rahul":777777381,"sumit":9847563210,\
      "rohan":89293743210,"wxy":99998889789,"sohan":8907897689,"ttt":90876675,"zzz":9411343434 }
root = Tk()
root.title('My App')
def fun():
    k = e1.get()
    v = e2.get()
    dict[k]=v
    lbl3.configure(text=k)
    lbl4.configure(text=v)
    print(dict)
lbl1 = Label(root, text='Key')
lbl1.grid(row=0, column=0)
lbl2 = Label(root, text='Value')
lbl2.grid(row=1, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)
add = Button(root, text='ADD', command=fun)
add.grid(row=2, column=1)
lbl3 = Label(root)
lbl3.grid(row=3, column=0)
lbl4 = Label(root)
lbl4.grid(row=3, column=1)
root.mainloop()