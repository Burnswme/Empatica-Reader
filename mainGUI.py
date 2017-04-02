# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import loadusrdata
import ExpertGUI
import UserGUI

def main():
# creates base window, sizes it and gives it a title
    root = Tk()
    root.geometry('1000x600+25+25')
    root.title("Empatica Reader")
    
# button to log in and view expert GUI to make changes
    loginButton = ttk.Button(root, text = "Login as admin",command = adminLogin)
    loginButton.place(relx = 1, x = -10, y = 10, rely = 0, anchor = 'ne')

# button to load data to database
    load = ttk.Button(root, text = "input data", command = loaddata)
    load.place(relx = .5, rely = .5, anchor = 's')

# button to diplay user data grid
    input = ttk.Button(root, text = "See your data", command = loadUsrGUI)
    input.place(relx = .5, rely = 1, anchor = 's')

    root.mainloop()

# method associated with input button
def loadUsrGUI():
    usr = UserGUI.UsrGUI()

# method assocciated with loginButton button, creates LogInTk object then 
def adminLogin():
    loginWindow = LogInTk()

# method associated with load button
def loaddata():
    loadGUI = loadusrdata.loadDataGUI()

# method that recieves an object of lype LogInTk to check for proper credentials and then create the expertGUI object
def login(loginWindow):
    usrid = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()

    if (usrid == 'hello' and pwd == 'world'):
        ExpertGUI.ExpertGUI()
    else :
        messagebox.showinfo(title = 'Error', message = 'wrong login')

# login popup for admin login
class LogInTk():

# constructor creates the various widget then calls the setFields method to put them on the window
    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x80+300+300')
        self.win.title("Admin Login")

    # these two hole the login information entered in the entry fields
        self.usrId = ""
        self.pwd = ""

        self.usrIdLbl = ttk.Label(self.win, text='User ID')
        self.pwdLbl = ttk.Label(self.win, text='Password')
        self.usrIdEntry = ttk.Entry(self.win, width=20)
        self.pwdEntry = ttk.Entry(self.win, width=20, show = '*')
    # button to pull info from entries
        self.submit = ttk.Button(self.win, text="Submit", command = self.getData)

        self.setFields()

# sets the location of the widgets created by constructor
    def setFields(self):
        self.usrIdLbl.grid(row = 1, column = 1)
        self.pwdLbl.grid(row = 2, column = 1)

        self.usrIdEntry.grid(row = 1, column = 2)
        self.pwdEntry.grid(row = 2, column = 2)

        self.submit.grid(row = 3, column = 2)

# gets the data entered and stores in proper variable, then calls login method
    def getData(self):
        self.usrId = self.usrIdEntry.get()
        self.pwd = self.pwdEntry.get()
        login(self)

# the get methods associated with the variables usrId and pwd
    def getUsrId(self):
        return self.usrId
    def getPwd(self):
        return self.pwd

main()
