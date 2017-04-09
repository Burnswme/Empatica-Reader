from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import pymysql

class loadDataGUI():
    def __init__(self):
        self.datawin = Tk()

        self.datawin.title('Empatica Reader')

        self.loadButton = ttk.Button(self.datawin, text = 'choose file for upload',command = self.open).place(relx = .5, rely = .5, anchor = "center")

        self.datawin.mainloop()

    def open(self):
        self.path = filedialog.askdirectory()
        self.activity = open(self.path + "/ACC.csv")
        self.heartRate = open(self.path + "/HR.csv")
        self.arousal = open(self.path + "/EDA.csv")

        hrarr = self.heartRate.read().split("\n")
        accarr = self.activity.read().split("\n")
        arousalarr = self.arousal.read().split("\n")

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