"""
Title
Author
Year
ISBN

view the list
add a book
delete a book
search a book
update a book

"""


#from backend import Bookstore
from tkinter import *
from backend import *

book=Bookstore()
selected_list=[]
flag=0

def get_select(event):
    global selected_list
    global flag
    flag=1
    if len(list.curselection())==0 or ("None" and "Selected" in list.get(ACTIVE)):
        pass
    else:
        index = list.curselection()[0]
        selected_list=list.get(index)
        empty_entry()
        fill_entry()

def empty_entry():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def fill_entry():
    e1.insert(END,selected_list[1])
    e2.insert(END,selected_list[2])
    e3.insert(END,selected_list[3])
    e4.insert(END,selected_list[4])

def view_command():
    global flag
    flag=0
    list.delete(0,END)
    for _ in book.view():
        list.insert(END,_)

def del_command():
    if len(selected_list)==0 or (list.get(ACTIVE)=="None Selected" or list.get(ACTIVE)=="None Selected To Update"):
        list.delete(0,END)
        list.insert(END,"None Selected")
        pass
    else:
        index=selected_list[0]
        list.delete(0,END)
        list.insert(END,selected_list)
        list.insert(END,"DELETED")
        book.delete(index)

def search_command():
    list.delete(0,END)
    for _ in book.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list.insert(END,_)

def update_command():
    if flag==0 or  (list.get(ACTIVE)=="None Selected To Update" or list.get(ACTIVE)=="None Selected"):
        list.delete(0,END)
        list.insert(END,"None Selected To Update")
        pass
    else:
        t=selected_list[0]
        book.update(t,title=e1.get(),author=e2.get(),year=e3.get(),isbn=e4.get())

def exit_command():
    window.destroy()

def add_command():
    list.delete(0,END)
    if not (e1.get().strip() and e2.get().strip() and e3.get().strip() and e4.get().strip()):
        list.insert(END,"ENTER ALL THE VALUES")
    else:
        book.insert(e1.get(),e2.get(),e3.get(),e4.get())
        list.insert(END,"SUCCESSFUL")
        empty_entry()

window = Tk()
window.wm_title("bookstore")

title=Label(window,text="Title")
title.grid(row=0,column=0)

auth=Label(window,text="Author")
auth.grid(row=0,column=2)

year=Label(window,text="Year")
year.grid(row=1,column=0)

isbn=Label(window,text="ISBN")
isbn.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text,fg="red",bd=4)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text,fg="red",bd=4)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text,fg="red",bd=4)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text,fg="red",bd=4)
e4.grid(row=1,column=3)

list = Listbox(window, height = 8 , width = 40,selectbackground='green',fg="white",bd=3,bg="grey")
list.grid(row=2,column=0, rowspan = 6,columnspan = 2)

scroll =Scrollbar(window)
scroll.grid(row=2,column = 2 ,rowspan = 6)

list.configure(yscrollcommand=scroll.set)
scroll.configure(command = list.yview)

list.bind("<<ListboxSelect>>",get_select)

b1=Button(window,text = "View All",width=14,bd=4,bg="lightgreen",command=view_command)
b1.grid(row = 2 ,column =3 )

b2=Button(window,text = "Search Book",width=14,bd=4,bg="lightgreen",command=search_command)
b2.grid(row = 3,column =3 )

b3=Button(window,text = "Add Book",width=14,bd=4,bg="lightgreen",command=add_command)
b3.grid(row = 4,column = 3)

b4=Button(window,text = "Update Book ",width=14,bd=4,bg="lightgreen",command=update_command)
b4.grid(row = 5,column = 3)

b5=Button(window,text = "Delete Book",width=14,bd=4,bg="lightgreen",command=del_command)
b5.grid(row = 6,column = 3)

b6=Button(window,text = "Close",width=14,bd=4,bg="lightgreen",command=exit_command)
b6.grid(row = 7,column = 3)


window.mainloop()
