import datetime
from datetime import date
from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
def create_user():
    # current_date = datetime.now()
    # print(current_date)
    #
    # # Định dạng ngày thành chuỗi theo định dạng '%d.%m.%Y'
    # formatted_date = current_date.strftime('%d.%m.%Y')
    os.system(f"pytest src/check_response/Get_users.py --html=report/$ABC/Create_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def delete_user():
    os.system("pytest Mã Nguồn/src/check_response/Delete_user.py --html=report/$(date +%d.%m.%Y)/Delete_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def get_user():
    os.system("pytest src/check_response/Get_users.py --html=report/$(date +%d.%m.%Y)/Get_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")
def update_user():
    os.system("pytest src/check_response/Update_user.py --html=report/$(date +%d.%m.%Y)/Update_user.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def login():
    os.system("pytest src/check_response/Login.py --html=report/$(date +%d.%m.%Y)/Login.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def register():
    os.system("pytest src/check_response/Register.py --html=report/$(date +%d.%m.%Y)/Register.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def dos():
    os.system("pytest src/security/Dos.py --html=report/$(date +%d.%m.%Y)/DOS.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def sql_injection():
    os.system("pytest src/security/SQL_Injection.py --html=report/$(date +%d.%m.%Y)/SQL_Injection.html")
    messagebox.showinfo("Task Completed", "Task completed!")

def all():
    os.system("pytest src/check_response/Create_user.py --html=report/$(date +%d.%m.%Y)/Create_user.html")
    os.system("pytest src/check_response/Delete_user.py --html=report/$(date +%d.%m.%Y)/Delete_user.html")
    os.system("pytest src/check_response/Get_users.py --html=report/$(date +%d.%m.%Y)/Get_user.html")
    os.system("pytest src/check_response/Update_user.py --html=report/$(date +%d.%m.%Y)/Update_user.html")
    os.system("pytest src/check_response/Login.py --html=report/$(date +%d.%m.%Y)/Login.html")
    os.system("pytest src/check_response/Register.py --html=report/$(date +%d.%m.%Y)/Register.html")
    os.system("pytest src/security/Dos.py --html=report/$(date +%d.%m.%Y)/DOS.html")
    os.system("pytest src/security/SQL_Injection.py --html=report/$(date +%d.%m.%Y)/SQL_Injection.html")
    messagebox.showinfo("All Task Completed", "All Task completed!")
root = Tk()
root.title("Testing API")

root.option_add("*Font", "Arial")  # thêm dòng này để đổi font chữ thành Arial

style = ttk.Style()
style.configure('TButton', font=('Arial', 14), foreground="black", background="light blue", width=20)

label = Label(root, text="Welcome to the Testing API!", font=("Arial", 16))
label.pack(pady=10)

frame1 = Frame(root)
frame1.pack(pady=10)

button1 = ttk.Button(frame1, text="Create User", width=20,command=create_user)
button1.pack(side=LEFT, padx=5)

button2 = ttk.Button(frame1, text="Delete User", width=20,command=delete_user)
button2.pack(side=LEFT, padx=5)

button3 = ttk.Button(frame1, text="Get User", width=20,command=get_user)
button3.pack(side=LEFT, padx=5)

button4 = ttk.Button(frame1, text="Update User", width=20,command=update_user)
button4.pack(side=LEFT, padx=5)

frame2 = Frame(root)
frame2.pack(pady=10)

button5 = ttk.Button(frame2, text="Login", width=20,command=login)
button5.pack(side=LEFT, padx=5)

button6 = ttk.Button(frame2, text="Register", width=20,command=register)
button6.pack(side=LEFT, padx=5)

frame3 = Frame(root)
frame3.pack(pady=10)

label2 = Label(frame3, text="Security:", font=("Arial", 14))
label2.pack(side=LEFT, padx=5)

button7 = ttk.Button(frame3, text="Dos", width=10,command=dos)
button7.pack(side=LEFT, padx=5)

button8 = ttk.Button(frame3, text="SQL Injection", width=15,command=sql_injection)
button8.pack(side=LEFT, padx=5)

button9 = ttk.Button(root, text="ALL", command=all, width=10)
button9.pack(pady=10)


button9 = ttk.Button(root, text="Quit", command=root.quit, width=10)
button9.pack(pady=10)


root.mainloop()
