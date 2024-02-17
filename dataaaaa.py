from tkinter import *
import classmake
db = classmake.database('d:/mydatapedarsag.db')


window = Tk()
# func
def exit_():
    window.destroy()


def insert():
    db.insertt(ent_fname.get() , ent_lname.get() , int(ent_score.get()))

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_fname.delete(0,END)
# lbl
window.geometry('400x400')
lbl_fname = Label(text='fname:')
lbl_fname.place(x=5,y=0)

lbl_lname = Label(text='lname:')
lbl_lname.place(x=5,y=50)

lbl_score = Label(text='score:')
lbl_score.place(x=5,y=100)
# ent
ent_fname = Entry()
ent_fname.place(x=50,y=0)

ent_lname = Entry()
ent_lname.place(x=50,y=50)

ent_score = Entry()
ent_score.place(x=50,y=100)
# btn

btn_insert= Button(text='insert',width=5,height=1,command=insert)
btn_insert.place(x=50,y=300)

btn_button= Button(text='exit',width=5,height=1,command=exit_)
btn_button.place(x=300,y=300)



window.mainloop()