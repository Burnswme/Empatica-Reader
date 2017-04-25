"""This is the main GUI. It houses the buttons to access the other features of the program.
   From this GUI, the user can load data into the database, view the data in the database,
   or log in to the expert GUI and set the baselines or thresholds."""
#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import loadusrdata
import ExpertGUI
import UserGUI

# This variable will allow the user to remain logged in to the expert GUI
# 0 means the user is not logged in, anything else means they are logged in
loggedIn = 0

# Set up the main window
def main():
    root = Tk()

    root.geometry('450x150+75+75')

    root.title("Empatica Reader")

# This the the button to log in to the expert GUI
# The function passes the username and password variables to adminLogin
    global loggedIn

    loginButton = ttk.Button(root, text = "Login as admin",command = lambda: adminLogin())
    loginButton.place(relx = 1, x = -10, y = 10, rely = 0, anchor = 'ne')

# This is the button to load data into the database
    load = ttk.Button(root, text = "Input data", command = loaddata)
    load.place(relx = .5, rely = .5, anchor = 's')

# This is the button to see the data in the database
    input = ttk.Button(root, text = "See Your Data", command = loadUsrGUI)
    input.place(relx = .5, rely = 1, anchor = 's')

    root.mainloop()

# This function opens the user GUI
def loadUsrGUI():
    usr = UserGUI.UsrGUI('ACC')

# This function opens the login window to access the expert GUI
def adminLogin():
    global loggedIn
    if(loggedIn == 0):
        loginWindow = LogInTk()
    else:
        exp = loginAlt()



# This function loads data into the database
def loaddata():
    loadGUI = loadusrdata.loadDataGUI()

def login(loginWindow):
    usrid = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()
    if (usrid == 'hello' and pwd == 'world'):
        setLoggedIn()
        expGUI = ExpertGUI.ExpertGUI()
    else :
        messagebox.showinfo(title = 'Error', message = 'wrong login')
def loginAlt():
    expGUI = ExpertGUI.ExpertGUI()
def setLoggedIn():
    global loggedIn
    loggedIn = 1

#login popup for admin
class LogInTk():

    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x80+300+300')
        self.win.title("Admin Login")
        self.win.bind('<Return>',self.getData)

        self.usrId = ""
        self.pwd = ""

        self.usrIdLbl = ttk.Label(self.win, text='User ID')
        self.pwdLbl = ttk.Label(self.win, text='Password')
        self.usrIdEntry = ttk.Entry(self.win, width=20)
        self.pwdEntry = ttk.Entry(self.win, width=20, show = '*')
        self.submit = ttk.Button(self.win, text="Submit", command = lambda: self.getData('a'))

        self.setFields()


    def setFields(self):
        self.usrIdLbl.grid(row = 1, column = 1)
        self.pwdLbl.grid(row = 2, column = 1)

        self.usrIdEntry.grid(row = 1, column = 2)
        self.pwdEntry.grid(row = 2, column = 2)

        self.submit.grid(row = 3, column = 2)


    def getData(self,a):
        self.usrId = self.usrIdEntry.get()
        self.pwd = self.pwdEntry.get()
        login(self)


    def getUsrId(self):
        return self.usrId
    def getPwd(self):
        #clear the window after login
        self.win.destroy()
        return self.pwd


main()