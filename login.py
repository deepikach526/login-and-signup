import tkinter as tk
from tkinter import messagebox

FILE_NAME="users.txt"

def is_valid_password(password):
    if len(password)<6:
        return False
    has_digit=any(char.isdigit()
                  for char in password)
    has_letter=any(char.isalpha()
                   for char in password)
    return has_digit and has_letter


def user_exists(username):
    try:
        with open(FILE_NAME,"r") as file:
            for line in file:
                user,_=line.strip().split(",")
                if user==username:
                    return True
    except FileNotFoundError:
        return False
    return False

def signup():
    username=entry_user.get()
    password=entry_pass.get()

    if username ==""or password =="":
        messagebox.showerror("Error","All fields are required!")
        return
    if user_exists(username):
        messagebox.showerror("Error","Username already exists!")
        return
    if not is_valid_password(password):
        messagebox.showerror("Error","Password must be 6+ chars with letters &digits!")
        return
    with open (FILE_NAME,"a") as file:
        file.write(f"{username},{password}\n")
    messagebox.showinfo("Success","Signup successful")
    entry_user.delete(0,tk.END)
    entry_pass.delete(0,tk.END) 

def login():
    username=entry_user.get()
    password=entry_pass.get()

    try:
        with open (FILE_NAME,"r") as file:
            for line in file:
                user,pwd=line.strip().split(",")
                if user==username and pwd == password:
                    messagebox.showinfo("Success","Login successful!")
    except FileNotFoundError:
        messagebox.showerror("Error","No users found.Please signup first.")
        return
        messagebox.showerror("Error","Invaliud Username or Password!")   


root=tk.Tk()
root.title("Login & Signup System")
root.geometry("400x300")
root.config(bg="#1e1e2f")

title=tk.Label(root,text="Login & Signup",font=("Arial",18,"bold"),bg="#1e1e2f",fg="white")
title.pack(pady=15)

label_user=tk.Label(root,text="Username",bg="#1e1e2f",fg="white")
label_user.pack()
entry_user=tk.Entry(root,width=30)
entry_user.pack(pady=5)

label_pass=tk.Label(root,text="Password",bg="#1e1e2f",fg="white")
label_pass.pack()
entry_pass=tk.Entry(root, width=30)
entry_pass.pack(pady=5)

frame=tk.Frame(root,bg="#1e1e2f")
frame.pack(pady=15)

btn_signup=tk.Button(frame,text="Signup",width=10,bg="#4caf50",fg="white",command=signup)
btn_signup.pack(side="left",padx=10)

btn_login=tk.Button(frame,text="Login",width=10,bg="#2196f3",fg="white",command=login)
btn_login.pack(side="left",padx=10)

root.mainloop()