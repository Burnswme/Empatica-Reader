#import TKinter and ttk
from tkinter import *
from tkinter import ttk

class UsrGUI():
    def __init__(self):
        root = Tk()
        root.geometry('1600x600')

        #creates canvas with scrollbar for user to see data
        window = Frame(root,width = 500,height = 500).grid(row = 1,column = 0, columnspan = 25)

        daysCanvas = Canvas(window, width = 500, height = 600, scrollregion = (0,0,0,4000),bg = 'red')
        daysCanvas.grid(row=1, column=0, rowspan=7,columnspan = 25, stick = 'nsew')

        dayLbl = Label(root, width = 8, text = 'Day').grid(row = 0, column = 0)

        #hour labels for canvas
        displayMatrix = [[0 for x in range(24)]for y in range(7)]

        i = 0
        while i <= 6:
            j = 0
            while j<=23:
                if j>7 and j<20:
                    displayMatrix[i][j] = Label(daysCanvas, height = 5, width = 5 , bg = 'orange',relief = RIDGE).grid(row = i+1,column =j+1)
                else:
                    displayMatrix[i][j] = Label(daysCanvas, height = 5, width = 5, bg= 'blue',relief = RIDGE).grid(row=i + 1, column=j + 1)
                j+=1
            i+=1


        #left side labels for days
        mon = Label(daysCanvas, text="Monday").grid(row = 1,column = 0, stick = 'nsew')
        tue = Label(daysCanvas, text="Tuesday").grid(row = 2,column = 0, stick = 'nsew')
        wed = Label(daysCanvas, text="Wednesday").grid(row = 3,column = 0, stick = 'nsew')
        thu = Label(daysCanvas, text="Thursday").grid(row = 4,column = 0, stick = 'nsew')
        fri = Label(daysCanvas, text="Friday").grid(row = 5,column = 0, stick = 'nsew')
        sat = Label(daysCanvas, text="Saturday").grid(row = 6,column = 0, stick = 'nsew')
        sun = Label(daysCanvas, text="Sunday").grid(row = 7,column = 0, stick = 'nsew')

        #hour labels for top

        w = 5

        twelveA = Label(root, text = '12:00',width = w).grid(row = 0,column = 1)
        oneA = Label(root, text = '1:00',width = w ).grid(row = 0,column = 2)
        twoA = Label(root, text = '2:00',width = w ).grid(row = 0,column = 3)
        threeA = Label(root, text = '3:00',width = w ).grid(row = 0,column = 4)
        fourA = Label(root, text = '4:00',width = w ).grid(row = 0,column = 5)
        fiveA = Label(root, text = '5:00',width = w ).grid(row = 0,column = 6)
        sixA = Label(root, text = '6:00',width = w ).grid(row = 0,column = 7)
        sevenA = Label(root, text = '7:00',width = w ).grid(row = 0,column = 8)
        eightA = Label(root, text = '8:00',width = w ).grid(row = 0,column = 9)
        nineA = Label(root, text = '9:00',width = w ).grid(row = 0,column = 10)
        tenA = Label(root, text = '10:00',width = w ).grid(row = 0,column = 11)
        elevenA = Label(root, text = '11:00',width = w ).grid(row = 0,column = 12)
        twelveP = Label(root, text = '12:00',width = w ).grid(row = 0,column = 13)
        oneP = Label(root, text = '1:00',width = w ).grid(row = 0,column = 14)
        twoP = Label(root, text = '2:00',width = w ).grid(row = 0,column = 15)
        threeP = Label(root, text = '3:00',width = w ).grid(row = 0,column = 16)
        fourP = Label(root, text = '4:00',width = w ).grid(row = 0,column = 17)
        fiveP = Label(root, text = '5:00',width = w ).grid(row = 0,column = 18)
        sixP = Label(root, text = '6:00',width = w ).grid(row = 0,column = 19)
        sevenP = Label(root, text = '7:00',width = w ).grid(row = 0,column = 20)
        eightP = Label(root, text = '8:00',width = w ).grid(row = 0,column = 21)
        nineP = Label(root, text = '9:00',width = w ).grid(row = 0,column = 22)
        tenP = Label(root, text = '10:00',width = w ).grid(row = 0,column = 23)
        elevenP = Label(root, text = '11:00',width = w ).grid(row = 0,column = 24)


        root.mainloop()



    #main()