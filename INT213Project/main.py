from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import random
import csv
from csv import DictWriter
import os

mainWindow = Tk()
mainWindow.title('GH')

# adding background image 
bg_image = PhotoImage(file='INT213Project/hotel.png')
bg_label = Label(mainWindow, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# adding font
headingFont = Font(family='Arial Black', size=40)
lbl = Label(mainWindow, text='Grand Hotel', font=headingFont).pack()


# load data from previous record
def load_data_window():
    load_data = Toplevel()
    load_data.geometry('500x300')
    load_data.title('Load')
    close_button = Button(load_data, text='Close', command=load_data.destroy)
    
    room_label = Label(master=load_data, text='Room No: ')
    room_label.grid(row=2, column=1)
    
    room = StringVar()
    room_entry = Entry(master=load_data, width=25, textvariable=room)
    room_entry.grid(row=2, column=2)
    room_entry.focus()

    def action():
        user_room = room.get()
        with open('INT213Project/file.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            counter = 0
            for row in csv_reader:
                if row[7] == user_room:
                    user_cost = row[8]
                    pop_window = Toplevel()
                    pop_window.title('Bill')
                    pop_window.geometry('500x300')
                    pop_button = Button(pop_window, text='Close', command= pop_window.destroy)
                    pop_label = Label(master=pop_window, text = f'\t\tBill is {user_cost}.', height = 10, width = 20)
                    pop_label.grid(row = 4, column = 5)
                    pop_button.grid(row = 5, column = 5)
                    counter = 1
                    break
            if counter == 0:
                pop_window = Toplevel()
                pop_window.title('Bill')
                pop_window.geometry('500x300')
                pop_label = Label(master=pop_window, text = 'Customer not found.', height = 10, width = 20)
                pop_button = Button(pop_window, text='Close', command= pop_window.destroy)
                pop_label.grid(row = 4, column = 5)
                pop_button.grid(row = 5, column = 5)

        

    submit_button = Button(master = load_data, text = 'Submit', command = action, relief = RAISED, borderwidth = 2, width = 10, height = 2)
    submit_button.grid(row = 4, column = 2)

    close_button.grid()


# inserting new data

def new_data_window():
    new_data = Toplevel()
    new_data.configure(bg=random.choice(['#d3d4cd', '#c0bfc7', '#d6c7d6']))
    new_data.geometry('500x300')
    new_data.title('New Records')
    close_button = Button(master = new_data, text='Close', command=new_data.destroy)

    # labels

    name_label = Label(master=new_data, text='Full Name: ')
    name_label.grid(row=0, column=0, sticky=W)

    age_label = Label(master=new_data, text='Age: ')
    age_label.grid(row=1, column=0, sticky=W)

    email_label = Label(master=new_data, text='Email: ')
    email_label.grid(row=2, column=0, sticky=W)

    phone_label = Label(master=new_data, text='Phone Number: ')
    phone_label.grid(row=3, column=0, sticky=W)

    address_label = Label(master=new_data, text='Address: ')
    address_label.grid(row=4, column=0, sticky=W)

    nid_label = Label(master=new_data, text='NID: ')
    nid_label.grid(row=5, column=0, sticky=W)

    number_of_person_label = Label(master=new_data, text='Number of Person: ')
    number_of_person_label.grid(row=6, column=0, sticky=W)

    # entry and getting those value

    name = StringVar()
    name_entry = Entry(master=new_data, width=25, textvariable=name)
    name_entry.grid(row=0, column=1)
    name_entry.focus()

    age = IntVar()
    age.set('')
    age_entry = Entry(master=new_data, width=25, textvariable=age)
    age_entry.grid(row=1, column=1)

    email = StringVar()
    email_entry = Entry(master=new_data, width=25, textvariable=email)
    email_entry.grid(row=2, column=1)

    phone_number = StringVar()
    phone_entry = Entry(master=new_data, width=25, textvariable=phone_number)
    phone_entry.grid(row=3, column=1)

    address_val = StringVar()
    address_entry = Entry(master=new_data, width=25, textvariable=address_val)
    address_entry.grid(row=4, column=1)

    nid_number = StringVar()
    nid_entry = Entry(master=new_data, width=25, textvariable=nid_number)
    nid_entry.grid(row=5, column=1)

    person_number = IntVar()
    person_number.set('')
    person_number_entry = Entry(master=new_data, width=12, textvariable=person_number)
    person_number_entry.grid(row=6, column=1)

    floor_num = StringVar()
    floor_label = Label(new_data, text='Floor: ')
    floor_label.grid(row=8, column=0, sticky=W)

    floor_box = ttk.Combobox(new_data, width=10, textvariable=floor_num, state='readonly')
    floor_box['values'] = ('A', 'B', 'C', 'D', 'E', 'F')
    floor_box.current(0)
    floor_box.grid(row=8, column=1)

    room_num = StringVar()
    room_label = Label(master=new_data, text='Room: ')
    room_label.grid(row=8, column=2)

    room_box = ttk.Combobox(new_data, width=10, textvariable=room_num, state='readonly')
    room_box['values'] = (
        '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
        '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
        '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
        '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
        '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
        '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
        '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
        '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'
    )
    room_box.current(0)
    room_box.grid(row=8, column=3)

    gender = StringVar()
    radio_button1 = Radiobutton(new_data, text='Male', value='Male', variable=gender)
    radio_button1.grid(row=9, column=0)
    radio_button2 = Radiobutton(new_data, text='Female', value='Female', variable=gender)
    radio_button2.grid(row=9, column=1)

    def action():
        user_name = name.get()
        user_age = age.get()
        user_email = email.get()
        user_gender = gender.get()
        user_address = address_val.get()
        user_phnumber = phone_number.get()
        user_nid = nid_number.get()
        user_number = person_number.get()
        user_floor_no = floor_num.get() + '-' + room_num.get()
        user_cost = '$' + str(user_number * 10)

        with open('INT213Project/file.csv','a', newline = '') as file:
            dict_writer = DictWriter(file, fieldnames = ['Name', 'Age', 'Email', 'Gender', 'Phone','Address','NID','Room No', 'Bill'])
            if os.stat('INT213Project/file.csv').st_size == 0:
                dict_writer.writeheader()
            dict_writer.writerow({
                'Name': user_name,
                'Age': user_age,
                'Email': user_email,
                'Gender': user_gender,
                'Phone': user_phnumber,
                'Address': user_address,
                'NID': user_nid,
                'Room No': user_floor_no,
                'Bill': user_cost
            })
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
        nid_entry.delete(0,END)
        room_box.delete(0, END)
        phone_entry.delete(0, END)
        person_number_entry.delete(0, END)
        
        print(' Data Updated '.center(20,'='))

    submit_button = Button(master = new_data, text = 'Submit', command = action, relief = RAISED, borderwidth = 2, width = 10, height = 2)
    submit_button.grid(row = 12, column = 2)
    close_button.grid(row = 12, column = 0)
    new_data.mainloop()


font_for_button = Font(family='Helvetica', size=10, weight='bold')

# new data button
button1 = Button(mainWindow, text='New Entry', command=new_data_window, width=25, height=8, relief=RAISED, borderwidth=5,
                 fg='black', bg='#B6AEAE', font=font_for_button)
button1.pack()

# load button
button2 = Button(mainWindow, text='Old Record', command=load_data_window, width=25, height=8, relief=RAISED, borderwidth=5,
                 fg='black', bg='#B6AEAE', font=font_for_button)
button2.pack()

mainWindow.geometry('700x500')
mainWindow.mainloop()
