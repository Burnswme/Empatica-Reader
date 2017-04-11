#import tkinter and pymysql for database interaction
from tkinter import *
import pymysql
import datetime


class UsrGUI():
    DAY = 86400
    HOUR = 3600

    # database connection
    connection = pymysql.connect(host='localhost',
                                      user='root',
                                      password='',
                                      db='empaticareader')

    cursor = connection.cursor()

    # pull most recent date to start from
    com = 'SELECT max(date) from Data'
    cursor.execute(com)
    recdate = cursor.fetchone()
    startdate = (recdate(0))
    recdate = recdate(0) - recdate(0) % DAY
    recdate = recdate - 604800

    def __init__(self):

        self.rootu = Tk()
        self.rootu.geometry('1200x600')

        self.rootu.title('Empatica Reader')

# creates canvas to display data
        self.daysCanvas = Canvas(self.rootu, width = 500, height = 600, bg = 'red')
        self.daysCanvas.grid(row=1, column=0, rowspan=7, columnspan = 25, stick = 'nsew')

        self.dayLbl = Label(self.rootu, width = 8, text = 'Day').grid(row = 0, column = 0)


# colored hour labels for canvas
        self.displayMatrix = [[0 for x in range(24)]for y in range(7)]

        i = 0
        while i <= 6:
            j = 0
            while j<=23:
                self.displayMatrix[i][j] = Label(self.daysCanvas, height = 5, width = 5 , bg = self.setColor(i,j),relief = RIDGE).grid(row = i+1,column =j+1)
                j+=1
            i+=1


# date labels on left side
        self.datematrix = [0 for x in range(7)]

        i = 0
        while i <=6:
            d = datetime.datetime.fromtimestamp(self.recdate).strftime('%m-%d') #convert unix timestamp into readable date
            self.datematrix[i] = Label(self.daysCanvas, text = d).grid(row = i+1, column = 0, stick = 'nsew')
            i+=1
            self.recdate+=86400

# hour labels for top
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

# to set the color of a given hour block of a day
    def setColor(self, d, h):
        # set unix timestamp from day/hour
        time = self.startdate + d*self.DAY + h*self.HOUR
        # pull necessary data
        com = ('SELECT (ACC, HR, EDA) from Data WHERE date ='+str(time))
        self.cursor.exectue(com)

        datatuple = self.cursor.fetchone()
        ACC = datatuple(0)
        HR = datatuple(1)
        EDA = datatuple(2)
