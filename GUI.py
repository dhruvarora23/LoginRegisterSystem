import re
import csv
import tkinter as tk

usernames = []
def Register():
    print("Register Menu")
    usernameinput = input("Enter a Username: ").lower()
    print("Password Criteria:\nMust be 8 or more characters\nMust have a lower case\nMust have a upper case\nMust contain numbers\nMust have special letters\n")
    while True:
        passwordinput = input("Enter a Password: ")
        if (len(passwordinput) <= 8):
            print("Password is too short, It must be 8 or more characters.")
        elif not re.search("[a-z]", passwordinput):
            print("Password must contain lowercase letters")
        elif not re.search("[A-Z]", passwordinput):
            print("Password must contain uppercase letters")
        elif not re.search("[0-9]", passwordinput):
            print("Password must contain numbers")
        elif not re.search("[_@$]", passwordinput):
            print("Password must contain special characters like #,@,$")
        else:
            break
    with open('Login.csv', 'r') as file:
        csv_reader = csv.reader(file)
        xyz = 0
        for row in csv_reader:

            for xyz in range(len(row)-1):
                usernames.append(f'{row[0]}')

    y = 0

    for x in range(len(usernames)):
        if usernameinput == usernames[x]:
            print("Username Already Exists\n")
            y = 1
            Register()
    if y == 0:
        with open('Login.csv', 'a') as csvfile:
             fieldnames = ['Username', 'Password']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             writer.writerow({'Username': usernameinput, 'Password': passwordinput})
             print("Registered Successfully!")

def login():
    def Need():
            with open("Login.csv", 'r') as csvfile:
                csvfile_Reader = csv.reader(csvfile)
                for row in csvfile_Reader:
                    for field in row:

                        if e2.get() in field and row[1] in e3.get():
                            print('Logged in')
                            notloggedin = False
    notloggedin = True
    while notloggedin == True:

        top = tk.Tk()
        top.geometry("400x250")
        Welcome = tk.Label(top, text = "Welcome Please Login").place(x = 30,y = 50)
        username1 = tk.Label(top, text = "Username").place(x = 30, y = 90)
        password = tk.Label(top, text = "Password").place(x = 30, y = 130)
        sbmitbtn = tk.Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue", command = Need).place(x = 30, y = 170)
        e2 = tk.Entry(top).place(x = 95, y = 90)
        e3 = tk.Entry(top).place(x = 95, y = 130)
        top.mainloop()


def main():
    r = tk.Tk()
    r.title('Start')
    r.geometry('400x150')
    button = tk.Button(r, text='Login', width=25, command = login).pack()
    button1 = tk.Button(r, text='Register', width=25, command= Register).pack()
    button2 = tk.Button(r, text='Quit', width=25, command= quit).pack()
    r.mainloop()

r = tk.Tk()
r.title('Start')
r.geometry('400x150')
button = tk.Button(r, text='Main Menu', width=25, command= (main)).pack()
r.mainloop()
