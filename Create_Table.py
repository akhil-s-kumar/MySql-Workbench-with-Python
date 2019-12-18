import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#',database="akhil")
cursor = connection.cursor()

def create_table_win():
    def create_table():
        tablename = "{}".format(tablennameentry.get())
        columnname1 = "{}".format(columnentry1.get())
        columntype1 = "{}".format(var1.get())
        columnsize1 = "{}".format(columndatasize1.get())
        columnname2 = "{}".format(columnentry2.get())
        columntype2 = "{}".format(var2.get())
        columnsize2 = "{}".format(columndatasize2.get())
        create_table = "create table {}({} {}({}), {} {}({}))".format(tablename, columnname1, columntype1, columnsize1, columnname2, columntype2, columnsize2)
        try:
         cursor.execute(create_table)
         print("Table Created!")
        except mysql.connector.Error:
          print("Fields could'nt be empty")
    root = tkinter.Tk()
    root.title("Create Table")
    root.geometry("500x500")

    var1 = StringVar(root)
    var1.set("Datatype")
    var2 = StringVar(root)
    var2.set("Datatype")

    Label(root, text="Enter the table name").grid(row=1, column=1)

    tablennameentry = Entry(root)
    tablennameentry.grid(row=1, column=2)

    Label(root, text="Enter the column name").grid(row=2, column=1)
    columnentry1 = Entry(root)
    columnentry1.grid(row=2, column=2)

    column1opt = OptionMenu(root, var1, "char", "varchar", "int", "float")
    column1opt.grid(row=2, column=3)

    Label(root, text="Enter the size").grid(row=2, column=4)
    columndatasize1 = Entry(root)
    columndatasize1.grid(row=2, column=5)

    Label(root, text="Enter the column name").grid(row=3, column=1)
    columnentry2 = Entry(root)
    columnentry2.grid(row=3, column=2)
    column2opt = OptionMenu(root, var2, "char", "varchar", "int", "float")
    column2opt.grid(row=3, column=3)
    Label(root, text="Enter the size").grid(row=3, column=4)
    columndatasize2 = Entry(root)
    columndatasize2.grid(row=3, column=5)

    Button(root,text='Create', command=create_table).grid(row=4, column=4)
    root.mainloop()
