
from tkinter import *
window = Tk()
# This is the main window with the login and Register system
def delete():
    for widget in window.winfo_children():
        widget.destroy()
def main_window():
    delete()
    window.geometry("420x420")
    window.configure(bg="#00b7ff")
    #Register and login buttons
    Register=Button(window,text="Register",padx=20,pady=3,command=sign_up)
    Login_button=Button(window,text="Sign In",padx=23,pady=3,command=sign_in)
    Register.place(x=165,y=180)
    Login_button.place(x=165,y=215)
    window.mainloop()
def sign_up():
    delete()
    #Letting the user choose a username and password
    username_label=Label(window,text="Username",bg="#00b7ff").place(x=100,y=110)
    username_entry=Entry(width=35,borderwidth=5)
    password_label=Label(window,text="Password",bg="#00b7ff").place(x=100,y=159)
    password_entry=Entry(window,width=35,borderwidth=5)
    def save():
        password_file=open("password.txt","w")
        username_file=open("username.txt","w")
        #Writing the user to the files
        username_file.write(username_entry.get())
        password_file.write(password_entry.get())
        username_file.close()
        password_file.close()
        main_window()
    save_button=Button(window,text="Finish",padx=20,pady=2,command=save).place(x=100,y=213)
    username_entry.place(x=100,y=130)
    password_entry.place(x=100,y=179)
    #Save the username and password to a file
def sign_in():
    delete()
    login_label=Label(window,text="Username",bg="#00b7ff").place(x=100,y=110)
    login_entry=Entry(window,width=35,borderwidth=5)
    password_label=Label(window,text="Password",bg="#00b7ff").place(x=100,y=159)
    password_entry=Entry(window,width=35,borderwidth=5)
    try_username = open("username.txt",'r')
    try_password = open("password.txt",'r')
    user = try_username.read()
    password_=try_password.read()
    def Login_try():
        if login_entry.get() != user or password_entry.get() != password_:
            incorrect=Label(window,text="Incorrect username or password",bg="#00b7ff",fg="red").place(x=100,y=245)
        elif login_entry.get() == user and password_entry.get() == password_:
            delete()
            correct=Label(window,text="Success",bg="#00b7ff").pack()
    login_button=Button(window,padx=26,pady=3,text="Login",command=Login_try).place(x=100,y=213)
    login_entry.place(x=100,y=130)
    password_entry.place(x=100,y=179)
main_window()
