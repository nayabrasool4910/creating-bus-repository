from tkinter import *
import backadmin

def insert_text():
    backadmin.insert(serviceno_integer.get(),busname_text.get(),source_text.get(),destination_text.get(),depo_text.get(),frequency_text.get(),passallowed_text.get())

def update_text():
    backadmin.update(serviceno_integer.get(),busname_text.get(),source_text.get(),destination_text.get(),depo_text.get(),frequency_text.get(),passallowed_text.get())

def search_text():
    list1.delete(0,END)
    for rows_search in backadmin.search(source_text.get(),destination_text.get()):
        list1.insert(END,rows_search)

def view_text():
    list1.delete(0,END)
    for rows_view in backadmin.view():
        list1.insert(END,rows_view)

def delete_text():
    backadmin.delete(serviceno_text.get())


window=Tk()
window.title("ADMIN ")
window.configure(background="sky blue")


l1=Label(window,text="BUS NAME :",fg="red")
l1.grid(row=0,column=0)

l2=Label(window,text="SERVICE NO :",fg="red")
l2.grid(row=1,column=0)

l3=Label(window,text="SOURCE :",fg="red")
l3.grid(row=2,column=0)

l4=Label(window,text="DESTINATION :",fg="red")
l4.grid(row=3,column=0)

l5=Label(window,text="DEPO :",fg="red")
l5.grid(row=4,column=0)

l6=Label(window,text="FREQUENCY :",fg="red")
l6.grid(row=5,column=0)

l7=Label(window,text="PASS ALLOWED :",fg="red")
l7.grid(row=6,column=0)

busname_text=StringVar()
e1=Entry(window,textvariable=busname_text)
e1.grid(row=0,column=1)

serviceno_text=StringVar()
e2=Entry(window,textvariable=serviceno_text)
e2.grid(row=1,column=1)

source_text=StringVar()
e3=Entry(window,textvariable=source_text)
e3.grid(row=2,column=1)

destination_text=StringVar()
e4=Entry(window,textvariable=destination_text)
e4.grid(row=3,column=1)

depo_text=StringVar()
e5=Entry(window,textvariable=depo_text)
e5.grid(row=4,column=1)

frequency_text=StringVar()
e6=Entry(window,textvariable=frequency_text)
e6.grid(row=5,column=1)

passallowed_text=StringVar()
e7=Entry(window,textvariable=passallowed_text)
e7.grid(row=6,column=1)

b1=Button(window,text="insert",fg="red",command=insert_text)
b1.grid(row=3,column=5)

b2=Button(window,text="  view",fg="red",command=view_text)
b2.grid(row=3,column=6)

b3=Button(window,text="search",fg="red",command=search_text)
b3.grid(row=3,column=7)

b4=Button(window,text="update",fg="red",command=update_text)
b4.grid(row=3,column=8)

b5=Button(window,text="delete",fg="red",command=delete_text)
b5.grid(row=3,column=9)


list1=Listbox(window,height=15,width=60)
list1.grid(row=9,column=1,rowspan=10,columnspan=3)



window.mainloop()
