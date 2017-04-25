#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import loadusrdata
import ExpertGUI
import UserGUI
import sqlite3

# This variable will allow the user to remain logged in to the expert GUI
# 0 means the user is not logged in, anything else means they are logged in
loggedIn = 0

def main():
    root = Tk()

    root.geometry('450x150+75+75')

    root.title("Empatica Reader")

    loggedIn

    loginButton = ttk.Button(root, text = "Login as admin",command = adminLogin)
    loginButton.place(relx = 1, x = -10, y = 10, rely = 0, anchor = 'ne')

    load = ttk.Button(root, text = "input data", command = loaddata)
    load.place(relx = .5, rely = .5, anchor = 's')

    input = ttk.Button(root, text = "See Your Data", command = loadUsrGUI)
    input.place(relx = .5, rely = 1, anchor = 's')

    # database dump button
    dumpB = ttk.Button(root, text = "Clear data", command = dump)
    dumpB.place(relx = 0,rely = 0, x = 10, y = 10, anchor = 'nw')

    root.mainloop()

def loadUsrGUI():
    usr = UserGUI.UsrGUI('ACC')


def adminLogin():
    global loggedIn
    if(loggedIn == 0):
        loginWindow = LogInTk()
    else:
        exp = loginAlt()

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

def loaddata():
    loadGUI = loadusrdata.loadDataGUI()


def login(loginWindow):
    usrid = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()

    if (usrid == 'hello' and pwd == 'world'):
        expGUI = ExpertGUI.ExpertGUI()
    else :
        messagebox.showinfo(title = 'Error', message = 'wrong login')


# clears the data in the DB
def dump():
    print('dumping')
    # database connection
    connection = sqlite3.connect("empaticareader.db")

    cursor = connection.cursor()

# login popup for admin
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

# gets data from the fields
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