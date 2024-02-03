from tkinter import *
from tkinter import messagebox



def help():
    top = Toplevel(root)
    top.title("Help")

    
def cancel():
    mb = messagebox.askyesno(title="Cancel",message="Do you wnat to Cancel?")
    if mb == 1:
        root.destroy()
    else:
        pass
    

def login():

    def change():
        if v.get() == 1:
            win.config(bg="red")
        elif v.get() == 2:
            win.config(bg="green")
        elif v.get() == 3:
            win.config(bg="Blue")
        elif v.get() == 4:
            win.config(bg="yellow")
        else:
            pass
        
    name = ent_name.get()
    passw = int(ent_pass.get())

    if name == "pouya" and passw == 1234:
        root.destroy()
        win = Tk()
        win.title("Hello")
        win.geometry(f"{ww}x{wh}+{wx}+{wy}")
        win.config(bg="yellow")
        

        # lbl_hell = Label(win,text="Hello pouya,Welcome back!",font="Arial 20 bold",bg="yellow")
        # lbl_hell.place(x=120,y=250)
        
        v = IntVar(win,0)
        Options = {"Red": 1 , "Green": 2 , "Blue": 3, "yellow": 4}
        for txt,val in Options.items():
            radiobtn = Radiobutton(win,variable=v,value=val,text=txt,bg="yellow").pack(side=TOP,pady=4)


        btn_change = Button(win,text="Change",command=change)
        btn_change.pack()

        win.mainloop()

root = Tk()
root.title("Login")
root.config(bg="grey")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
cx = screen_w / 2
cy = screen_h / 2
ww = 600
wh = 600
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)
root.geometry(f"{ww}x{wh}+{wx}+{wy}")

lbl_name = Label(root,text="Username: ")
lbl_name.place(x=100,y=100)


lbl_lastname = Label(root,text="lastname: ")
lbl_lastname.place(x=100,y=150)

ent_name = Entry(root)
ent_name.place(x=200,y=100)

ent_pass = Entry(root,show="*")
ent_pass.place(x=200,y=150)


btn_login = Button(root,text="Login",command=login)
btn_login.place(x=200,y=400)


btn_cancel = Button(root,text="Cancel",command=cancel)
btn_cancel.place(x=300,y=400)


btn_help = Button(root,text="Help",command=help)
btn_help.place(x=400,y=400)


root.mainloop()