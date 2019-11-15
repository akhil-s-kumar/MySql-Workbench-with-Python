import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#')
cursor = connection.cursor()  
      
def show_database_win():
    def show_database():
        show_database = "show databases;"
        cursor.execute(show_database)
        a = cursor.fetchall()
        return a
        cursor.clear()
    root = tkinter.Tk()
    root.title("Show Database")
    root.geometry("500x500")

    showdatabase_Message = Message(root, text=show_database(), width=220,font=("Verdana",15))
    showdatabase_Message.pack(expand=True,fill="both")

    root.mainloop()

