from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import pymysql

class loadDataGUI():
    # establish db connection to be used
    connection = pymysql.connect(host='localhost',
                                      user='root',
                                      password='',
                                      db='empaticareader')

    cursor = connection.cursor()

    # an offset to put utc time into eastern time, 4 hours
    offset = 3600*4

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



        # call the methods to compile the data from the files
        self.dbavger(self.hrarr)
        self.dbavger(self.arousalarr)

        self.fill(self.hrarr[0])

    # method to fill missing rows of db
    def fill(self, dat):

        # pull largest and thus most recent date from db
        self.cursor.exectute('SELECT MAX(date) FROM Data')
        last = self.cursor.fetchone()
        last -= last(0)-self.offset
        i = 1
        # fill the days with no data with 0's
        while(dat< last):
            last = (last+3600*i)
            stat = 'INSERT into Data (date, ACC, HR, EDA) VALUES('+str(last)+', 0,0,0)'
            self.cursor.execute(stat)


    # commits data to data base
    def commitdb(self, ar, st):
        i=0


        #to put timestamp to next lowest hour
        time = int(float(self.hrarr[0]))%3600
        time = int(float(self.hrarr[0]))-time+3600
        time = time - self.offset


        #inserts all values from array to database
        while(i<len(ar)):
            com = 'INSERT into Data( date,'+st+') VALUES ('+str(time)+', '+str(ar[i])+')'
            self.cursor.execute(com)
            i = i+1
            time = time+3600


    def dbavger(self, ary):
        timestamp = int(float(ary[0])%3600)
        sampleRate = int(float(ary[1]))
        arrayIndex = 0
        if(timestamp > 0):                                 # this is to ensure no partial hours are measured
            arrayIndex = timestamp*sampleRate    # skip ahead to the first full hour of data

        counter = 0
        returnVal = []
        type = ""
        sum = 0
        divisor = 1
        average = 0
        hours = 0

        if (sampleRate == 1):
            type = "HR"
            counter = 360           #the counter is the incoming array length, divided by the number of measurements in an hour
            divisor = 360           #divisor is used to calculate the average later
        elif (sampleRate == 4):
            type = "EDA"
            counter = 1440
            divisor = 1440

        end = len(ary) - arrayIndex  #number of valid data indexes in list
        leftOver = end % divisor
        end = end-leftOver              #end is the final index of the measured data
        leveler = (end-arrayIndex)%10   # sets the end to the last set or data that needs to be read
        end = end - leveler

        print('arrylen: '+str(len(ary))+' end: '+str(end)+' counter: '+str(counter)+' type: '+type+' array index: '+str(arrayIndex))


        while (arrayIndex <= (end-3600)):  # outer loop counts up from 0 to 23

            while (counter > 0):             # inner loop counts down from counter to 0
                sum += int(float(ary[arrayIndex]))  # array index increments by ten so only a tenth
                arrayIndex += 10             # of the values are collected
                counter -= 1
            average = sum / divisor
            returnVal.append(average)   #store the average for this hour in the return array
            counter = divisor
            hours += 1


        self.commitdb(returnVal, type)
