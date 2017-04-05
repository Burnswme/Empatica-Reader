from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class ExpertGUI():
        def __init__(self):

                self.root = Tk()
                self.root.title("Empatica Reader Expert Menu")
                self.root.geometry('500x500+25+25')

                #open the baselines.txt and populate the fields with them
                self.lines = open("baselines.txt").read().split('\n')
                #print(self.lines)

                # these variables will hold the baseline values set by the expert user

                self.arousalBaseline = self.lines[0]
                #print(self.lines[0])
                self.activityBaseline = self.lines[1]
                #print(self.lines[1])
                self.heartRateBaseline = self.lines[2]
                #print(self.lines[2])

                # these variables will hold the threshold triggers set by the expert user

                self.arousalTrigger = self.lines[3]
                #print(self.lines[3])
                self.activityTrigger = self.lines[4]
                #print(self.lines[4])
                self.heartRateTrigger = self.lines[5]
                #print(self.lines[5])

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


                #these variables will hold the actual images
                self.imgtemp = Image.open(self.arousalAlert)
                self.imgtemp = self.imgtemp.resize((40,40),Image.ANTIALIAS)
                self.aroAlert = ImageTk.PhotoImage(self.imgtemp)

                self.imgtemp = Image.open(self.activityAlert)
                self.imgtemp = self.imgtemp.resize((40,40),Image.ANTIALIAS)
                self.actAlert = ImageTk.PhotoImage(self.imgtemp)

                self.imgtemp = Image.open(self.heartRateAlert)
                self.imgtemp = self.imgtemp.resize((40,40),Image.ANTIALIAS)
                self.heaAlert = ImageTk.PhotoImage(self.imgtemp)







                #frame 1 holds the checkboxes to determine which variables to track
                self.frame1 = LabelFrame(self.root,text = "Select alerts to display")
                self.frame1.grid(row=0,column=0)

                #frame 2 holds the data from the currently selected variable
                self.frame2 = LabelFrame(self.root,text = "Update Baselines")
                self.frame2.grid(row=0,column=1)

                #frame 3 holds the % deviation from the baseline at which the program triggers an alert
                self.frame3 = LabelFrame(self.root,text = "Set percentage at which to trigger alerts")
                self.frame3.grid(row=1,column=1)

                #frame 4 holds the current images used for alerts and allows the user to specify a path
                #where to find the new alerts
                self.frame4 = LabelFrame(self.root,text = "Set the visual representations of the alerts")
                self.frame4.grid(row=1,column=0)

                #the update button takes values present in the fields, checks them against baselines.txt, and updates them
                self.updateButton = Button(self.root, text="Update", fg="black",command = self.update)
                self.updateButton.grid(row = 3,column = 0)

                #these are the checkboxes which set which variables to display alerts for
                self.c1 = Checkbutton(self.frame1,text = "Arousal",variable = self.arousalDisplay, onvalue = 1,offvalue = 0,height = 5,
                                 width = 20)
                self.c2 = Checkbutton(self.frame1,text = "Activity",variable = self.activityDisplay, onvalue = 1, offvalue = 0, height = 5,
                                 width = 20)
                self.c3 = Checkbutton(self.frame1,text = "Heart Rate",variable = self.heartRateDisplay, onvalue = 1, offvalue = 0,
                                 height = 5, width = 20)
                self.c1.pack()
                self.c2.pack()
                self.c3.pack()

                #these are the entry boxes for the baselines, populated automatically by the GUI
                #using the baselines present in baselines.txt

                self.l1 = Label(self.frame2,text = "Arousal Baseline")
                self.l1.pack()
                self.E1 = Entry(self.frame2,bd = 5)
                self.E1.pack()
                self.E1.insert(self.arousalBaseline,self.arousalBaseline)
                self.l2 = Label(self.frame2,text = "Activity Baseline")
                self.l2.pack()
                self.E2 = Entry(self.frame2,bd = 5)
                self.E2.pack()
                self.E2.insert(self.activityBaseline,self.activityBaseline)
                self.l3 = Label(self.frame2, text = "Heart Rate Baseline")
                self.l3.pack()
                self.E3 = Entry(self.frame2,bd = 5)
                self.E3.pack()
                self.E3.insert(self.heartRateBaseline,self.heartRateBaseline)

                #these are the entry boxes for the alert thresholds, set automatically by the GUI
                #using the last 3 lines from baselines.txt
                self.l4 = Label(self.frame3, text = "Arousal Alert Threshold")
                self.l4.pack()
                self.E4 = Entry(self.frame3,bd = 5)
                self.E4.pack()
                self.E4.insert(self.arousalTrigger,self.arousalTrigger)
                self.l5 = Label(self.frame3, text = "Activity Alert Threshold")
                self.l5.pack()
                self.E5 = Entry(self.frame3,bd = 5)
                self.E5.pack()
                self.E5.insert(self.activityTrigger,self.activityTrigger)
                self.l6 = Label(self.frame3, text = "Heart Rate Threshold")
                self.l6.pack()
                self.E6 = Entry(self.frame3,bd = 5)
                self.E6.pack()
                self.E6.insert(self.heartRateTrigger,self.heartRateTrigger)

                #these are the images used for the alerts
                self.l7 = Label(self.frame4,text = "Arousal Alert Image",image = self.aroAlert)
                self.l7.grid(column = 0,row = 0)
                self.l8 = Label(self.frame4,text = "Activity Alert Image",image = self.actAlert)
                self.l8.grid(column = 0,row = 1)
                self.l9 = Label(self.frame4,text = "Heart Rate Alert Image",image = self.heaAlert)
                self.l9.grid(column = 0,row = 2)
                self.arousalButton = Button(self.frame4, text="Update Arousal Alert Image", fg="black",
                                            command = lambda: self.pickFile(self.aroAlert))
                self.arousalButton.grid(column = 1,row = 0)
                self.activityButton = Button(self.frame4, text = "Update Activity Alert Image",fg = "black",
                                             command = lambda: self.pickFile(self.actAlert))
                self.activityButton.grid(column = 1,row = 1)
                self.heartRateButton = Button(self.frame4,text = "Update Heart Rate Alert Image",fg = "black",
                                              command = lambda: self.pickFile(self.heaAlert))
                self.heartRateButton.grid(column = 1,row = 2)

                self.root.mainloop()

        def update(self):
                if(self.E1.get() != self.arousalBaseline):
                        self.arousalBaseline = self.E1.get()
                if(self.E2.get() != self.activityBaseline):
                        self.activityBaseline = self.E2.get()
                if(self.E3.get() != self.heartRateBaseline):
                        self.heartRateBaseline = self.E3.get()
                if(self.E4.get() != self.arousalTrigger):
                        self.arousalTrigger = self.E4.get()
                if(self.E5.get() != self.activityTrigger):
                        self.activityTrigger = self.E5.get()
                if(self.E6.get() != self.heartRateTrigger):
                        self.heartRateTrigger = self.E6.get()


                self.file = open("baselines.txt",'w')

                print(self.arousalBaseline, file = self.file)
                print(self.activityBaseline,file = self.file)
                print(self.heartRateBaseline,file = self.file)
                print(self.arousalTrigger,file = self.file)
                print(self.activityTrigger,file = self.file)
                print(self.heartRateBaseline,file = self.file)
                print(self.arousalDisplay.get(),file = self.file)
                print(self.activityDisplay.get(),file = self.file)
                print(self.heartRateDisplay.get(),file = self.file)
                print(self.arousalAlert,file = self.file)
                print(self.activityAlert,file = self.file)
                print(self.heartRateAlert,file = self.file)

        def pickFile(self,image):
                if (image == self.aroAlert):
                        #self.arousalAlert = filedialog.askopenfilename()
                        self.arousalAlert = filedialog.askopenfilename()
                        #self.imgtemp = Image.open(self.arousalAlert)
                        #self.imgtemp = self.imgtemp.resize((40, 40), Image.ANTIALIAS)
                        #self.aroAlert = ImageTk.PhotoImage(self.imgtemp)
                if(image == self.actAlert):
                        #self.activityAlert = filedialog.askopenfilename()
                        self.activityAlert = filedialog.askopenfilename()
                        #self.imgtemp = Image.open(self.activityAlert)
                        #self.imgtemp = self.imgtemp.resize((40, 40), Image.ANTIALIAS)
                        #self.actAlert = ImageTk.PhotoImage(self.imgtemp)
                if(image == self.heaAlert):
                        #self.heartRateAlert = filedialog.askopenfilename()
                        self.heartRateAlert = filedialog.askopenfilename()
                        #self.imgtemp = Image.open(self.heartRateAlert)
                        #self.imgtemp = self.imgtemp.resize((40, 40), Image.ANTIALIAS)
                        #self.heaAlert = ImageTk.PhotoImage(self.imgtemp)








test = ExpertGUI()