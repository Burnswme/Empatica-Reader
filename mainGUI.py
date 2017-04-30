"""This is the main GUI. It houses the buttons to access the other features of the program.
   From this GUI, the user can load data into the database, view the data in the database,
   or log in to the expert GUI and set the baselines or thresholds."""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import loadusrdata
import ExpertGUI
import UserGUI
import sqlite3

# This global variable will allow the user to remain logged in to the expert GUI
# 0 means the user is not logged in, anything else means they are logged in
loggedIn = 0

# Set up the main window
def main():
    global loggedIn

    root = Tk()
    root.geometry('450x150+75+75')
    root.title("Empatica Reader")

    # This the the button to log in to the expert GUI
    # The function passes the username and password variables to adminLogin
    loginButton = ttk.Button(root, text="Login as admin", command=lambda: adminLogin())
    loginButton.place(relx=1, x=-10, y=10, rely=0, anchor='ne')

    # This is the button to load data into the database
    load = ttk.Button(root, text="Input data", command=loaddata)
    load.place(relx=.5, rely=.5, anchor='s')

    # This is the button to see the data in the database
    input = ttk.Button(root, text="See Your Data", command=loadUsrGUI)
    input.place(relx=.5, rely=1, anchor='s')

    # database dump button
    dumpB = ttk.Button(root, text="Clear data", command=dump)
    dumpB.place(relx=0, rely=0, x=10, y=10, anchor='nw')

    root.mainloop()

# This function opens the user GUI when button is pressed, passing HR by default
def loadUsrGUI():
    usr = UserGUI.UsrGUI('HR')


# This function opens the login window to access the expert GUI
# will check the global loggedIn to see if login window needs to be run
def adminLogin():
    global loggedIn
    if (loggedIn == 0):
        loginWindow = LogInTk()
    else:
        exp = loginAlt()


# This function loads data into the database, by creating a loadusrdata object
def loaddata():
    loadGUI = loadusrdata.loadDataGUI()

# this is the function that pulls the data from the fields and checks if it is correct
def login(loginWindow):
    usrid = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()
    if (usrid == 'mercado' and pwd == 'cmpeics'):
        setLoggedIn()
        expGUI = ExpertGUI.ExpertGUI()
    else:
        messagebox.showinfo(title='Error', message='wrong login')

# this is the alternate method if loggedIn is set to 1
def loginAlt():
    expGUI = ExpertGUI.ExpertGUI()

# called on first login
def setLoggedIn():
    global loggedIn
    loggedIn = 1


# clears the data in the DB
def dump():
    print('dumping')
    # database connection
    connection = sqlite3.connect("empaticareader.db")

    cursor = connection.cursor()

    cursor.execute('select max(date) from data')
# get most recent date form db
    tup = cursor.fetchone()
    recdate = float(tup[0])

# delete any data older than 8 days
    recdate -= (604800 + 86400)
    cursor.execute('delete from data where date < '+str(recdate)+';')
    connection.commit()
    messagebox.showinfo(title='Cleared!', message='Database has been trimmed.')


# login popup for admin
class LogInTk():
    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x80+300+300')
        self.win.title("Admin Login")
# bind enter key to getdata function
        self.win.bind('<Return>', self.getData)

        self.usrId = ""
        self.pwd = ""

# password and usrid labels and entry fields
        self.usrIdLbl = ttk.Label(self.win, text='User ID')
        self.pwdLbl = ttk.Label(self.win, text='Password')
        self.usrIdEntry = ttk.Entry(self.win, width=20)
        self.pwdEntry = ttk.Entry(self.win, width=20, show='*')
# button calls getData function, passing a due to the
        self.submit = ttk.Button(self.win, text="Submit", command=lambda: self.getData('a'))

        self.setFields()
# set fields simply uses grid to put the labels, entries and buttons on the window
    def setFields(self):
        self.usrIdLbl.grid(row=1, column=1)
        self.pwdLbl.grid(row=2, column=1)

        self.usrIdEntry.grid(row=1, column=2)
        self.pwdEntry.grid(row=2, column=2)

        self.submit.grid(row=3, column=2)
# sets the variables usrid and pwd from the entry fields then calls the login function
    def getData(self, a):
        self.usrId = self.usrIdEntry.get()
        self.pwd = self.pwdEntry.get()
        login(self)
# getters used by login function to get the data held by usrid and pwd variables
    def getUsrId(self):
        return self.usrId

    def getPwd(self):
        # clear the window after login
        self.win.destroy()
        return self.pwd


main()