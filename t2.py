from tkinter import *


root = Tk()
root.geometry("600x600")
root.title("Contact Managment")

lblname = Label(root,text="Name:")
lblname.place(relx=0.1,rely=0.1)

lbllastname = Label(root,text="Lastname:")
lbllastname.place(relx=0.5,rely=0.1)

lblcity = Label(root,text="City:")
lblcity.place(relx=0.1,rely=0.2)

lbltel = Label(root,text="Tel:")
lbltel.place(relx=0.5,rely=0.2)


entryname = Entry()
entryname.place(relx=0.2,rely=0.1)


entrylastname = Entry()
entrylastname.place(relx=0.65,rely=0.1)


entrycity = Entry()
entrycity.place(relx=0.2,rely=0.2)


entrytel = Entry()
entrytel.place(relx=0.65,rely=0.2)


btninsert = Button(root,text="Insert")
btninsert.place(relx=0.8,rely=0.3)


btndelete = Button(root,text="Delete")
btndelete.place(relx=0.8,rely=0.35)


btnclear = Button(root,text="fetch")
btnclear.place(relx=0.8,rely=0.4)


btnexit = Button(root,text="Exit")
btnexit.place(relx=0.8,rely=0.45)


lsbox = Listbox(root)
lsbox.place(relx=0.2,rely=0.3)


root.mainloop()