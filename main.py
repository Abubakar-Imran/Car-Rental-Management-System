import tkinter.messagebox
from tkinter import *
import json
from user import *
from admin import *
# creating root object
root = Tk()

# defining size of window
root.geometry("1920x1080")
# bg = PhotoImage(file="download.png")
label1 = Label(root)
label1.place(x=0, y=0)

# setting up the title of window
root.title("Car Rental System")

# creating a text label
"""
The login button. This will take the username and password and compare it to the stored credentials.
If the credentials are correct, the user will be taken to the main menu. Otherwise, the user will be prompted to try again.
"""
Label(root, text='Welcome to Car Rental System', font=('Verdana', 50), bg="#463f3a", fg="white", padx=20, pady=20,
      relief=RIDGE, borderwidth=10).pack(pady=50)
# creating a Registration Form
Label(root, text="USERNAME:", font=('Verdana', 20), bg="#ede0d4", borderwidth=10, relief=RAISED).place(x=330, y=250)
name_field = Entry(root, width=30, font=('Verdana', 15), bg="#ede0d4")
name_field.place(x=330, y=320)
Label(root, text="PASSWORD:", font=('Verdana', 20), bg="#ede0d4", borderwidth=10, relief=RAISED).place(x=330, y=400)
pass_field = Entry(root, show="*", width=30, font=('Verdana', 15),  bg="#ede0d4")
pass_field.place(x=330, y=470)

# creating a buttons
Button(root, text='Login', font=("Verdana", 20), fg='white', bg='#52b788', width=20, height=1, borderwidth=10,
       relief=RIDGE, command=lambda: login()).place(x=850, y=275)
Button(root, text='Signup', font=("Verdana", 20), fg='white', bg='#52b788', width=20, height=1, borderwidth=10,
       relief=RIDGE, command=lambda: sign_up()).place(x=850, y=425)

# creating a function to store details


def sign_up():
    """
     this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up a new user. this function is used to sign up
    """
    name = name_field.get()
    password = pass_field.get()
    if name == '' or password == '':
        """
        If the name or password is empty, then we need to prompt the user for their credentials.
        @param name - the user's name           
        @param password - the user's password           
        """
        tkinter.messagebox.showerror("Error", "All Fields are required!!")
    elif name == "admin":
        tkinter.messagebox.showerror("Error", "Admin is already registered")
    else:

        # assigning the details to tuples
        f = open("database.json")
        """
        This function is used to save the user details in the database.
        @param name - the user name
        @param password - the password
        @returns the success message
        """

        with open("database.json", "r") as f:
            data1 = json.load(f)
        for is_Present in data1["user_details"]:
            if is_Present["user_name"] == name:
                tkinter.messagebox.showerror("Error", "Account already exists")
                break
        else:
            data1["user_details"].append({"user_name": name, "password": password, "name": "",
                                         "phone": "", "age": "", "email": "", "gender": "", "bookings": {"car_name": ""}})
            with open("database.json", "w") as f:
                json.dump(data1, f)
            # displaying success message
            tkinter.messagebox.showinfo(
                "Success", "Your Details Saved Successfully")


def login():
    """
    Login to the database.
    @returns the database cursor
    """
    g = open("database.json")
    data = json.load(g)
    name = name_field.get()
    password = pass_field.get()
    index = 0
    if (name == "admin" and password == "admin"):
        root.destroy()
        admin()
    else:
        for is_present in data["user_details"]:

            if is_present["user_name"] == name and is_present["password"] == password:
                """
                Check if the user name and password are correct. If so, log them in. Otherwise, keep trying.
                @param user_name - the user name input by the user.
                @param password - the password input by the user.
                """
                tkinter.messagebox.showinfo(
                    "Login Status", "Successfully Logged in")
                root.destroy()
                name_d(name)
                idxe(index)
                user_window()
                break
            index += 1
        else:
            tkinter.messagebox.showerror("Error", "Data Not Registered")


# mainloop
root.mainloop()
