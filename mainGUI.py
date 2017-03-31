#import tkinter
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    root.geometry('1000x600+25+25')

    root.title("Empatica Reader")

    loginButton = ttk.Button(root, text = "Login as admin",command = adminLogin)
    loginButton.place(relx = 1, x = -10, y = 10, rely = 0, anchor = 'ne')

    greeting = ttk.Button(root, text = "input data", command = loaddata)
    greeting.place(relx = .5, rely = .5, anchor = 's')

    input = ttk.Button(root, text = "Input", command = loadUsrGUI)
    input.place(relx = .5, rely = 1, anchor = 's')

    root.mainloop()

def loadUsrGUI():
    usr = UsrGUI()


def adminLogin():
    loginWindow = LogInTk()

def loaddata():
    loadGUI = loadDataGUI()

def getLoginData(loginWindow):
    usrid = loginWindow.getUsrId()
    pwd = loginWindow.getPwd()

    print (usrid+" "+pwd)


#class expertGUI():
#    root = Tk()
#    root.geometry('800x600')
#    root.title('Empatica Reader Expert Menu')

class LogInTk():

    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x80+300+300')
        self.win.title("Admin Login")

        self.usrId = ""
        self.pwd = ""

        self.usrIdLbl = ttk.Label(self.win, text='User ID')
        self.pwdLbl = ttk.Label(self.win, text='Password')
        self.usrIdEntry = ttk.Entry(self.win, width=20)
        self.pwdEntry = ttk.Entry(self.win, width=20, show = '*')
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
        getLoginData(self)


    def getUsrId(self):
        return self.usrId
    def getPwd(self):
        return self.pwd

class UsrGUI():

    def __init__(self):
        self.rootu = Tk()
        self.rootu.geometry('1200x600')

        self.rootu.title('Empatica Reader')

        #creates canvas to display data
        self.daysCanvas = Canvas(self.rootu, width = 500, height = 600, bg = 'red')
        self.daysCanvas.grid(row=1, column=0, rowspan=7, columnspan = 25, stick = 'nsew')

        self.dayLbl = Label(self.rootu, width = 8, text = 'Day').grid(row = 0, column = 0)

        #hour labels for canvas
        self.displayMatrix = [[0 for x in range(24)]for y in range(7)]

        i = 0
        while i <= 6:
            j = 0
            while j<=23:
                self.displayMatrix[i][j] = Label(self.daysCanvas, height = 5, width = 5 , bg = self.setColor(j),relief = RIDGE).grid(row = i+1,column =j+1)
                j+=1
            i+=1


        #left side labels for days
        mon = Label(self.daysCanvas, text="Monday").grid(row = 1,column = 0, stick = 'nsew')
        tue = Label(self.daysCanvas, text="Tuesday").grid(row = 2,column = 0, stick = 'nsew')
        wed = Label(self.daysCanvas, text="Wednesday").grid(row = 3,column = 0, stick = 'nsew')
        thu = Label(self.daysCanvas, text="Thursday").grid(row = 4,column = 0, stick = 'nsew')
        fri = Label(self.daysCanvas, text="Friday").grid(row = 5,column = 0, stick = 'nsew')
        sat = Label(self.daysCanvas, text="Saturday").grid(row = 6,column = 0, stick = 'nsew')
        sun = Label(self.daysCanvas, text="Sunday").grid(row = 7,column = 0, stick = 'nsew')

        #hour labels for top

        w = 5

        twelveA = Label(self.rootu, text = '12:00',width = w).grid(row = 0,column = 1)
        oneA = Label(self.rootu, text = '1:00',width = w ).grid(row = 0,column = 2)
        twoA = Label(self.rootu, text = '2:00',width = w ).grid(row = 0,column = 3)
        threeA = Label(self.rootu, text = '3:00',width = w ).grid(row = 0,column = 4)
        fourA = Label(self.rootu, text = '4:00',width = w ).grid(row = 0,column = 5)
        fiveA = Label(self.rootu, text = '5:00',width = w ).grid(row = 0,column = 6)
        sixA = Label(self.rootu, text = '6:00',width = w ).grid(row = 0,column = 7)
        sevenA = Label(self.rootu, text = '7:00',width = w ).grid(row = 0,column = 8)
        eightA = Label(self.rootu, text = '8:00',width = w ).grid(row = 0,column = 9)
        nineA = Label(self.rootu, text = '9:00',width = w ).grid(row = 0,column = 10)
        tenA = Label(self.rootu, text = '10:00',width = w ).grid(row = 0,column = 11)
        elevenA = Label(self.rootu, text = '11:00',width = w ).grid(row = 0,column = 12)
        twelveP = Label(self.rootu, text = '12:00',width = w ).grid(row = 0,column = 13)
        oneP = Label(self.rootu, text = '1:00',width = w ).grid(row = 0,column = 14)
        twoP = Label(self.rootu, text = '2:00',width = w ).grid(row = 0,column = 15)
        threeP = Label(self.rootu, text = '3:00',width = w ).grid(row = 0,column = 16)
        fourP = Label(self.rootu, text = '4:00',width = w ).grid(row = 0,column = 17)
        fiveP = Label(self.rootu, text = '5:00',width = w ).grid(row = 0,column = 18)
        sixP = Label(self.rootu, text = '6:00',width = w ).grid(row = 0,column = 19)
        sevenP = Label(self.rootu, text = '7:00',width = w ).grid(row = 0,column = 20)
        eightP = Label(self.rootu, text = '8:00',width = w ).grid(row = 0,column = 21)
        nineP = Label(self.rootu, text = '9:00',width = w ).grid(row = 0,column = 22)
        tenP = Label(self.rootu, text = '10:00',width = w ).grid(row = 0,column = 23)
        elevenP = Label(self.rootu, text = '11:00',width = w ).grid(row = 0,column = 24)


    def setColor(self, h):
        if (h>7 and h<20):
            return 'orange'
        else:
            return 'blue'

class loadDataGUI():
    def __init__(self, folder):
        activity = open(folder + "ACC.csv")
        heartRate = open(folder + "HR.csv")
        arousal = open(folder + "EDA.csv")

main()