import mysql.connector
import Use_Database
import Show_Tables
import Drop_Table
import Create_Table
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root",passwd='akhilS29#',database="akhil")
cursor = connection.cursor()

def database_options_win():

    root = tkinter.Tk()
    root.title("Database Options")
    root.geometry("500x500")

    STbtn = Button(root,text="Show Tables",fg="red", font=("Verdana",15),command=Show_Tables.show_tables_win)
    STbtn.pack(side=LEFT, expand=True)

    CTbtn = Button(root,text="Create Table",fg="red", font=("Verdana",15),command=Create_Table.create_table_win)
    CTbtn.pack(side=LEFT, expand=True)

    DTbtn = Button(root,text="Drop Table",fg="red", font=("Verdana",15),command=Drop_Table.drop_table_win)
    DTbtn.pack(side=LEFT, expand=True)
    
    root.mainloop()
