from tkinter import *
from tkinter import ttk
import tkMessageBox
import tkinter

class ExpertGUI:

        root = Tk()
        root.title("Empatica Reader Expert Menu")
        root.geometry('500x300+25+25')

        #frame 1 holds the checkboxes to determine which variables to track
        frame1 = LabelFrame(root,text = "Select variables to display")
        frame1.pack(side = LEFT)

        #frame 2 holds the data from the currently selected variable
        frame2 = LabelFrame(root,text = "Update Baselines")
        frame2.pack(side = RIGHT)

        #frame 3 holds the % deviation from the baseline at which the program triggers an alert
        frame3 = LabelFrame(root,text = "Set percentage at which to trigger alerts")
        frame3.pack(side = TOP)

        arousal = IntVar()
        activity = IntVar()
        heartRate = IntVar()

        #these variables will hold the baseline values set by the expert user

        arousalBaseline = 0
        activityBaseline = 0
        heartRateBaseline = 0

        #these variables will hold the threshold triggers set by the expert user

        arousalTrigger = 0
        activityTrigger = 0
        heartRateTrigger = 0

        c1 = Checkbutton(frame1,text = "Arousal",variable = arousal, onvalue = 1,offvalue = 0,height = 5,
                         width = 20)
        c2 = Checkbutton(frame1,text = "Activity",variable = activity, onvalue = 1, offvalue = 0, height = 5,
                         width = 20)
        c3 = Checkbutton(frame1,text = "Heart Rate",variable = heartRate, onvalue = 1, offvalue = 0,
                         height = 5, width = 20)
        c1.pack()
        c2.pack()
        c3.pack()

        l1 = Label(frame2,text = "Arousal Baseline")
        l1.pack()
        E1 = Entry(frame2,bd = 5)
        E1.pack()
        l2 = Label(frame2,text = "Activity Baseline")
        l2.pack()
        E2 = Entry(frame2,bd = 5)
        E2.pack()
        l3 = Label(frame2, text = "Heart Rate Baseline")
        l3.pack()
        E3 = Entry(frame2,bd = 5)
        E3.pack()
        updateButton = Button(frame2,text = "Update",fg = "black")
        updateButton.pack(side = BOTTOM)

        l4 = Label(frame3, text = "Arousal Alert Threshold")
        l4.pack()
        E4 = Entry(frame3,bd = 5)
        E4.pack()
        l5 = Label(frame3, text = "Activity Alert Threshold")
        l5.pack()
        E5 = Entry(frame3,bd = 5)
        E5.pack()
        l6 = Label(frame3, text = "Heart Rate Threshold")
        l6.pack()
        E6 = Entry(frame3,bd = 5)
        E6.pack()
        updateButton2 = Button(frame3,text = "Update",fg = "black")
        updateButton2.pack(side = BOTTOM)


        root.mainloop()