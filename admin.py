import tkinter as tk
import json
from user import idxe
def admin():
# creating the main window
    p=open("database.json")
    data=json.load(p)
    root = tk.Tk()


    # setting the title of the main window
    root.title('Car Rental System - Admin Page')

    # setting the geometry of the main window
    root.geometry('1920x1080')

    # creating the frames in the main window

    TOP_frame = tk.Frame(root, bg='white',
                        relief=tk.RIDGE, borderwidth=10)

    # packing the frames in the main window
    TOP_frame.pack(side=tk.TOP, fill=tk.BOTH,
                    expand=True)

    # for display cars in use
    heading = tk.Label(TOP_frame, text='Cars In Use',
                    font=('Verdana', 15))

    heading.pack(pady=10)
    global list_box
    # creating a Listbox
    list_box = tk.Listbox(TOP_frame, width=50, height=30,font=("Verdana",15))

    # inserting values in the Listbox
    j=1
    for cars in data["cars_in_use"]:
        list_box.insert(j,cars["name"])
        j+=1
    # packing the Listbox
    list_box.pack(padx=5, pady=5)
    # creating the delete button
    delete_btn = tk.Button(TOP_frame, text='Delete Car',padx=10, command=lambda : move_to_available())
    # packing the delete button
    delete_btn.pack(pady=10)

    # running the main window
    root.mainloop()
def move_to_available():
    with open("database.json", "r") as f:
        data1 = json.load(f)
    for i in list_box.curselection():
        value = list_box.get(i)
        list_box.delete(i)
        break
    print(value)
    indie = 0
    for cars in data1["cars_in_use"]:
        if cars["name"] == value:
            break
        indie+=1
    data1["cars"].append(data1["cars_in_use"].pop(indie))
    data1["user_details"][i]["bookings"] = {"car_name":""}
    with open("database.json", "w") as f:
        json.dump(data1, f)

