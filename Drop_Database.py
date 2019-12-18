import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#')
cursor = connection.cursor()

def drop_database_win():
    def drop_database():
        drop_database = "drop database {}".format(dropdatabaseentry.get())
        try:
         cursor.execute(drop_database)
         print("Database",dropdatabaseentry.get(),"has been deleted successfully!")
        except mysql.connector.Error:
          print("Database",dropdatabaseentry.get(),"doesn't exist!")
    root = tkinter.Tk()
    root.title("Drop Database")
    root.geometry("500x500")
    Label(root, text="Enter the Database you want to delete").pack(side=LEFT, expand=True)
    dropdatabaseentry = Entry(root)
    dropdatabaseentry.pack(side=LEFT, expand=True)
    Button(root,text='Drop', command=drop_database).pack(side=LEFT, expand=True)
    root.mainloop()

