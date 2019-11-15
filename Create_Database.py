# Modules
import mysql.connector
import tkinter
from tkinter import *

# MySql Connection
connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#')
cursor = connection.cursor()


def create_database_win():
    def create_database():
        create_database = "create database {}".format(databaseentry.get())
        try:       
          cursor.execute(create_database)
          print("Database",databaseentry.get(),"has been created successfully!")
        except mysql.connector.Error:
          print("Database",databaseentry.get(),"is already existing!")

    root = tkinter.Tk()
    root.title("Create Database")
    root.geometry("500x500")
    Label(root, text="Database").grid(row=0)
    databaseentry = Entry(root)
    databaseentry.grid(row=0, column=1)
    Button(root,text='Create', command=create_database).grid(row=3, column=1)
    root.mainloop()
    
