### === Settings: used to set up the frames ==== ###
class Settings:
    def __init__(self,width,height,font):
        self.WIDTH = width
        self.HEIGHT = height
        self.FONT = font

### ===== mFrame: base class for frames =====###
class mFrame:
    def __init__(self, window,settings, background):
        self.WINDOW = window
        self.SETTINGS = settings
        self.BACKGROUND = background
        self.Canvas = None

    def __createCanvas__(self):
        self.Canvas = Canvas(self.WINDOW, width = self.SETTINGS.WIDTH, HEIGHT = SELF.SETTINGS.HEIGHT, bg = "FAFAFA" )
        self.Canvas.place(x=(404/2 -self.SETTINGS.WIDTH/2), Y =(500/2 - SELF.settings.height/2))

    def __deleteCanvas__(self):
        self.Canvas = None

### === MainFrame: contains the animation === ###

class MainFrame(mFrame):
    def __init__(self,window):
        settings = Settings(250,400, "Helvetica")
        mFrame.__init__(self,window,settings, "img_01.gif")

    def  __createCanvas__(self):
        mFrame.__createCanvas__(self)
        
        b = Button(self.Canvas, text = "New Ball" , command = self.__createBall__)
        b.place(x =0, y = 0)

        self.Canvas.mainloop()

    def __deletaCanvas__(self):
        self.Canvas = None

    def __createBall__(self):
        ball = Ball(self.Canvas)
        threadN = Thread(target=ball.__moving__)
        threadB.start()

### === Ball: objects instanciated for the animation ==== ###
class Ball:
    def __init__(self, canvas):
        self.x = random.radiant(0, 230)
        self.y = random.radiant(0,380)
        self.r = random.radiant(10, 35)
        self.Canvas = canvas
        self.dirX = random.radiant(-3, 3)
        self.dirY = random.radiant(-3,3)
        self.ball = self.Canvas.create_oval(self.x, self.y, self.x+self.r, self.y+self.r , fill ="#9AFE2E")

        self.flag = False

def __moving__(self):
    self.flag = True
    while self.flag:
        self.Canvas.move(self.ball, self.dirX, self.dirY)
        pos = self.Canvas.coords(self.ball)
        if pos[0] <= 0 or pos[2] >= 250:
            self.dirX = -self.dirX
        if pos[1] <= 0 or pos[3] >= 400:
            self.dirY = -selfdirY

        self.Canvas.update()
        time.sleep(0.025)
