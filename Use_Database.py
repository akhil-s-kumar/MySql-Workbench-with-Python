# Modules
import mysql.connector
import tkinter
from tkinter import *

# MySql Connection
connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#')
cursor = connection.cursor()


def use_database_win():
    def use_database():
        use_database = "use {}".format(usedatabaseentry.get())
        try:
         cursor.execute(use_database)
         print("Database changed!")
        except mysql.connector.Error:
          print("Unknown database!")

    root = tkinter.Tk()
    root.title("Use Database")
    root.geometry("500x500")
    Label(root, text="Enter the database you want to use").grid(row=0)
    usedatabaseentry = Entry(root)
    usedatabaseentry.grid(row=0, column=1)
    Button(root,text='Use', command=use_database).grid(row=3, column=1)
    root.mainloop()
