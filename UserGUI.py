"""User GUI displays the information gathered from the database in the form of a bar chart.
   In order to function properly, the user first needs to import data using the main GUI."""
#import tkinter and pymysql for database interaction
from tkinter import *
from tkinter import ttk
import sqlite3
import datetime
from PIL import Image, ImageTk


class UsrGUI():

    DAY = 86400
    HOUR = 3600
    OFFSET = 3600*4


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
    # image paths
    arrimg = ''
    accimg = ''
    hrimg = ''
    # max and min
    arrmax = 0
    arrmin = 0

    accmax = 0
    accmin = 0

    hrmax = 0
    hrmin = 0

    # set in setcolor method, used in setalert
    ACC = 0
    HR = 0
    EDA = 0

    # holds all our images and colors if they need to be on the label
    image = [[0 for x in range(24)]for y in range(7)]
    color = [[0 for x in range(24)]for y in range(7)]

    # holds width for all labels
    w = 5

    # metric is the data passed by the call to UsrGUI in the mainGUI method
    def __init__(self, metric):

        # establish the database connection
        self.connection = sqlite3.connect("empaticareader.db")

        self.cursor = self.connection.cursor()

        # pull most recent date to start from
        com = 'SELECT max(date) from data'
        self.cursor.execute(com)
        pull = self.cursor.fetchone()
        startdate = int(pull[0]) - self.OFFSET
        # set recdate to one week ago from the most recent date
        self.recdate = startdate - startdate % self.DAY
        self.recdate = self.recdate - 518400
        self.ti = self.recdate
        self.ti = self.ti - (self.ti%86400)


        self.metric = metric

        self.rootu = Toplevel()
        self.rootu.geometry('1200x625')

        self.rootu.title('Empatica Reader')

# creates canvas to display data
        self.daysCanvas = Canvas(self.rootu, width = 500, height = 600)
        self.daysCanvas.grid(row=0, column=0, rowspan=7, columnspan = 25, stick = 'nsew')

        self.dayLbl = Label(self.daysCanvas, width = self.w, text = 'Day').grid(row = 0, column = 0)

# buttons to select which metric is displayed
        self.selhr = ttk.Button(self.rootu, text = 'Heart rate (default)', command = self.sethrdisplay).grid(row = 0,column = 26)
        self.selacc = ttk.Button(self.rootu, text = 'Activity', command = self.setaccdisplay).grid(row = 1,column = 26)
        self.seleda = ttk.Button(self.rootu, text = 'Arousal', command = self.setedadisplay).grid(row = 2,column = 26)

# key for the colors
        self.blue = Label(self.rootu, bg = '#2B5E9F', text = 'very low reading').grid(row = 7, column = 26)
        self.lblue = Label(self.rootu, bg = '#6F9FDC', text = 'low reading').grid(row = 6, column = 26)
        self.green = Label(self.rootu, bg = '#3ED748', text = 'good reading').grid(row =5, column = 26)
        self.orange = Label(self.rootu, bg = '#F2B43A', text = 'high reading').grid(row = 4, column = 26)
        self.red = Label(self.rootu, bg = '#FF0000', text = 'very high reading').grid(row = 3, column = 26)

        # get data form baselines file then store in variables for clarity
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
        # image paths
        self.arrimg = self.baselines[9]
        self.accimg = self.baselines[10]
        self.hrimg = self.baselines[11]
        # max and min
        self.accmax = float(self.baselines[12])
        self.accmin = float(self.baselines[13])

        self.hrmax = float(self.baselines[14])
        self.hrmin = float(self.baselines[15])

        self.arrmax = float(self.baselines[16])
        self.arrmin = float(self.baselines[17])

# colored hour labels for canvas
        self.displayMatrix = [[0 for x in range(24)]for y in range(7)]

        i = 0
        while i <= 6:
            j = 0
            while j<=23:
                self.setColor(i,j)
                self.displayMatrix[i][j] = Label(self.daysCanvas,bg = self.color[i][j],relief = RIDGE)
                try:
                    self.displayMatrix[i][j].config(image = self.image[i][j])
                except:
                    self.displayMatrix[i][j].config(width = 5,height = 5)
                self.displayMatrix[i][j].grid(row = i+1,column =j+1,stick = 'nsew')
                j+=1
            i+=1


