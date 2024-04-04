import datetime
from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
def create_user():
    d = datetime.date.today()
    command = f'pytest src/check_response/Create_user.py --html="report/{d}/Create_user.html"'
    os.system(command)
    messagebox.showinfo("Task Completed", "Task completed!")

def delete_user():
    os.system(f"pytest src/check_response/Delete_user.py --html=report/{datetime.date.today()}/Delete_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def get_user():
    os.system(f"pytest src/check_response/Get_users.py --html=report/{datetime.date.today()}/Get_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")
def update_user():
    os.system(f"pytest src/check_response/Update_user.py --html=report/{datetime.date.today()}/Update_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def login():
    os.system(f"pytest src/check_response/Login.py --html=report/{datetime.date.today()}/Login.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def register():
    os.system(f"pytest src/check_response/Register.py --html=report/{datetime.date.today()}/Register.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def dos():
    os.system(f"pytest src/security/Dos.py --html=report/{datetime.date.today()}/DOS.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def sql_injection():
    os.system(f"pytest src/security/SQL_Injection.py --html=report/{datetime.date.today()}/SQL_Injection.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def close_root():
  root.destroy()

def all():
    os.system(f"pytest src/check_response/Create_user.py --html=report/{datetime.date.today()}//Create_user.html")
    os.system(f"pytest src/check_response/Delete_user.py --html=report/{datetime.date.today()}//Delete_user.html")
    os.system(f"pytest src/check_response/Get_users.py --html=report/{datetime.date.today()}//Get_user.html")
    os.system(f"pytest src/check_response/Update_user.py --html=report/{datetime.date.today()}//Update_user.html")
    os.system(f"pytest src/check_response/Login.py --html=report/{datetime.date.today()}//Login.html")
    os.system(f"pytest src/check_response/Register.py --html=report/{datetime.date.today()}//Register.html")
    os.system(f"pytest src/security/Dos.py --html=report/{datetime.date.today()}//DOS.html")
    os.system(f"pytest src/security/SQL_Injection.py --html=report/{datetime.date.today()}//SQL_Injection.html")
    messagebox.showinfo("All Task Completed", "All Task completed!")

root = Tk()
root.title("Testing API")
root.geometry("800x400")

root.option_add("*Font", "Arial")
root.configure(background='#7D95AB')

style = ttk.Style()
style.configure('TButton', font=('Arial', 14), foreground="black", background="light blue", width=20)

label = Label(root, text="Welcome to the Testing API!", font=("Arial", 16))
label.pack(pady=10)

button_create_user = ttk.Button(root, text="Create User", width=20, command=create_user)
button_create_user.place(x=50, y=50, width=150)

button_delete_user = ttk.Button(root, text="Delete User", width=20, command=delete_user)
button_delete_user.place(x=230, y=50, width=150)

button_get_user = ttk.Button(root, text="Get User", width=20, command=get_user)
button_get_user.place(x=410, y=50, width=150)

button_update_user = ttk.Button(root, text="Update User", width=20, command=update_user)
button_update_user.place(x=590, y=50, width=150)

button_login = ttk.Button(root, text="Login", width=20, command=login)
button_login.place(x=230, y=100, width=150)

button_register = ttk.Button(root, text="Register", width=20, command=register)
button_register.place(x=410, y=100, width=150)

label_security = Label(root, text="Security:", font=("Arial", 14))
label_security.place(x=70, y=150, width=150)

button_dos = ttk.Button(root, text="Dos", width=10, command=dos)
button_dos.place(x=230, y=150, width=150)

button_sql_injection = ttk.Button(root, text="SQL Injection", width=15, command=sql_injection)
button_sql_injection.place(x=410, y=150, width=150)

button_all = ttk.Button(root, text="ALL", command=all, width=10)
button_all.place(x=320, y=200, width=150)

button_quit = ttk.Button(root, text="Quit", command=close_root, width=10)
button_quit.place(x=320, y=250, width=150)

root.mainloop()
