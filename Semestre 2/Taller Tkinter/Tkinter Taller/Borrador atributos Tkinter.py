### ======= Libraries ===== #####
from tkinter import *
from threading import Thread
import os, time
from Frame import *

### ======    ===== ###
WIDTH = 400
HEIGHT = 500
transColor = "#642EFE"

def main ():
    # Window creation
    mainWindow = Tk()

    #Window settings
    mainWindow.title("Tkinter")
    mainWindow.minsize(WIDTH, HEIGHT)
    mainWindow.resizable(width = False, height=False)
    mainWindow.wm_attributes('-transparentcolor', transColor)

    #Adding a background
    bgPath = os. path.join("rsc", "img_00.gif")
    bgImg = PhotoImage(file=bgPath)

    #Placing the main canvas
    mCanvas = Canvas(mainWindow, width=396, height = 496, bg = "#FAFAFA")
    mCanvas.place(x=0, y=0)

    #Placing the background
    bg = Label(mCanvas, image=bgImg, bg="#FAFAFA")
    bg.place(x=-2, y=0)

    #Main Frame
    settings = Settings(250, 400, "Helvetica")
    mainFrame = MainFrame(mainWindow) 
    mainFrame.__createCanvas__()

    #setting this window as main
    mainWindow.mainloop()

main()
