from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import pymysql

class loadDataGUI():
    def __init__(self):
        self.datawin = Tk()

        self.datawin.title('Empatica Reader')

        self.loadButton = ttk.Button(self.datawin, text = 'choose file for upload',command = self.open).place(relx = .5, rely = .5, anchor = "center")

        self.fin = ttk.Button(self.datawin, text = 'done', command = self.close).place(relx = .5, rely = .8, anchor = "center")

        
        self.datawin.mainloop()
        
    def close(self):
        self.datawin.destroy()

    def open(self):
        self.path = filedialog.askdirectory()
        self.activity = open(self.path + "/ACC.csv")
        self.heartRate = open(self.path + "/HR.csv")
        self.arousal = open(self.path + "/EDA.csv")

        accarr = self.activity.read().split("\n")
        hrarr = self.heartRate.read().split("\n")
        arousalarr = self.arousal.read().split("\n")
        
        dbavger(hrarr)
        dbavger(arousalarr)

    def commitdb(self, ar, str):
        # commits data to data base
        connection = pymysql.connect(host = 'localhost',
                                      user = 'a',
                                      password = 'a',
                                      db = 'EmpaticaReader')

        cursor = connection.cursor()

        i=0

        while(i<24):
            com = 'INSERT into Data('+str+') VALUES '+ar[i]
            cursor.execute(com)
            i = i+1
def dbavger(self,ary = []):
    self.sampleRate = ary[1]
    self.arrayIndex = 3
    self.counter = 24
    self.returnVal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.type = ""
    self.sum = 0
    self.divisor = 1
    self.average = 0
    self.hours = 0

    if(self.sampleRate == 1):
        self.type = "HR"
        self.counter = 360
        self.divisor = 360
    elif(self.sampleRate == 4):
        self.type = "EDA"
        self.counter = 1440
        self.divisor = 1440
    while(self.hours < 24): #outer loop counts up from 0 to 23

        while(self.counter > 0): #inner loop counts down from counter to 0
            self.sum += ary(self.arrayIndex)    #array index increments by ten so only a tenth
            self.arrayIndex += 10               #of the values are collected
            self.counter -= 1
        self.average = self.sum/self.divisor
        self.returnVal[self.hours] = self.average
        self.counter = self.divisor
        self.hours -= 1



    commitdb(self.returnVal,self.type)            
