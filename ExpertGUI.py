"""The purpose of this program is to run the interface used by the health professional.
   It can only be accessed by logging in on the main gui page and is not intended for 
   use by the patient. Using this interface, the health professional can set baselines,
   set alert thresholds, turn on or off alert categories, and update alert images."""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
#from PIL.Image import core as _imaging
from PIL import Image, ImageTk

class ExpertGUI():
        def __init__(self):

                self.rootE = Toplevel()
                self.rootE.title("Empatica Reader Expert Menu")
                self.rootE.geometry('500x500+25+25')

                #attempt to open the baselines.txt and populate the fields with them
                try:
                        self.lines = open("baselines.txt").read().split('\n')

                        # these variables will hold the baseline values set by the expert user

                        self.arousalBaseline = self.lines[0]
                        self.activityBaseline = self.lines[1]
                        self.heartRateBaseline = self.lines[2]

                        # these variables will hold the threshold triggers set by the expert user

                        self.arousalTrigger = self.lines[3]
                        self.activityTrigger = self.lines[4]
                        self.heartRateTrigger = self.lines[5]

                        #these variables will hold the values of the checkboxes

                        self.arousalDisplay = IntVar()
                        self.arousalDisplay.set(self.lines[6])
                        self.activityDisplay = IntVar()
                        self.activityDisplay.set(self.lines[7])
                        self.heartRateDisplay = IntVar()
                        self.heartRateDisplay.set(self.lines[8])
 
                        #these variables will hold the path specifying the source image of the alerts

                        self.arousalAlert = self.lines[9]
                        self.activityAlert = self.lines[10]
                        self.heartRateAlert = self.lines[11]

                except Exception as inst:
                        #if the baselines.txt file fails to open, open the backup

                        self.lines = open("backup.txt").read().split('\n')

                        # these variables will hold the default baseline values

                        self.arousalBaseline = self.lines[0]
                        self.activityBaseline = self.lines[1]
                        self.heartRateBaseline = self.lines[2]

                        # these variables will hold the default threshold triggers

                        self.arousalTrigger = self.lines[3]
                        self.activityTrigger = self.lines[4]
                        self.heartRateTrigger = self.lines[5]

                        # these variables will hold the values of the checkboxes

                        self.arousalDisplay = IntVar()
                        self.arousalDisplay.set(self.lines[6])
                        self.activityDisplay = IntVar()
                        self.activityDisplay.set(self.lines[7])
                        self.heartRateDisplay = IntVar()
                        self.heartRateDisplay.set(self.lines[8])

                        # these variables will hold the path specifying the source image of the alerts

                        self.arousalAlert = self.lines[9]
                        self.activityAlert = self.lines[10]
                        self.heartRateAlert = self.lines[11]

                #chkBoxFrame holds the checkboxes to determine which variables to track
                self.chkBoxFrame = LabelFrame(self.rootE,text = "Select alerts to display")
                self.chkBoxFrame.grid(row=0,column=0)

                #baselineFrame holds the values of the baselines
                self.baselineFrame = LabelFrame(self.rootE,text = "Update Baselines")
                self.baselineFrame.grid(row=0,column=1)

                #thresholdFrame holds the % deviation from the baseline at which the program triggers an alert
                self.thresholdFrame = LabelFrame(self.rootE,text = "Set percentage at which to trigger alerts")
                self.thresholdFrame.grid(row=1,column=1)

                #alertFrame holds the current images used for alerts and allows the user to specify a path
                #where to find the new alerts
                self.alertFrame = LabelFrame(self.rootE,text = "Set the visual representations of the alerts")
                self.alertFrame.grid(row=1,column=0)

                #the update button takes values present in the fields, checks them against baselines.txt, and updates them
                self.updateButton = Button(self.rootE, text="Update", fg="black",command = self.update)
                self.updateButton.grid(row = 3,column = 0)

                #these are the checkboxes which set which variables to display alerts for
                self.aroChkBtn = Checkbutton(self.chkBoxFrame,text = "Arousal",variable = self.arousalDisplay, onvalue = 1,offvalue = 0,height = 5,
                                 width = 20)
                self.actChkBtn = Checkbutton(self.chkBoxFrame,text = "Activity",variable = self.activityDisplay, onvalue = 1, offvalue = 0, height = 5,
                                 width = 20)
                self.heaChkBtn = Checkbutton(self.chkBoxFrame,text = "Heart Rate",variable = self.heartRateDisplay, onvalue = 1, offvalue = 0,
                                 height = 5, width = 20)
                self.aroChkBtn.pack()
                self.actChkBtn.pack()
                self.heaChkBtn.pack()

                #these are the entry boxes for the baselines, populated automatically by the GUI
                #using the baselines present in baselines.txt

                self.aroEntry = Label(self.baselineFrame,text = "Arousal Baseline")
                self.aroEntry.pack()
                self.aroEntry = Entry(self.baselineFrame,bd = 5)
                self.aroEntry.pack()
                self.arousalBaselineString = str(self.arousalBaseline) #convert floats and ints into strings before storing in the entry box
                self.aroEntry.insert(0,self.arousalBaselineString)

                self.actEntry = Label(self.baselineFrame,text = "Activity Baseline")
                self.actEntry.pack()
                self.actEntry = Entry(self.baselineFrame,bd = 5)
                self.actEntry.pack()
                self.activityBaselineString = str(self.activityBaseline)
                self.actEntry.insert(0,self.activityBaselineString)

                self.heaEntry = Label(self.baselineFrame, text = "Heart Rate Baseline")
                self.heaEntry.pack()
                self.heaEntry = Entry(self.baselineFrame,bd = 5)
                self.heaEntry.pack()
                self.heartRateBaselineString = str(self.heartRateBaseline)
                self.heaEntry.insert(0,self.heartRateBaselineString)

                #these are the entry boxes for the alert thresholds, set automatically by the GUI
                #using the last 3 lines from baselines.txt

                self.aroThreshold = Label(self.thresholdFrame, text = "Arousal Alert Threshold")
                self.aroThreshold.pack()
                self.aroTrigger = Entry(self.thresholdFrame,bd = 5)
                self.aroTrigger.pack()
                self.arousalTriggerString = str(self.arousalTrigger) #convert ints and floats to strings
                self.aroTrigger.insert(0,self.arousalTriggerString)

                self.actThreshold = Label(self.thresholdFrame, text = "Activity Alert Threshold")
                self.actThreshold.pack()
                self.actTrigger = Entry(self.thresholdFrame,bd = 5)
                self.actTrigger.pack()
                self.activityTriggerString = str(self.activityTrigger)
                self.actTrigger.insert(0,self.activityTriggerString)

                self.heaThreshold = Label(self.thresholdFrame, text = "Heart Rate Threshold")
                self.heaThreshold.pack()
                self.heaTrigger = Entry(self.thresholdFrame,bd = 5)
                self.heaTrigger.pack()
                self.heartRateTriggerString = str(self.heartRateTrigger)
                self.heaTrigger.insert(0,self.heartRateTriggerString)

                # these variables will hold the actual images
                # try to load the image paths from the baselines file
                # if that fails, load from the backup

                try:
                        self.imgtemp = Image.open(self.arousalAlert)
                except:
                        print("This is not a valid image file, loading from backup")
                        self.lines = open("backup.txt").read().split('\n')
                        self.arousalAlert = self.lines[9]
                        self.imgtemp = Image.open(self.arousalAlert)

                self.imgtemp = self.imgtemp.resize((40, 40), Image.ANTIALIAS)
                self.aroAlert = ImageTk.PhotoImage(self.imgtemp)

                try:
                        self.imgtemp2 = Image.open(self.activityAlert)
                except:
                        print("This is not a valid image file, loading from backup")
                        self.lines = open("backup.txt").read().split('\n')
                        self.activityAlert = self.lines[10]
                        self.imgtemp = Image.open(self.activityAlert)

                self.imgtemp2 = self.imgtemp2.resize((40, 40), Image.ANTIALIAS)
                self.actAlert = ImageTk.PhotoImage(self.imgtemp2)

                try:
                        self.imgtemp3 = Image.open(self.heartRateAlert)
                except:
                        print("This is not a valid image file, loading from backup")
                        self.lines = open("backup.txt").read().split('\n')
                        self.heartRateAlert = self.lines[11]
                        self.imgtemp = Image.open(self.heartRateAlert)

                self.imgtemp3 = self.imgtemp3.resize((40, 40), Image.ANTIALIAS)
                self.heaAlert = ImageTk.PhotoImage(self.imgtemp3)

                #these are the images used for the alerts

                self.aroImageLabel = Label(self.alertFrame,text = "Arousal Alert Image", image = self.aroAlert)
                self.aroImageLabel.grid(column = 0,row = 0)
                self.actImageLabel = Label(self.alertFrame,text = "Activity Alert Image", image = self.actAlert)
                self.actImageLabel.grid(column = 0,row = 1)
                self.heaImageLabel = Label(self.alertFrame,text = "Heart Rate Alert Image", image = self.heaAlert)
                self.heaImageLabel.grid(column = 0,row = 2)

                #these are the update buttons for the images
                self.arousalButton = Button(self.alertFrame, text="Update Arousal Alert Image", fg="black",
                                            command = lambda: self.pickFile(self.aroAlert))
                self.arousalButton.grid(column = 1,row = 0)
                self.activityButton = Button(self.alertFrame, text = "Update Activity Alert Image",fg = "black",
                                             command = lambda: self.pickFile(self.actAlert))
                self.activityButton.grid(column = 1,row = 1)
                self.heartRateButton = Button(self.alertFrame,text = "Update Heart Rate Alert Image",fg = "black",
                                              command = lambda: self.pickFile(self.heaAlert))
                self.heartRateButton.grid(column = 1,row = 2)

                self.rootE.mainloop()

        #this is the update method, which gets called when the user presses the update button
        def update(self):
                #if the baselines or triggers are different from the ones in the file
                #they get saved and the file gets updated

                if(self.aroEntry.get() != self.arousalBaseline):
                        self.arousalBaseline = self.aroEntry.get()
                if(self.actEntry.get() != self.activityBaseline):
                        self.activityBaseline = self.actEntry.get()
                if(self.heaEntry.get() != self.heartRateBaseline):
                        self.heartRateBaseline = self.heaEntry.get()
                if(self.aroTrigger.get() != self.arousalTrigger):
                        self.arousalTrigger = self.aroTrigger.get()
                if(self.actTrigger.get() != self.activityTrigger):
                        self.activityTrigger = self.actTrigger.get()
                if(self.heaTrigger.get() != self.heartRateTrigger):
                        self.heartRateTrigger = self.heaTrigger.get()

                #Open the file to write to
                self.file = open("baselines.txt",'w')

                #print the data to the file

                print(self.arousalBaseline, file = self.file)
                print(self.activityBaseline,file = self.file)
                print(self.heartRateBaseline,file = self.file)
                print(self.arousalTrigger,file = self.file)
                print(self.activityTrigger,file = self.file)
                print(self.heartRateTrigger,file = self.file)
                print(self.arousalDisplay.get(),file = self.file)
                print(self.activityDisplay.get(),file = self.file)
                print(self.heartRateDisplay.get(),file = self.file)
                print(self.arousalAlert,file = self.file)
                print(self.activityAlert,file = self.file)
                print(self.heartRateAlert,file = self.file)
                self.rootE.destroy()
                self.file.close()
                ExpertGUI()
                #close the file, close the window, then call the expertGUI again

        #this function is called when the user clicks one of the update image buttons

        def pickFile(self,image):

                #the try/catch blocks ensure that the user picks a valid
                #image file and throws an error if that isn't the case

                if (image == self.aroAlert):
                        self.arousalAlert = filedialog.askopenfilename()
                        try:
                                self.imgtemp = Image.open(self.arousalAlert)
                        except:
                                print("This is not a valid image file")
                if(image == self.actAlert):
                        self.activityAlert = filedialog.askopenfilename()
                        try:
                                self.imgtemp2 = Image.open(self.activityAlert)
                        except:
                                print("This is not a valid image file")
                if(image == self.heaAlert):
                        self.heartRateAlert = filedialog.askopenfilename()
                        try:
                                self.imgtemp3 = Image.open(self.heartRateAlert)
                        except:
                                print("This is not a valid image file")
