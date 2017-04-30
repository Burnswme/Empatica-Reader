from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class loadDataGUI():
    baselines = []
    # baselines
    arrbase = 0
    accbase = 0
    hrbase = 0
    # thresholds
    arrthresh = 0
    accthresh = 0
    hrthresh = 0
    # if display alert
    arrdis = 0
    accdis = 0
    hrdis = 0

    # these will hold the alert thresholds
    acclow = 0
    acchigh = 0

    hrlow = 0
    hrhigh = 0

    arrlow = 0
    arrhigh = 0

    # values to hold min and max value recorded
    accmin = 12
    accmax = 13

    hrmin = 14
    hrmax = 15

    arrmin = 16
    arrmax = 17


    def __init__(self):

        # establish db connection to be used
        self.connection = sqlite3.connect("empaticareader.db")

        self.cursor = self.connection.cursor()

        self.datawin = Tk()

        self.datawin.geometry('175x200+800+200')

        self.datawin.title('Empatica Reader')

        self.infolbl = ttk.Label(self.datawin, wraplength = 150, text = 'Select the name of the folder downloaded from the website')\
            .place(relx = .5, rely = .1, anchor = 'n')

        self.loadButton = ttk.Button(self.datawin, text='Choose folder for upload', command=self.open) \
            .place(relx=.5, rely=.5, anchor="center")

        self.fin = ttk.Button(self.datawin, text='done', command=self.close) \
            .place(relx=.5, rely=.8, anchor="center")

        self.baselines = open('baselines.txt', 'r').read().split('\n')
        # baselines
        self.arrbase = float(self.baselines[0])
        self.accbase = float(self.baselines[1])
        self.hrbase = float(self.baselines[2])
        # thresholds
        self.arrthresh = float(self.baselines[3])
        self.accthresh = float(self.baselines[4])
        self.hrthresh = float(self.baselines[5])
        # if display alert
        self.arrdis = float(self.baselines[6])
        self.accdis = float(self.baselines[7])
        self.hrdis = float(self.baselines[8])
        # threshold values calculated from percentages
        self.acclow = self.accbase - self.accbase * self.accthresh
        self.acchigh = self.accbase + self.accbase * self.accthresh

        self.hrlow = self.hrbase - self.hrbase * self.hrthresh
        self.hrhigh = self.hrbase + self.hrbase * self.hrthresh

        self.arrlow = self.arrbase - self.arrbase * self.arrthresh
        self.arrhigh = self.arrbase + self.arrbase * self.arrthresh

        # maxes and mins
        self.accmax = float(self.baselines[12])
        self.accmin = float(self.baselines[13])

        self.hrmax = float(self.baselines[14])
        self.hrmin = float(self.baselines[15])

        self.arrmax = float(self.baselines[16])
        self.arrmin = float(self.baselines[17])

        self.datawin.mainloop()

    def close(self):
        self.update()
        self.datawin.destroy()

    def open(self):
        try:
            self.path = filedialog.askdirectory()
            self.activity = open(self.path + "/ACC.csv")
            self.heartRate = open(self.path + "/HR.csv")
            self.arousal = open(self.path + "/EDA.csv")

            self.hrarr = self.heartRate.read().split("\n")
            self.accarr = self.activity.read().split("\n")
            self.arousalarr = self.arousal.read().split("\n")

            # to put timestamp to next lowest hour
            stime = int(float(self.hrarr[0])) % 3600
            stime = int(float(self.hrarr[0])) - stime


            # fills any missing dates with 0
            self.fill(self.hrarr[0])

            etime = len(self.hrarr) // 3600
            etime = etime*3600 + stime                  #number of hours in file

            while stime <= etime:
                try:
                    exe = 'INSERT INTO data (date) VALUES ('+str(stime)+');'
                    self.cursor.execute(exe)
                    self.connection.commit()
                except:
                    self.connection.rollback()

                stime += 3600

            # call the methods to compile the data from the files
            self.dbavger(self.hrarr)
            self.dbavger(self.arousalarr)
            self.accavg(self.accarr)
            messagebox.showinfo(title='Confirm', message='Uploaded!')

        except:
           messagebox.showinfo(title = 'Error', message = 'Invalid folder selected')

    # method to fill missing rows of db
    def fill(self, dat):
        # find start of file to know how much to fill
        time = int(float(dat)) % 3600
        time = int(float(dat)) - time + 3600

        # pull largest and thus most recent date from db
        self.cursor.execute('SELECT MAX(date) FROM Data')
        last = self.cursor.fetchone()
        num = int(last[0])

        i = 1
        # fill the days with no data with 0's
        while (num < time):
            try:
                stat = 'INSERT into Data (date, ACC, HR, EDA) VALUES(' + str(num) + ', 0,0,0)'
                self.cursor.execute(stat)
                self.connection.commit()
            except:
                self.connection.rollback()
            num = num + 3600

    # commits data to data base
    def commitdb(self, ar, st, al):
        i = 0

        at = st+'alert'

        # to put timestamp to next lowest hour
        time = int(float(self.hrarr[0])) % 3600
        time = int(float(self.hrarr[0])) - time + 3600


        # inserts all values from array to database
        while (i < len(ar)):
            try:
                com = 'UPDATE data SET ' + st + '=' + str(ar[i]) + ', ' + at + '= ' + str(al[i]) + ' WHERE date = ' + str(time) + ';'
                self.cursor.execute(com)
                self.connection.commit()
            except:
                self.connection.rollback()
            i = i + 1
            time = time + 3600

    def dbavger(self, ary):
        # first we pull the timestamp and sample rate from file
        timestamp = int(float(ary[0]) % 3600)
        sampleRate = int(float(ary[1]))
        arrayIndex = 3
        # then we cut partial hours
        if (timestamp > 0):
            arrayIndex = timestamp * sampleRate
        # set timestamp to first full hour of data
        timestamp = float(ary[0])+(timestamp-3600)
        counter = 0  # will hold measurements per hour, used in inner loop
        returnVal = []
        alert = []
        boo = 0   # value to be stored if an alert is to be triggered
        type = ""
        sum = 0
        divisor = 0  # will hold duplicate of counter, not changed in loop
        average = 0
        hours = 0

        # see if file is for HR or EDA
        if (sampleRate == 1):
            type = "HR"
            counter = 360
            divisor = 360
        elif (sampleRate == 4):
            type = "EDA"
            counter = 1440
            divisor = 1440

        # find the length of the file so we know when to stop, cutting any partial hours
        end = len(ary) - arrayIndex
        leftOver = end % divisor
        end = end - leftOver
        leveler = (end - arrayIndex) % 10
        end = end - leveler

        # nested loop to calculate averages for the hours in the file, outer is for whole file, inner is for each hour
        # (end - divisor *20) this makes sure the last time this loop executes is on the last hour
        while (arrayIndex <= (end - divisor * 10)):
            sum = 0
            while (counter > 0):
                sum += float(ary[arrayIndex])  # array index increments by ten to reduce number of calculations

                if self.isalert(float(ary[arrayIndex]), type):
                    boo = 1

                self.max(float(ary[arrayIndex]),type)

                arrayIndex += 10
                counter -= 1

            average = sum / divisor
            returnVal.append(average)  # store the average for this hour in the return array
            alert.append(boo)
            counter = divisor
            hours += 1

        # commit list to db
        self.commitdb(returnVal, type, alert)

    # special case averager for the ACC file, since it uses three columns and 3D measurements
    def accavg(self, acclist):
        # first we pull the timestamp and sample rate from file
        timerow = acclist[0].split(',')
        timestamp = int(float(timerow[0]) % 3600)
        samplerow = acclist[1].split(',')
        sampleRate = int(float(samplerow[1]))
        arrayIndex = 3

        # then we cut partial hours off the front
        if (timestamp > 0):
            arrayIndex = timestamp * sampleRate + 1

        # set timestamp to first full hour of data
        timestamp = float(timerow[0])+(timestamp-3600)
        counter = 115200  # holds number of measurements per hour, used in inner loop
        returnVal = []
        alert = []
        boo = 0 # value to be stored if an alert is to be triggered
        type = 'ACC'
        sum = 0
        divisor = 115200  # duplicate of counter, not changed in loop
        average = 0
        hours = 0


        # find length of file so we know when to stop, cutting any partial hours
        end = len(acclist) - arrayIndex
        leftOver = end % divisor
        end = end - leftOver
        leveler = (end - arrayIndex) % 1
        end = end - leveler

        # nested loop to calculate averages for the hours in the file, outer is for whole file, inner is for each hour
        # (end - divisor *20) this makes sure the last time this loop executes is on the last hour
        while (arrayIndex <= (end - divisor)):
            sum = 0
            while (counter > 0):
                row = acclist[arrayIndex].split(',')
                row2 = acclist[arrayIndex - 1].split(',')

                # find resultant vector from components given
                magnitude = 0
                x = abs(float(row[0]))
                y = abs(float(row[1]))
                z = abs(float(row[2]))

                """x2 = float(row2[0])
                y2 = float(row2[1])
                z2 = float(row2[2])

                xcomp = abs(x - x2)
                ycomp = abs(y - y2)
                zcomp = abs(z - z2)"""

                magnitude = (x+y+z)


                if self.isalert(magnitude, type):
                    boo = 1

                self.max(magnitude,type)

                sum += magnitude
                arrayIndex += 1  # of the values are collected
                counter -= 1
            average = sum / divisor
            returnVal.append(average)  # store the average for this hour in the return array
            alert.append(boo)
            counter = divisor
            hours += 1

        # commit list to db
        self.commitdb(returnVal, type, alert)


    # checks if this is a smallest value of not
    def max(self, p, ty):
        if ty == 'EDA':
            if p > self.arrmax:
                self.arrmax = p
            if p < self.arrmin:
                self.arrmin = p
        if ty == 'HR':
            if p > self.hrmax:
                self.hrmax = p
            if p < self.hrmin:
                self.hrmin = p
        if ty == 'ACC':
            if p > self.accmax:
                self.accmax = p
            if p < self.accmin:
                self.accmin = p


    # checks to see if an alert needs to be displayed for that hour
    def isalert(self,p,ty):
        if ty == 'EDA' and self.arrdis == 1 and (p > self.arrhigh or p < self.arrlow):
            return True
        elif ty == 'HR' and self.hrdis == 1 and (p > self.hrhigh or p < self.hrlow):
            return True
        elif ty == 'ACC' and self.accdis == 1 and (p > self.acchigh or p < self.acclow):
            return True
        else:
            return False

    # method to update baselines file
    def update(self):
        file = open("baselines.txt", 'w')

        print(self.baselines[0], file=file)
        print(self.baselines[1], file=file)
        print(self.baselines[2], file=file)
        print(self.baselines[3], file=file)
        print(self.baselines[4], file=file)
        print(self.baselines[5], file=file)
        print(self.baselines[6], file=file)
        print(self.baselines[7], file=file)
        print(self.baselines[8], file=file)
        print(self.baselines[9], file=file)
        print(self.baselines[10], file=file)
        print(self.baselines[11], file=file)
        print(self.accmax,file = file)
        print(self.accmin,file = file)
        print(self.hrmax,file = file)
        print(self.hrmin,file = file)
        print(self.arrmax,file = file)
        print(self.arrmin,file = file)

        file.close()
