from tkinter import *
from  oopwithUI import *
from tkinter import messagebox

def letter():
    s1 = Student(ent_fname.get(),ent_Lname.get(),int(ent_score.get()))
    x = s1.state(int(ent_score.get()))
    lst_box.insert(END,f"{s1.fname},{s1.Lname},{s1.score}")
    messagebox.showinfo(message=x,title="state")


root = Tk()
root.geometry("500x500+500+200")


lbl_name = Label(root,text="Fname : ",font="Arial 10 bold")
lbl_name.place(x=10,y=20)

lbl_Lname = Label(root,text="Lname : ",font="Arial 10 bold")
lbl_Lname.place(x=10,y=60)


lbl_score = Label(root,text="score : ",font="Arial 10 bold")
lbl_score.place(x=10,y=100)


ent_fname = Entry(root)
ent_fname.place(x=100,y=20)

ent_Lname = Entry(root)
ent_Lname.place(x=100,y=60)

ent_score = Entry(root)
ent_score.place(x=100,y=100)

lst_box = Listbox(root,font="Arial 10 bold",width=60)
lst_box.place(x=30,y=150)


btn_insert = Button(root,text="insert")
btn_insert.place(x=30,y=350)

btn_state = Button(root,text="state",command=letter)
btn_state.place(x=130,y=350)


btn_exit = Button(root,text="Exit")
btn_exit.place(x=30,y=400)

root.mainloop()