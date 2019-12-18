# Modules
import tkinter
from tkinter import *
import Show_Database
import Create_Database
import Drop_Database
import Use_Database

# Frame
root = tkinter.Tk()
root.title("MySql Workbench with Python")
root.geometry("1366x768")


frame=Frame(root, width=1366, height=768, background="#3B4045")
frame.pack(expand=True,fill="both")

SDbtn = Button(frame,text="Show Databases",fg="red", font=("Verdana",15),command=Show_Database.show_database_win)
SDbtn.pack(side=LEFT, expand=True)

CNDbtn = Button(frame,text="Create Databases",fg="red", font=("Verdana",15),command=Create_Database.create_database_win)
CNDbtn.pack(side=LEFT, expand=True)

DEDbtn = Button(frame,text="Drop Databases",fg="red", font=("Verdana",15),command=Drop_Database.drop_database_win)
DEDbtn.pack(side=LEFT, expand=True)

UDbtn = Button(frame,text="Use Databases",fg="red", font=("Verdana",15),command=Use_Database.use_database_win)
UDbtn.pack(side=LEFT, expand=True)

root.mainloop()
