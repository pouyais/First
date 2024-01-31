from tkinter import *


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


lbl_lisbox = Label(root,text="List Box",font="Arial 20 bold",bg="yellow")
lbl_lisbox.place(x=0,y=50)


lst_contact = Listbox(root,)
lst_contact.pack(side=LEFT,expand=1,fill=BOTH)


sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

sb.config(command=lst_contact.yview)

a = 0
for i in range(51):
    a += 1
    lst_contact.insert(END,f"{a}-This is line")
    

root.mainloop()