# date labels on left side
        self.datematrix = [0 for x in range(7)]
        dnum = self.recdate
        i = 0
        while i <=6:
            d = datetime.datetime.fromtimestamp(dnum).strftime('%m-%d') # convert unix timestamp into readable date
            self.datematrix[i] = Label(self.daysCanvas, text = d, width = self.w, height = self.w)\
                .grid(row = i+1, column = 0, stick = 'nsew')
            i += 1
            dnum += 86400

# hour labels for top, if statement to designate this as a block for clarity while coding
        if True:
            twelveA = Label(self.daysCanvas, text = '12:00',width = self.w).grid(row = 0,column = 1)
            oneA = Label(self.daysCanvas, text = '1:00',width = self.w ).grid(row = 0,column = 2)
            twoA = Label(self.daysCanvas, text = '2:00',width = self.w ).grid(row = 0,column = 3)
            threeA = Label(self.daysCanvas, text = '3:00',width = self.w ).grid(row = 0,column = 4)
            fourA = Label(self.daysCanvas, text = '4:00',width = self.w ).grid(row = 0,column = 5)
            fiveA = Label(self.daysCanvas, text = '5:00',width = self.w ).grid(row = 0,column = 6)
            sixA = Label(self.daysCanvas, text = '6:00',width = self.w ).grid(row = 0,column = 7)
            sevenA = Label(self.daysCanvas, text = '7:00',width = self.w ).grid(row = 0,column = 8)
            eightA = Label(self.daysCanvas, text = '8:00',width = self.w ).grid(row = 0,column = 9)
            nineA = Label(self.daysCanvas, text = '9:00',width = self.w ).grid(row = 0,column = 10)
            tenA = Label(self.daysCanvas, text = '10:00',width = self.w ).grid(row = 0,column = 11)
            elevenA = Label(self.daysCanvas, text = '11:00',width = self.w ).grid(row = 0,column = 12)
            twelveP = Label(self.daysCanvas, text = '12:00',width = self.w ).grid(row = 0,column = 13)
            oneP = Label(self.daysCanvas, text = '1:00',width = self.w ).grid(row = 0,column = 14)
            twoP = Label(self.daysCanvas, text = '2:00',width = self.w ).grid(row = 0,column = 15)
            threeP = Label(self.daysCanvas, text = '3:00',width = self.w ).grid(row = 0,column = 16)
            fourP = Label(self.daysCanvas, text = '4:00',width = self.w ).grid(row = 0,column = 17)
            fiveP = Label(self.daysCanvas, text = '5:00',width = self.w ).grid(row = 0,column = 18)
            sixP = Label(self.daysCanvas, text = '6:00',width = self.w ).grid(row = 0,column = 19)
            sevenP = Label(self.daysCanvas, text = '7:00',width = self.w ).grid(row = 0,column = 20)
            eightP = Label(self.daysCanvas, text = '8:00',width = self.w ).grid(row = 0,column = 21)
            nineP = Label(self.daysCanvas, text = '9:00',width = self.w ).grid(row = 0,column = 22)
            tenP = Label(self.daysCanvas, text = '10:00',width = self.w ).grid(row = 0,column = 23)
            elevenP = Label(self.daysCanvas, text = '11:00',width = self.w ).grid(row = 0,column = 24)

    # these are the separate display methods for each metric

    def sethrdisplay(self):
        self.rootu.destroy()
        UsrGUI('HR')


    def setaccdisplay(self):
        self.rootu.destroy()
        UsrGUI('ACC')


    def setedadisplay(self):
        self.rootu.destroy()
        UsrGUI('EDA')


    # to set the color of a given hour block of a day
    # x and y are integers indicating the position of the label
    def setColor(self,x,y):
        # set unix timestamp from day/hour
        work = True

        # pull necessary data
        com = ('SELECT ACC, HR, EDA, ACCalert, HRalert, EDAalert from data WHERE date = '+str(self.ti)+';')

        try:
            self.cursor.execute(com)

        except:
            work = False

        # update recdate to read through all 168 hour blocks
        self.ti += 3600
        datatuple = self.cursor.fetchone()

        # if the row exists, set the color, otherwise it will be gray
        if work and not datatuple == None:
            self.ACC = float(datatuple[0])
            self.HR = float(datatuple[1])
            self.EDA = float(datatuple[2])
            ACCal = float(datatuple[3])
            HRal = float(datatuple[4])
            EDAal = float(datatuple[5])


            # Activity set
            if self.metric == 'ACC':
                # low limits darkblue values , midd limits light blue values, high limits green values
                # we use nexthigh to limit orange values, anything over nexthigh is red
                perc = 3
                low = 87
                midd = low + perc
                high = midd + perc
                nexthigh = high + perc +perc


            # below lower is blue(with alert)
                if self.ACC<low:
                    tcolor = '#2B5E9F'
            # from lower to half of threshold is light blue
                elif self.ACC<midd:
                    tcolor = '#6F9FDC'
            # within half of threshold is green
                elif self.ACC<nexthigh:
                    tcolor = '#3ED748'
            # from half to upper is orange
                elif self.ACC<high:
                    tcolor = '#F2B43A'
            # above upper is red (with alert)
                else:
                    tcolor = '#FF0000'
                # check whether to set alert or not
                if (ACCal == 1) and self.ACC != 0:
                    temp = Image.open(self.accimg)
                    temp = temp.resize((35, 35), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            # Heart rate set
            elif self.metric == 'HR':
                # low limits darkblue values , midd limits light blue values, high limits green values
                # we use nexthigh to limit orange values, anything over nexthigh is red
                perc = (self.hrmax - self.hrmin)*.05
                low = self.hrmin + perc*2
                midd = low + perc
                high = midd + perc
                nexthigh = high + perc


                # below lower is blue(with alert)
                if self.HR < low:
                    tcolor = '#2B5E9F'
                    # from lower to half of threshold is light blue
                elif self.HR < midd:
                    tcolor = '#6F9FDC'
                    # within half of threshold is green
                elif self.HR < high:
                    tcolor = '#3ED748'
                    # from half to upper is orange
                elif self.HR < nexthigh:
                    tcolor = '#F2B43A'
                    # above upper is red (with alert)
                else:
                    tcolor = '#FF0000'
                # check whether to set alert
                if (HRal == 1) and self.HR != 0:
                    temp = Image.open(self.hrimg)
                    temp = temp.resize((35, 35), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            # Arousal set
            elif self.metric == 'EDA':
                # low limits darkblue values , midd limits light blue values, high limits green values
                # we use nexthigh to limit orange values, anything over nexthigh is red
                perc = (self.arrmax - self.arrmin)*.015
                low = self.arrmin + perc
                midd = low + perc
                high = midd + perc
                nexthigh = high + perc

                # below lower is blue(with alert)
                if self.EDA < low:
                    tcolor = '#2B5E9F'
                    # from lower to half of threshold is light blue
                elif self.EDA < midd:
                    tcolor = '#6F9FDC'
                    # within half of threshold is green
                elif self.EDA < high:
                    tcolor = '#3ED748'
                    # from half to upper is orange
                elif self.EDA < nexthigh:
                    tcolor = '#F2B43A'
                    # above upper is red (with alert)
                else:
                    tcolor = '#FF0000'
                # check whether to set alert or not
                if (EDAal == 1) and self.EDA != 0:
                    temp = Image.open(self.arrimg)
                    temp = temp.resize((35, 35), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            if (self.ACC == 0 and self.HR == 0 and self.EDA == 0):
                tcolor = 'gray'

        else:
            tcolor = 'gray'
        self.color[x][y] = tcolor