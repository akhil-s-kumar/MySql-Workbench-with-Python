# Modules
import mysql.connector
import tkinter
from tkinter import *

# MySql Connection
connection = mysql.connector.connect(host="localhost",user="root", passwd='akhilS29#')
cursor = connection.cursor()

# Frame
root = tkinter.Tk()
root.title("MySql Workbench with Python")
root.geometry("1366x768")

def show_database_win(): 
    showdatabasewin = Toplevel(root)
    showdatabasewin.title("Show Databases")
    showdatabasewin.geometry("500x500")
    showdatabase_label = Label(showdatabasewin, text="Hello Tkinter!")
    showdatabase_label.pack()
    

def create_database_win(): 
    createdatabasewin = Toplevel(root)
    createdatabasewin.title("Create Databases")
    createdatabasewin.geometry("500x500")

def drop_database_win(): 
    dropdatabasewin = Toplevel(root)
    dropdatabasewin.title("Drop Databases")
    dropdatabasewin.geometry("500x500")

def use_database_win(): 
    usedatabasewin = Toplevel(root)
    usedatabasewin.title("Use Databases")
    usedatabasewin.geometry("500x500")
    
frame=Frame(root, width=1366, height=768, background="#3B4045")
frame.pack(expand=True,fill="both")

SDbtn = Button(frame,text="Show Databases",fg="red", font=("Verdana",15),command=show_database_win)
SDbtn.pack(side=LEFT, expand=True)

CNDbtn = Button(frame,text="Create Databases",fg="red", font=("Verdana",15),command=create_database_win)
CNDbtn.pack(side=LEFT, expand=True)

DEDbtn = Button(frame,text="Drop Databases",fg="red", font=("Verdana",15),command=drop_database_win)
DEDbtn.pack(side=LEFT, expand=True)

UDbtn = Button(frame,text="Use Databases",fg="red", font=("Verdana",15),command=use_database_win)
UDbtn.pack(side=LEFT, expand=True)

root.mainloop()

cont = "y" or "Y"
while cont.lower() == "y" or cont.upper() == "Y":
    print("Press 1 to show all existing databases: ")
    print("Press 2 for creating a new database: ")
    print("Press 3 to drop a existing database: ")
    print("Press 4 to use a database: ")
    choice_1 = int(input("Enter your choice: "))
    
    if choice_1 == 1:
      show_database = "show databases;"
      cursor.execute(show_database)
      for i in cursor:
          print(i)

    if choice_1 == 2:
      create_database_name = input("Enter the database name: ")
      create_database = "create database {}".format(create_database_name)
      try:
         cursor.execute(create_database)
         print("Database",create_database_name,"has been created successfully!")
      except mysql.connector.Error:
          print("Database",create_database_name,"is already existing!")
          
    if choice_1 == 3:
      drop_database_name = input("Enter the database name you want to delete: ")
      drop_database = "drop database {}".format(drop_database_name)
      try:
         cursor.execute(drop_database)
         print("Database",drop_database_name,"has been deleted successfully!")
      except mysql.connector.Error:
          print("Database",drop_database_name,"doesn't exist!")

    if choice_1 == 4:
      use_database_name = input("Enter the database name you want to use: ")
      use_database = "use {}".format(use_database_name)
      try:
         cursor.execute(use_database)
         print("Database changed!")
         cont1 = "y" or "Y"
         while cont1.lower() == "y" or cont1.upper() == "Y":
             print("Press 1 to create a new table: ")
             print("Press 2 to delete a existing table: ")
             print("Press 3 to describe a table: ")
             print("Press 4 to show all existing tables: ")
             print("Press 5 to add values into a table: ")
             print("Press 6 to view all values in a table: ")
             print("Press 7 to alter a table: ")
             choice_2 = int(input("Enter your choice: "))

             if choice_2 == 1:
                 create_table_name = input("Enter the table name: ")
                 create_table_column = int(input("Enter the number of rows you wanted in the table: "))
                 create_table_column_name_list =[]
                 create_table_column_type_list =[]
                 create_table_column_compile = []
                 for i in range (create_table_column):
                       create_table_column_name = input("Enter the Column name: ")
                       print("press 1 for VARCHAR: ")
                       print("press 2 for CHAR: ")
                       print("press 3 for INT: ")
                       create_table_column_type = int(input("Enter column type: "))
                       if create_table_column_type == 1:
                           create_table_column_type1_size =int(input("Enter the size: "))
                           create_table_column_type1 = " varchar({})".format(create_table_column_type1_size)
                           create_table_column_compile.append(create_table_column_name+create_table_column_type1+",")
                 j = create_table_column_compile[-1][-1]
                 for k in create_table_column_compile:
                     l = k
                     print(k)
                 create_table = "create table {}({})".format(create_table_name,l)
                 try:
                    cursor.execute(create_table)
                    print("Table",create_table_name,"has been created successfully!")
                 except mysql.connector.Error:
                    print("Table",create_table_name,"already exist!")

         cont1 = input("Do you want to continue? (y/n)")
         if cont1 == "n":
             break
       
      except mysql.connector.Error:
          print("Unknown database!")




    cont = input("Do you want to continue? (y/n)")
    if cont == "n":
       break


