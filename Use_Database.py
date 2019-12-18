# Modules
import mysql.connector
import Database_Options
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
         Database_Options.database_options_win()
        except mysql.connector.Error:
          print("Unknown database!")
    root = tkinter.Tk()
    root.title("Use Database")
    root.geometry("500x500")
    Label(root, text="Enter the database you want to use").pack(side=LEFT, expand=True)
    usedatabaseentry = Entry(root)
    usedatabaseentry.pack(side=LEFT, expand=True)
    Button(root,text='Use', command=use_database).pack(side=LEFT, expand=True)
    root.mainloop()



