from tkinter import *
from tkinter import ttk

class ExpertGUI():
        def __init__(self):
                self.root = Tk()
                self.root.title("Empatica Reader Expert Menu")
                self.root.geometry('500x300+25+25')

                #open the baselines.txt and populate the fields with them
                self.lines = open("baselines.txt").read().split('\n')

                # these variables will hold the baseline values set by the expert user

                self.arousalBaseline = self.lines[0]
                print(self.lines[0])
                self.activityBaseline = self.lines[1]
                print(self.lines[1])
                self.heartRateBaseline = self.lines[2]
                print(self.lines)

                # these variables will hold the threshold triggers set by the expert user

                self.arousalTrigger = self.lines[3]
                self.activityTrigger = self.lines[4]
                self.heartRateTrigger = self.lines[5]

                #frame 1 holds the checkboxes to determine which variables to track
                self.frame1 = LabelFrame(self.root,text = "Select alerts to display")
                self.frame1.pack(side = LEFT)

                #frame 2 holds the data from the currently selected variable
                self.frame2 = LabelFrame(self.root,text = "Update Baselines")
                self.frame2.pack(side = RIGHT)

                #frame 3 holds the % deviation from the baseline at which the program triggers an alert
                self.frame3 = LabelFrame(self.root,text = "Set percentage at which to trigger alerts")
                self.frame3.pack(side = TOP)

                #the update button takes values present in the fields, checks them against baselines.txt, and updates them
                self.updateButton = Button(self.root, text="Update", fg="black",command = self.update)
                self.updateButton.pack(side=BOTTOM)

                self.arousal = IntVar()
                self.activity = IntVar()
                self.heartRate = IntVar()

                self.c1 = Checkbutton(self.frame1,text = "Arousal",variable = self.arousal, onvalue = 1,offvalue = 0,height = 5,
                                 width = 20)
                self.c2 = Checkbutton(self.frame1,text = "Activity",variable = self.activity, onvalue = 1, offvalue = 0, height = 5,
                                 width = 20)
                self.c3 = Checkbutton(self.frame1,text = "Heart Rate",variable = self.heartRate, onvalue = 1, offvalue = 0,
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


test = ExpertGUI()