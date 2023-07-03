from tkinter import *
import json
import os
import tkinter.messagebox
from PIL import ImageTk, Image
import datetime
import time
import smtplib
import ssl

smtp_port = 587
"""
Send an email with the given context.
@param context - the context for the email.
"""
smtp_server = "smtp.gmail.com"

simple_email_context = ssl.create_default_context()
email_from = "needaspeed639@gmail.com"
pswd = "myqvetahydsgmkyz"

global start_date
start_date = datetime.date.today()
i = 1
name2 = ""


def name_d(name):
    """
    Set the global variable name2 to the name parameter.
    @param name - the name parameter
    """
    global name2
    name2 = name


def idxe(ind):
    """
    Set the global index variable to the input index.
    @param ind - the index to set the global index to
    """
    global i
    i = ind


def user_window():
    """
    Create the user window for the user to interact with.
    @param window - the window to be created.
    """

    # create the window
    window = Tk()
    window.geometry("1920x1080")
    header = Frame(window)
    header.pack(side=TOP, expand=YES, fill=BOTH, anchor="w")
    Label(header, text=f'Hello {name2}!', bg="black", fg="white", font=('Verdana', 20), width=100, pady=15).place(x=0,
                                                                                                                  y=0)
    Button(header, text="Log Out", width="14", bg="grey", fg="white", font=('Verdana', 10), pady=22,
           command=lambda: user_logout(window)).place(x=0, y=0)

    # create the bottom frame
    bottom_frame = Frame(window)
    bottom_frame.configure(bg="#b58463")
    bottom_frame.pack(side=BOTTOM, expand=YES, fill=BOTH)

    # create the top frame
    top_frame = Frame(window)
    top_frame.configure(bg="#e8ac65")
    top_frame.pack(side=BOTTOM)

    # add three buttons to the bottom frame
    Button(bottom_frame, text="Add Booking", width="20", pady=50, bg="red", fg="white", font=('Verdana', 19),
           borderwidth=20, relief=GROOVE,
           command=lambda: add_booking(window)).place(x=150, y=100)

    Button(bottom_frame, text="Current Booking", width="20", pady=50, bg="dark green", fg="white", font=('Verdana', 19),
           borderwidth=20, relief=GROOVE,
           command=lambda: current_booking(window)).pack(side=BOTTOM, anchor="center", pady=30)

    Button(bottom_frame, text="Edit Profile", width="20", pady=50, bg="blue", fg="white", font=('Verdana', 19),
           borderwidth=20, relief=GROOVE, command=lambda: add_personal(window)).place(
        x=1030, y=100)

    # add an image to the right frame
    img = PhotoImage(file="poster.png")
    image_label = Label(top_frame, image=img)
    image_label.pack(side=TOP)
    window.mainloop()


