from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import pymysql

class loadDataGUI():
    def __init__(self):
        self.datawin = Tk()

        self.datawin.title('Empatica Reader')

        self.loadButton = ttk.Button(self.datawin, text = 'choose file for upload',command = self.open)\
            .place(relx = .5, rely = .5, anchor = "center")

        self.fin = ttk.Button(self.datawin, text = 'done', command = self.close)\
            .place(relx = .5, rely = .8, anchor = "center")

        self.datawin.mainloop()

    def close(self):
        self.datawin.destroy()

    def open(self):
        self.path = filedialog.askdirectory()
        self.activity = open(self.path + "/ACC.csv")
        self.heartRate = open(self.path + "/HR.csv")
        self.arousal = open(self.path + "/EDA.csv")

        self.hrarr = self.heartRate.read().split("\n")
        self.accarr = self.activity.read().split("\n")
        self.arousalarr = self.arousal.read().split("\n")

# establish db connection to be used
        self.connection = pymysql.connect(host = 'localhost',
                                      user = 'a',
                                      password = 'a',
                                      db = 'EmpaticaReader')

        self.cursor = self.connection.cursor()


# call the methods to compile the data from the files
        self.dbavger(self.hrarr)
        self.dbavger(self.arousalarr)

        self.fill(self.hrarr[0])

# method to fill missing rows of db
    def fill(self, dat):

# pull largest and thus most recent date from db
        self.cursor.exectute('SELECT MAX(date) FROM Data')
        last = self.cursor.fetchone()
        i = 1
# fill the days with no data with 0's
        while(dat< last):
            last = (last+3600*i)
            stat = 'INSERT into Data (date, ACC, HR, EDA) VALUES('+last+', 0,0,0)'
            self.cursor.execute(stat)


# commits data to data base
    def commitdb(self, ar, st):
        i=0


#to put timestamp to next lowest hour
        time = int(self.hrarr[0])%3600
        time = int(self.hrarr[0])-time+3600


#inserts all values from array to database
        while(i<len(ar)):
            com = 'INSERT into Data( date,'+st+') VALUES ('+time+', '+ar[i]+')'
            self.cursor.execute(com)
            i = i+1
            time = time+3600
