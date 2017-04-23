#import tkinter and pymysql for database interaction
from tkinter import *
import pymysql
import datetime
from PIL import Image, ImageTk


class UsrGUI():
    DAY = 86400
    HOUR = 3600
    OFFSET = 3600*4

    # database connection
    connection = pymysql.connect(host='localhost',
                                      user='root',
                                      password='pswd',
                                      db='empaticareader')

    cursor = connection.cursor()

    # pull most recent date to start from
    com = 'SELECT max(date) from data'
    cursor.execute(com)
    pull = cursor.fetchone()
    startdate = int(pull[0])
    #set recdate to one week ago from the most recent date
    recdate = startdate - startdate % DAY
    recdate = recdate - 518400
    ti = recdate - OFFSET
    # get data form baselines file then store in variables for clarity
    baselines = open('baselines.txt', 'r').read().split('\n')
    # baselines
    arrbase = float(baselines[0])
    accbase = float(baselines[1])
    hrbase = float(baselines[2])
    # thresholds
    arrthresh = float(baselines[3])
    accthresh = float(baselines[4])
    hrthresh = float(baselines[5])
    # if display alert
    arrdis = float(baselines[6])
    accdis = float(baselines[7])
    hrdis = float(baselines[8])
    # image paths
    arrimg = baselines[9]
    accimg = baselines[10]
    hrimg = baselines[11]

    # set in setcolor method, used in setalert
    ACC = 0
    HR = 0
    EDA = 0

    # holds all our images and colors if they need to be on the label
    image = [[0 for x in range(24)]for y in range(7)]
    color = [[0 for x in range(24)]for y in range(7)]

    # holds width for all labels
    w = 5

    def __init__(self, metric):

        self.metric = metric

        self.rootu = Toplevel()
        self.rootu.geometry('1200x600')

        self.rootu.title('Empatica Reader')

# creates canvas to display data
        self.daysCanvas = Canvas(self.rootu, width = 500, height = 600, bg = 'red')
        self.daysCanvas.grid(row=1, column=0, rowspan=7, columnspan = 25, stick = 'nsew')

        self.dayLbl = Label(self.rootu, width = self.w, text = 'Day').grid(row = 0, column = 0)

# buttons to select which metric is displayed
        self.selhr = Button(self.rootu, text = 'Heart rate', command = self.sethrdisplay).grid(row = 0,column = 26)
        self.selacc = Button(self.rootu, text = 'Activity (default)', command = self.setaccdisplay).grid(row = 1,column = 26)
        self.seleda = Button(self.rootu, text = 'Arousal', command = self.setedadisplay).grid(row = 2,column = 26)

# key for the colors
        self.blue = Label(self.rootu, bg = '#2B5E9F', text = 'very low reading').grid(row = 7, column = 26)
        self.lblue = Label(self.rootu, bg = '#6F9FDC', text = 'low reading').grid(row = 6, column = 26)
        self.green = Label(self.rootu, bg = '#3ED748', text = 'good reading').grid(row =5, column = 26)
        self.orange = Label(self.rootu, bg = '#F2B43A', text = 'high reading').grid(row = 4, column = 26)
        self.red = Label(self.rootu, bg = '#FF0000', text = 'very high reading').grid(row = 3, column = 26)



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
        dnum = self.recdate + 3600
        i = 0
        while i <=6:
            d = datetime.datetime.fromtimestamp(dnum).strftime('%m-%d') # convert unix timestamp into readable date
            self.datematrix[i] = Label(self.daysCanvas, text = d, width = self.w, height = self.w)\
                .grid(row = i+1, column = 0, stick = 'nsew')
            i += 1
            dnum += 86400

