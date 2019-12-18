import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#',database="akhil")
cursor = connection.cursor()

def drop_table_win():
    def drop_table():
        drop_tables = "drop table {}".format(droptableentry.get())
        try:
         cursor.execute(drop_tables)
         print("Table deleted!")
        except mysql.connector.Error:
          print("Unknown table!")
    root = tkinter.Tk()
    root.title("Show Tables")
    root.geometry("500x500")
    Label(root, text="Enter the table you want to delete").pack(side=LEFT, expand=True)
    droptableentry = Entry(root)
    droptableentry.pack(side=LEFT, expand=True)
    Button(root,text='Drop', command=drop_table).pack(side=LEFT, expand=True)
    root.mainloop()
