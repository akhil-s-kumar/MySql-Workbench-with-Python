import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#',database="akhil")
cursor = connection.cursor()

def show_tables_win():
    def show_tables():
        show_tables = "show tables;"
        cursor.execute(show_tables)
        a = cursor.fetchall()
        return a
    root = tkinter.Tk()
    root.title("Show Tables")
    root.geometry("500x500")
    showtables_Message = Message(root, text=show_tables(), width=220,font=("Verdana",15))
    showtables_Message.pack(side=LEFT, expand=True)

    root.mainloop()
