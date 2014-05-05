from .View import *
import os

from ..Scene.GameScene import GameScene

from tkinter.filedialog import askopenfilename
class SelectScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.fileSelected = False
        self.background = self.resizeImage(gameapi.image.load(os.path.join("Image","easy_background.jpg")), (800,340))
        self.icon_pressed = self.resizeImage(gameapi.image.load(os.path.join("Image","icon_pressed.png")), (150,150))
        self.icon_unpressed = self.resizeImage(gameapi.image.load(os.path.join("Image","icon_unpressed.png")), (150,150))
        self.easy = self.resizeImage(gameapi.image.load(os.path.join("Image","easy.png")), (300,150))
        self.normal = self.resizeImage(gameapi.image.load(os.path.join("Image","normal.png")), (300,150))
        self.hard = self.resizeImage(gameapi.image.load(os.path.join("Image","hard.png")), (300,150))
        self.title1 = self.resizeImage(gameapi.image.load(os.path.join("Image","title1.png")), (300,170))
        self.title2 = self.resizeImage(gameapi.image.load(os.path.join("Image","title2.png")), (300,200))        
        self.title3 = self.resizeImage(gameapi.image.load(os.path.join("Image","title3.png")), (300,200))
        self.title4 = self.resizeImage(gameapi.image.load(os.path.join("Image","title3.png")), (300,200))
        self.title5 = self.resizeImage(gameapi.image.load(os.path.join("Image","title1.png")), (300,170))
        self.title6 = self.resizeImage(gameapi.image.load(os.path.join("Image","title2.png")), (300,200))
        self.title7 = self.resizeImage(gameapi.image.load(os.path.join("Image","title7.png")), (300,200))
        self.title8 = self.resizeImage(gameapi.image.load(os.path.join("Image","title2.png")), (300,200))
        self.title9 = self.resizeImage(gameapi.image.load(os.path.join("Image","title3.png")), (300,200))

        self.mode = 1
        self.icon = 1
        
    def onDraw(self):            
        self.fill((200,200,200))
        #self.drawRect(self.red, (0, 0, 800, 600))
        leftTop = (0,0)
        self.drawImage (self.background, leftTop)

        if self.mode == 1:
            leftTop = (0,0)
            self.drawImage (self.easy, leftTop)
            
        elif self.mode == 2:
            leftTop = (250,0)
            self.drawImage (self.normal, leftTop)
            
        elif self.mode == 3:
            leftTop = (500,0)
            self.drawImage (self.hard, leftTop)
            
        self.drawIcons()
                    
    def onUpdateTime(self, time):
        if self.fileSelected:
            self.scene.sceneManager.pushGameScene(self.scene.filename)
        if self.keyMiddle.check(self.keyMiddle.key['5']):
            self.mode = 1
        elif self.keyMiddle.check(self.keyMiddle.key['6']):
            self.mode = 2
        elif self.keyMiddle.check(self.keyMiddle.key['7']):
            self.mode = 3
        elif self.keyMiddle.check(self.keyMiddle.key['r']):
            self.icon = 1           
        elif self.keyMiddle.check(self.keyMiddle.key['t']):
            self.icon = 2
        elif self.keyMiddle.check(self.keyMiddle.key['y']):
            self.icon = 3
        elif self.keyMiddle.check(81):
            self.fileopen()



    def fileopen(self):
        print ('Fileopen')
        print (self.icon)
        if self.mode == 1:
            if self.icon == 1:
                self.scene.filename = "MIDI/Music/Twinkle Twinkle Little Star.mid"
            elif self.icon == 2:
                self.scene.filename = "MIDI/Music/Happy Birthday.mid"
            elif self.icon == 3:
                self.scene.filename = "MIDI/Music/Amazing Grace.mid"
        if self.mode == 2:
            if self.icon == 1:
                self.scene.filename = "MIDI/Music/moonlight-movement1.mid"
            elif self.icon == 2:
                self.scene.filename = "MIDI/Music/wagner-bridal-chorus.mid"
            elif self.icon == 3:
                self.scene.filename = "MIDI/Music/pachelbels-canon-arranged.mid"
        if self.mode == 3:
            if self.icon == 1:
                self.scene.filename = "MIDI/Music/Minuet.mid"
            elif self.icon == 2:
                self.scene.filename = "MIDI/Music/idina_menzel-let_it_go.mid"
            elif self.icon == 3:
                self.scene.filename = "MIDI/Music/The-Entertainer.mid"

        self.fileSelected = True

    def drawIcons(self):
        leftTop = (80,50)
        self.drawImage (self.icon_unpressed, leftTop)
        leftTop = (330,50)
        self.drawImage (self.icon_unpressed, leftTop)
        leftTop = (580,50)
        self.drawImage (self.icon_unpressed, leftTop)
        if self.icon == 1:
            leftTop = (80, 50)
            self.drawImage (self.icon_pressed, leftTop)
        elif self.icon == 2:
            leftTop = (330,50)
            self.drawImage (self.icon_pressed, leftTop)
        elif self.icon == 3:
            leftTop = (580,50)
            self.drawImage (self.icon_pressed, leftTop)

        if self.mode == 1:
            leftTop = (0,200)
            self.drawImage (self.title1, leftTop)
            leftTop = (250,200)
            self.drawImage (self.title2, leftTop)
            leftTop = (500,200)
            self.drawImage (self.title3, leftTop)
        if self.mode == 2:
            leftTop = (0,200)
            self.drawImage (self.title4, leftTop)
            leftTop = (250,200)
            self.drawImage (self.title5, leftTop)
            leftTop = (500,200)
            self.drawImage (self.title6, leftTop)
        if self.mode == 3:
            leftTop = (0,200)
            self.drawImage (self.title7, leftTop)
            leftTop = (250,200)
            self.drawImage (self.title8, leftTop)
            leftTop = (500,200)
            self.drawImage (self.title9, leftTop)

            
