from tkinter import *
from tkinter import messagebox

# ===== Functions =====

def insert(*event):
    name = ent_name.get()
    score = int(ent_score.get())
    if 0 < score <= 100:
        lst_student.insert(END,f'{name},{score}')
    else:
        messagebox.showinfo(title="Incorrect validation",message="Your score must be between 0 to 100")
    clear()
    

def clear():
    ent_name.delete(0,END)
    ent_score.delete(0,END)
    ent_name.focus_set()
    
    
def delete():
    lst_student.delete(lst_student.curselection())
    

def fetch():
    data = lst_student.get(lst_student.curselection()).split(",")
    ent_name.insert(0,data[0])
    ent_score.insert(0,data[1])
    lst_student.delete(lst_student.curselection())
    



# ===== UI Design =====
root = Tk()
root.geometry("500x500+500+100")
root.title("contact manager")
root.config(bg="#4d94ff")
root.resizable(0,0)
root.bind("")


lblname = Label(root,text="Name : ",bg="#4d94ff",font="Arial 12 bold")
lblname.place(x=50,y=50)


lblscore = Label(root,text="Score : ",bg="#4d94ff",font="Arial 12 bold")
lblscore.place(x=50,y=120)


ent_name = Entry(root,font="Arial 12 bold")
ent_name.place(x=120,y=52)


ent_score = Entry(root,font="Arial 12 bold")
ent_score.bind("<Return>",insert)
ent_score.place(x=120,y=122)


lst_student = Listbox(root,width=30,font="tahoma 12 bold")
lst_student.place(x=50,y=200)


btninsert = Button(root,text="Insert",font="Arial 12 bold",command=insert)
btninsert.place(x=350,y=200)


btndelete = Button(root,text="Delete",font="Arial 12 bold",command=delete)
btndelete.place(x=350,y=250)


btnfetch = Button(root,text="Fetch",font="Arial 12 bold",command=fetch)
btnfetch.place(x=350,y=300)

btnfetch1 = Button(root,text="Fetch1",font="Arial 12 bold",command=fetch)
btnfetch1.place(x=350,y=350)



root.mainloop()