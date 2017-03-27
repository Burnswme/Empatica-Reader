#import tkinter
from tkinter import *
from tkinter import ttk


def main():
    root = Tk()

    root.geometry('860x600+25+25')

    root.title("Empatica Reader")

    loginButton = ttk.Button(root, text = "Login as admin",command = adminLogin)
    loginButton.place(relx = 1, x = -10, y = 10, rely = 0, anchor = 'ne')

    greeting = ttk.Label(root, text = "input data")
    greeting.place(relx = .5, rely = .5, anchor = 's')

    input = ttk.Button(root, text = "Input")
    input.pack(side = BOTTOM)





    #for future
    mon = Label(root, text="Monday")
    tue = Label(root, text="Tuesday")
    wed = Label(root, text="Wednesday")
    thu = Label(root, text="Thursday")
    fri = Label(root, text="Friday")
    sat = Label(root, text="Saturday")
    sun = Label(root, text="Sunday")

    root.mainloop()


def adminLogin():
    #print "didit"
    loginWindow = LogInTk()

    id = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()

    print id+" "+pwd

class LogInTk:


    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x80+300+300')
        self.win.title("Admin Login")

        self.usrId = ""
        self.pwd = ""

        self.usrIdLbl = ttk.Label(self.win, text='User ID')
        self.pwdLbl = ttk.Label(self.win, text='Password')
        self.usrIdEntry = ttk.Entry(self.win, width=20)
        self.pwdEntry = ttk.Entry(self.win, width=20)
        self.submit = ttk.Button(self.win, text="Submit", command = self.getData)

        self.setFields()


    def setFields(self):
        #usrIdLbl = ttk.Label(self.win, text = 'User ID')
        self.usrIdLbl.grid(row = 1, column = 1)
        #pwdLbl = ttk.Label(self.win, text = 'Password')
        self.pwdLbl.grid(row = 2, column = 1)

        #usrIdEntry = ttk.Entry(self.win, width = 20)
        self.usrIdEntry.grid(row = 1, column = 2)
        #pwdEntry = ttk.Entry(self.win, width = 20)
        self.pwdEntry.grid(row = 2, column = 2)

        #submit = ttk.Button(self.win, text = "Submit")
        self.submit.grid(row = 3, column = 2)


    def getData(self):
        self.usrId = self.usrIdEntry.get()
        self.pwd = self.pwdEntry.get()


    def getUsrId(self):
        return self.usrId
    def getPwd(self):
        return self.pwd


main()