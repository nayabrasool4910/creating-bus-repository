from tkinter import *
import backadmin

def search_text():
    list1.delete(0,END)
    for rows_search in backadmin.search(source_text.get(),destination_text.get()):
        list1.insert(END,rows_search)

def view_text():
    list1.delete(0,END)
    for rows_view in backadmin.view():
        list1.insert(END,rows_view)

window=Tk()
window.title("KNR TRAVELS")
window.configure(background="sky blue")

l1=Label(window,text="SOURCE:",fg="red")
l1.grid(row=0,column=0)

l2=Label(window,text="DESTINATION:",fg="red")
l2.grid(row=2,column=0)

l3=Label(window, text="WISH YOU A HAPPY JOURNEY",fg="red",font="none 40 bold")
l3.grid(row=10,column=10)

source_text=StringVar()
e1=Entry(window,textvariable=source_text)
e1.grid(row=0,column=1)

destination_text=StringVar()
e2=Entry(window,textvariable=destination_text)
e2.grid(row=2,column=1)

b1=Button(window,text="search",fg="red",command=search_text)
b1.grid(row=1,column=4)

b2=Button(window,text="  view",fg="red",command=view_text)
b2.grid(row=1,column=5)

list1=Listbox(window,height=10,width=100)
list1.grid(row=0,column=8,rowspan=10,columnspan=3)


window.mainloop()