def add_booking(window):
    """
    Create the window for adding a booking.
    @param window - the main window
    """

    window.destroy()
    global add_book_window
    add_book_window = Tk()
    add_book_window.geometry("1920x1080")
    add_book_window.configure(bg="#f9dcc4")
    Label(add_book_window, text='ADD BOOKING', font=('Verdana', 50), bg="#ce4257", fg="white", padx=20, pady=20,
          relief=RIDGE, borderwidth=10).pack(pady=10)
    g = open("database.json")

    data_user = json.load(g)
    cars = []
    for car in data_user["cars"]:
        cars.append(car["name"])
    global dd_cars

    dd_cars = StringVar(add_book_window)
    dd_cars.set("Choose a car")
    dropdown_cars = OptionMenu(add_book_window, dd_cars, *cars)
    dropdown_cars.configure(font=("Verdana", 20), bg="#e8d6cb", fg="black")
    dropdown_cars.place(x=530, y=200)

    # Create a label and entry
    global l1
    """
    Create the labels and entries for the left frame.
    @param frame_left - the left frame
    """
    l1 = Label(add_book_window, text="Car Name:", font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global e1
    e1 = Entry(add_book_window, font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    # Create a label and entry
    global l2
    l2 = Label(add_book_window, text="Model", font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global e2
    e2 = Entry(add_book_window, font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global l3
    # Create a label and entry
    l3 = Label(add_book_window, text="License Plate:", font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global e3
    e3 = Entry(add_book_window, font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global l6
    l6 = Label(add_book_window, text="Description:", font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global l4
    l4 = Label(add_book_window, text="\n")
    global l5
    l5 = Label(add_book_window, text="Rate:", font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)
    global e5
    e5 = Entry(add_book_window, font=("Verdana", 18), bg="#e8d6cb", fg="black", relief=RAISED)

    global durations

    # Add the widgets to the two frames
    """
    Pack the widgets into the window.
    """
    l1.place(x=200, y=300)
    e1.place(x=400, y=300)
    l2.place(x=200, y=360)
    e2.place(x=400, y=360)
    l3.place(x=200, y=420)
    e3.place(x=400, y=420)
    l6.place(x=200, y=540)
    l4.place(x=200, y=600)
    l5.place(x=200, y=480)
    e5.place(x=400, y=480)
    btn = Button(add_book_window, text="Choose", font=("Verdana", 18), bg="#e8d6cb", fg="black",
                 command=lambda: show_details(add_book_window))
    btn.place(x=900, y=195)
    b1 = Button(add_book_window, text="Submit", bg="#ce4257", fg="white", font=("Verdana", 18), relief=RIDGE,
                borderwidth=5,
                command=lambda: show_bill(add_book_window))

    # fixed durations
    durations = StringVar(add_book_window)
    """
    Create the dropdown menu for the duration of the rent.
    @param frame_left - the left frame of the GUI.
    @param frame_right - the right frame of the GUI.
    """
    durations.set("Choose the period of rent")

    dropdown_time = OptionMenu(add_book_window, durations, "1 ", "2", "3", "4", "5", "6", "7")
    dropdown_time.configure(font=("Verdana", 18), bg="#e8d6cb", fg="black", )
    dropdown_time.place(x=200, y=700)
    b1.place(x=600, y=690)

    # BACK BUTTON ON ORDER WINDOW
    btn = Button(add_book_window, text="BACK", font=("Verdana", 18), bg="#ce4257", fg="white",
                 command=lambda: on_back(add_book_window))
    btn.place(x=0, y=0)
    # global canvas
    # Create a button
    global canvas
    """
    Create a canvas to display the images.
    @param frame_right - the frame to put the canvas in.
    """
    img1 = ImageTk.PhotoImage(Image.open("white.png"))
    canvas = Label(add_book_window, image=img1, width=500, height=450)
    canvas.place(x=900, y=300)

    add_book_window.mainloop()


def show_bill(add_book_window):
    dat = open("database.json")
    """
    This function is used to book a car. It takes the user input and sends an email to the customer.
    @param data - the database json file
    @param i - the index of the user in the database
    @param name_1 - the name of the car
    @param make_1 - the make of the car
    @param license_1 - the license of the car
    @param rate_1 - the rate of the car
    @param duration_t - the duration of the booking
    @param start_date - the start date of the booking
    @param end_of_rent - the end date of the booking
    @param price - the price of the booking
    @param email_from -
    """
    with open("database.json", "r") as dat:
        data = json.load(dat)
    if data["user_details"][i]["bookings"]["car_name"] == "":
        if data["user_details"][i]["name"] == "":
            tkinter.messagebox.showerror("Error", "Complete Your Profile")
        else:
            global name_1
            name_1 = e1.get()
            global make_1
            make_1 = e2.get()
            global license_1
            license_1 = e3.get()
            global rate_1
            rate_1 = e5.get()
            global duration_t
            duration_t = durations.get()
            name_customer = data["user_details"][i]["name"]
            end_of_rent = start_date + datetime.timedelta(days=int(duration_t))
            data["user_details"][i]["bookings"]["car_name"] = name_1
            data["user_details"][i]["bookings"]["make"] = make_1
            data["user_details"][i]["bookings"]["license"] = license_1
            data["user_details"][i]["bookings"]["rph"] = rate_1
            data["user_details"][i]["bookings"]["duration"] = duration_t
            data["user_details"][i]["bookings"]["price"] = int(duration_t) * int(rate_1)
            price = int(duration_t) * int(rate_1)
            inde = 0
            for remove_cars in data["cars"]:
                if remove_cars["name"] == name_1:
                    data["cars_in_use"].append(data["cars"].pop(inde))
                inde += 1
            with open("database.json", "w") as dat:
                json.dump(data, dat)

            tkinter.messagebox.showinfo("Booking Confirmed", "View your order from the Current Bookings Tab")
            message = f"\n\nCONGRATULATIONS!!!!\tOrder Confirmed\nOrder Details\nCustomer Name:\t{name_customer}\nCar Name:\t{name_1}\nMake:\t{make_1}\nLicense:\t{license_1}\nRate per Day:\t{rate_1}\nDuration:\t{duration_t} days\nStart Date:\t{start_date}\nReturn Date:\t{end_of_rent}\nTotal Cost:\t{price} PKR\n"
            email_to = data["user_details"][i]["email"]
            try:
                print("Connecting...........")
                TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                TIE_server.starttls(context=simple_email_context)
                TIE_server.login(email_from, pswd)
                print("Connected to Server.....")

                print()
                print(f"Sending Email to-{email_to}")
                TIE_server.sendmail(email_from, email_to, message)
                print(f"Sended Email to-{email_to}")
            except Exception as e:
                print(e)
    else:
        tkinter.messagebox.showerror("Error", "Booking Limit reached")


def current_booking(window):
    add_bill_window = Tk()
    """
    The main window for the car rental system. This window will be used to add a bill to the system.
    @param add_bill_window - the main window for the car rental system.
    """
    add_bill_window.geometry("470x720")
    add_bill_window.configure(bg="#b4edd2")
    add_bill_window.title("Car Receipt")
    l = open("database.json")
    data_current_booking = json.load(l)
    name_1 = data_current_booking["user_details"][i]["bookings"]["car_name"]
    make_1 = data_current_booking["user_details"][i]["bookings"]["make"]
    license_1 = data_current_booking["user_details"][i]["bookings"]["license"]
    duration_t = data_current_booking["user_details"][i]["bookings"]["duration"]
    rate_1 = data_current_booking["user_details"][i]["bookings"]["rph"]
    user_name_1 = data_current_booking["user_details"][i]["user_name"]
    end_date = start_date + datetime.timedelta(days=int(duration_t))
    headlabel_main = Label(add_bill_window, text="CAR RENTAL SYSTEM", font=("helvetica", 30), bg='#2c9373', fg='white',
                           borderwidth=15, relief=RIDGE)
    headlabel = Label(add_bill_window, text="Car Receipt", fg='RED', font=("helvetica", 20))
    text = Text(add_bill_window, height=25, width=50, padx=10, pady=20)
    """
    Create a text box with the user's information.
    @param add_bill_window - the window that the text box is in.
    @param user_name_1 - the user's name.
    @param name_1 - the car's name.
    @param make_1 - the car's make.
    @param license_1 - the car's license.
    @param rate_1 - the car's rate per hour.
    @param duration_t - the car's duration.
    @param start_date - the car's start date.
    @param end_date - the car's end date.
    @returns the text box
    """
    text.insert(INSERT, f"User Name      : {user_name_1}\n\n")
    text.insert(INSERT, f"Car Name       : {name_1}\n\n")
    text.insert(INSERT, f"Model          : {make_1}\n\n")
    text.insert(INSERT, f"License        : {license_1}\n\n")
    text.insert(INSERT, f"Rate per Hour  : {rate_1}\n\n")
    text.insert(INSERT, f"Price          : {int(duration_t) * int(rate_1)}\n\n")
    text.insert(INSERT, f"Duration       : {duration_t}\n\n")
    text.insert(INSERT, f"Date of Order  : {start_date}\n\n")
    text.insert(INSERT, f"Date of Return : {end_date}\n\n\n")
    text.insert(INSERT, "Thank you for your purchase!\n\n")
    headlabel.grid(row=10, column=0, columnspan=2, pady=15)
    headlabel_main.grid(row=5, column=0, columnspan=2)
    headlabel_main.configure(pady=10)
    text.grid(row=12, column=0, columnspan=2, padx=10, pady=10)
    btn = Button(add_bill_window, text="BACK", command=lambda: add_bill_window.destroy())
    btn.grid(row=15, column=0, padx=200)
    btn.configure(font=("Verdana", 13), bg="#2c9373", fg="white", borderwidth=10, relief=RIDGE)


def show_details(add_book_window):
    e1.config(state=NORMAL)
    """
    Reset the GUI to the default state. This is called when the user selects a new car.
    @param e1 - the entry for the number of epochs to train for.
    @param e2 - the entry for the learning rate.
    @param e3 - the entry for the batch size.
    @param e5 - the entry for the number of hidden layers.
    @param car_chosen - the car that the user selected.
    """
    e2.config(state=NORMAL)
    e3.config(state=NORMAL)
    e5.config(state=NORMAL)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e5.delete(0, END)
    car_chosen = dd_cars.get()
    x = open("database.json")
    """
    When a car is selected from the list of cars, this function will fill in the fields with the car's information.
    @param car_chosen - the car chosen from the list of cars
    """
    data_edit_cars = json.load(x)
    for is_there in data_edit_cars["cars"]:
        if (is_there["name"] == car_chosen):
            e1.insert(0, car_chosen)
            e2.insert(0, is_there["make"])
            e3.insert(0, is_there["license_plate"])
            l4.config(text=is_there["description"])
            e5.insert(0, is_there["rph"])
            global img2
            img2 = ImageTk.PhotoImage(Image.open(is_there["link"]))
            canvas.config(image=img2)
            break
    e1.config(state=DISABLED)
    e2.config(state=DISABLED)
    e3.config(state=DISABLED)
    e5.config(state=DISABLED)


def add_personal(window):
    """
    This function is used to add personal information to the database. It is called when the user clicks on the "Add Personal Information" button.
    @param window - the window that is being destroyed.
    """
    """
    This function is used to add personal information to the database. It is called when the user clicks on the "Add Personal Information" button.
    @param window - the window that is being destroyed.
    """
    window.destroy()
    edit_details = Tk()

    edit_details.geometry("1920x1080")
    edit_details.configure(bg="#cddafd")

    edit_details.title("Personal Information")

    Label(edit_details, text='EDIT PROFILE', font=('Verdana', 50), bg="#003049", fg="white", padx=20, pady=20,
          relief=RIDGE, borderwidth=10).pack(pady=50)

    x = open("database.json")
    data_edit_details = json.load(x)

    name_user = data_edit_details["user_details"][i]["name"]
    age_user = data_edit_details["user_details"][i]["age"]
    gender_user = data_edit_details["user_details"][i]["gender"]
    email_user = data_edit_details["user_details"][i]["email"]
    phone_user = data_edit_details["user_details"][i]["phone"]
    Label(edit_details, text="Name:", font=('Verdana', 20), bg="#dad7cd", borderwidth=5, relief=SUNKEN).place(x=450,
                                                                                                              y=250)

    global name_entry
    name_entry = Entry(edit_details, width=20, font=('Verdana', 20), bg="#dad7cd")
    name_entry.place(x=730, y=250)
    name_entry.insert(0, name_user)
    global age_entry
    # Create age label and entry
    Label(edit_details, text="Age:", font=('Verdana', 20), bg="#dad7cd", borderwidth=5, relief=SUNKEN).place(x=450,
                                                                                                             y=310)
    age_entry = Entry(edit_details, width=20, font=('Verdana', 20), bg="#dad7cd")
    age_entry.place(x=730, y=310)
    age_entry.insert(0, age_user)

    # Create gender label and option menu
    global gender_var
    Label(edit_details, text="Gender:", font=('Verdana', 20), bg="#dad7cd", borderwidth=5, relief=SUNKEN).place(x=450,
                                                                                                                y=370)

    gender_var = StringVar(edit_details)
    gender_option = OptionMenu(edit_details, gender_var, "Male", "Female", "Other")
    gender_option.configure(font=('Verdana', 19), bg="#dad7cd")
    gender_option.place(x=730, y=367)
    gender_var.set(gender_user)
    # Create email label and entry
    global email_entry
    Label(edit_details, text="Email:", font=('Verdana', 20), bg="#dad7cd", borderwidth=5, relief=SUNKEN).place(x=450,
                                                                                                               y=430)
    email_entry = Entry(edit_details, width=20, font=('Verdana', 20), bg="#dad7cd")
    email_entry.place(x=730, y=430)
    email_entry.insert(0, email_user)

    # Create phone number label and entry
    global phone_entry
    Label(edit_details, text="Phone Number:", font=('Verdana', 20), bg="#dad7cd", borderwidth=5, relief=SUNKEN).place(
        x=450, y=490)
    phone_entry = Entry(edit_details, width=20, font=('Verdana', 20), bg="#dad7cd")
    phone_entry.place(x=730, y=495)
    phone_entry.insert(0, phone_user)
    # Create submit function

    # assigning the details to
    # Create submit button
    submit_button = Button(edit_details, text="Update Profile", bg="#003049", fg="white", font=('Verdana', 18),
                           relief=RIDGE, borderwidth=5,
                           command=lambda: on_submit())
    submit_button.place(x=670, y=600)

    back_button = Button(edit_details, text="Back", bg="#003049", fg="white", font=('Verdana', 18),
                         command=lambda: on_back(edit_details))
    back_button.place(x=0, y=0)


def on_submit():
    """
    When the submit button is pressed, the user's details are saved in the database.json file.
    @param name_user - the user's name           
    @param age - the user's age           
    @param gender - the user's gender           
    @param email - the user's email           
    @param phone - the user's phone           
    """
    z = open("database.json")
    with open("database.json", "r") as z:
        data = json.load(z)
    name_user = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    if name_user.isalpha() and age.isnumeric() and age.isnumeric() and email.find("@") != -1:
        data["user_details"][i]["name"] = name_user
        data["user_details"][i]["age"] = age
        data["user_details"][i]["gender"] = gender
        data["user_details"][i]["email"] = email
        data["user_details"][i]["phone"] = phone
        tkinter.messagebox.showinfo("Success", "Your Details Saved Successfully")
    else:
        tkinter.messagebox.showerror("Error", "Enter Data In Correct Format")
    with open("database.json", "w") as z:
        json.dump(data, z)


# Create back function

def on_back(edit_details):
    """
    When the user clicks the back button, destroy the current window and open the user window.
    @param edit_details - the current window
    """
    edit_details.destroy()
    user_window()


def user_logout(window):
    """
    When the user logs out, destroy the window and open the main.py file.
    @param window - the window to be destroyed.
    """
    window.destroy()
    os.system('python main.py')