# hour labels for top, if statement to designate this as a block for clarity while coding
        if True:
            twelveA = Label(self.rootu, text = '12:00',width = self.w).grid(row = 0,column = 1)
            oneA = Label(self.rootu, text = '1:00',width = self.w ).grid(row = 0,column = 2)
            twoA = Label(self.rootu, text = '2:00',width = self.w ).grid(row = 0,column = 3)
            threeA = Label(self.rootu, text = '3:00',width = self.w ).grid(row = 0,column = 4)
            fourA = Label(self.rootu, text = '4:00',width = self.w ).grid(row = 0,column = 5)
            fiveA = Label(self.rootu, text = '5:00',width = self.w ).grid(row = 0,column = 6)
            sixA = Label(self.rootu, text = '6:00',width = self.w ).grid(row = 0,column = 7)
            sevenA = Label(self.rootu, text = '7:00',width = self.w ).grid(row = 0,column = 8)
            eightA = Label(self.rootu, text = '8:00',width = self.w ).grid(row = 0,column = 9)
            nineA = Label(self.rootu, text = '9:00',width = self.w ).grid(row = 0,column = 10)
            tenA = Label(self.rootu, text = '10:00',width = self.w ).grid(row = 0,column = 11)
            elevenA = Label(self.rootu, text = '11:00',width = self.w ).grid(row = 0,column = 12)
            twelveP = Label(self.rootu, text = '12:00',width = self.w ).grid(row = 0,column = 13)
            oneP = Label(self.rootu, text = '1:00',width = self.w ).grid(row = 0,column = 14)
            twoP = Label(self.rootu, text = '2:00',width = self.w ).grid(row = 0,column = 15)
            threeP = Label(self.rootu, text = '3:00',width = self.w ).grid(row = 0,column = 16)
            fourP = Label(self.rootu, text = '4:00',width = self.w ).grid(row = 0,column = 17)
            fiveP = Label(self.rootu, text = '5:00',width = self.w ).grid(row = 0,column = 18)
            sixP = Label(self.rootu, text = '6:00',width = self.w ).grid(row = 0,column = 19)
            sevenP = Label(self.rootu, text = '7:00',width = self.w ).grid(row = 0,column = 20)
            eightP = Label(self.rootu, text = '8:00',width = self.w ).grid(row = 0,column = 21)
            nineP = Label(self.rootu, text = '9:00',width = self.w ).grid(row = 0,column = 22)
            tenP = Label(self.rootu, text = '10:00',width = self.w ).grid(row = 0,column = 23)
            elevenP = Label(self.rootu, text = '11:00',width = self.w ).grid(row = 0,column = 24)

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


            # Activiy set
            if self.metric == 'ACC':
                # low holds the lower threshold, half a value of half the threshold, high holds the high threshold
                low = self.accbase - self.accbase*self.accthresh
                half = (self.accbase*self.accthresh)/2
                high = self.accbase + self.accbase*self.accthresh
            # below lower is blue(with alert)
                if self.ACC<low:
                    tcolor = '#2B5E9F'
            # from lower to half of threshold is light blue
                elif self.ACC<low+half:
                    tcolor = '#6F9FDC'
            # within half of threshold is green
                elif self.ACC<high-half:
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
                    temp = temp.resize((40, 40), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            # Heart rate set
            elif self.metric == 'HR':
                # low holds the lower threshold, half a value of half the threshold, high holds the high threshold
                low = self.hrbase - self.hrbase * self.hrthresh
                half = (self.hrbase * self.hrthresh) / 2
                high = self.hrbase + self.hrbase * self.hrthresh

                # below lower is blue(with alert)
                if self.HR < low:
                    tcolor = '#2B5E9F'
                    # from lower to half of threshold is light blue
                elif self.HR < low + half:
                    tcolor = '#6F9FDC'
                    # within half of threshold is green
                elif self.HR < high - half:
                    tcolor = '#3ED748'
                    # from half to upper is orange
                elif self.HR < high:
                    tcolor = '#F2B43A'
                    # above upper is red (with alert)
                else:
                    tcolor = '#FF0000'
                # check whether to set alert
                if (HRal == 1) and self.HR != 0:
                    temp = Image.open(self.hrimg)
                    temp = temp.resize((40, 40), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            # Arousal set
            elif self.metric == 'EDA':
                # low holds the lower threshold, half a value of half the threshold, high holds the high threshold
                low = self.arrbase - self.arrbase * self.arrthresh
                half = (self.arrbase * self.arrthresh) / 2
                high = self.arrbase + self.arrbase * self.arrthresh

                # below lower is blue(with alert)
                if self.EDA < low:
                    tcolor = '#2B5E9F'
                    # from lower to half of threshold is light blue
                elif self.EDA < low + half:
                    tcolor = '#6F9FDC'
                    # within half of threshold is green
                elif self.EDA < high - half:
                    tcolor = '#3ED748'
                    # from half to upper is orange
                elif self.EDA < high:
                    tcolor = '#F2B43A'
                    # above upper is red (with alert)
                else:
                    tcolor = '#FF0000'
                # check whether to set alert or not
                if (EDAal == 1) and self.EDA != 0:
                    temp = Image.open(self.arrimg)
                    temp = temp.resize((40, 40), Image.ANTIALIAS)
                    self.image[x][y] = ImageTk.PhotoImage(temp)
                else:
                    self.image[x][y] = ''

            if (self.ACC == 0 and self.HR == 0 and self.EDA == 0):
                tcolor = 'gray'

        else:
            tcolor = 'gray'
        self.color[x][y] = tcolor
