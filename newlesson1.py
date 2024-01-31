from tkinter import *


def click():
    global i
    if v.get() == 1:
        root.config(bg="red")
    else:
        pass


root = Tk()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
print(screen_w,screen_h)

cx = screen_w / 2
cy = screen_h / 2
ww = 600
wh = 600
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)

root.geometry(f"{ww}x{wh}+{wx}+{wy}")
root.title("new lesson")
root.config(bg="yellow")


v = IntVar(root)


ckbox = Checkbutton(root,text="Red",variable = v)
ckbox.pack(side=TOP)

btn_click = Button(root,text="Run",command=click)
btn_click.pack(side=TOP)

lst_contact = Listbox(root,)
lst_contact.pack(side=LEFT,fill=Y)


sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

sb.config(command=lst_contact.yview)

a = 0
for i in range(51):
    a += 1
    lst_contact.insert(END,f"{a}-This is line")
    

root.mainloop()