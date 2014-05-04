from .View import *
import os

from ..Scene.GameScene import GameScene

from tkinter.filedialog import askopenfilename
class SelectScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.fileSelected = False
        self.easy_background = self.resizeImage(gameapi.image.load(os.path.join("Image","easy_background.jpg")), (800,600))
        self.normal_background = self.resizeImage(gameapi.image.load(os.path.join("Image","normal_background.jpg")), (800,600))
        self.hard_background = self.resizeImage(gameapi.image.load(os.path.join("Image","hard_background.jpg")), (800,600))
        self.icon_pressed = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (200,200))
        self.icon_unpressed = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (200,200))
        self.title1 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title2 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))        
        self.title3 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title4 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title5 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title6 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title7 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title8 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.title9 = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))

        self.mode = 1
        self.icon = 0
        
    def onDraw(self):            
        self.fill((200,200,200))
        self.drawRect(self.red, (20, 40, 400, 300))

        if self.mode == 1:
            leftTop = (0,0)
            self.drawImage (self.easy_background, leftTop)
            
        elif self.mode == 2:
            leftTop = (0,0)
            self.drawImage (self.normal_background, leftTop)
            
        elif self.mode == 3:
            leftTop = (0,0)
            self.drawImage (self.hard_background, leftTop)

        self.drawIcons()
                    
    def onUpdateTime(self, time):
        if self.fileSelected:
            self.scene.sceneManager.pushGameScene(self.scene.filename)
        if self.keyMiddle.check(self.keyMiddle.key['2']):
            self.mode = 1
        elif self.keyMiddle.check(self.keyMiddle.key['3']):
            self.mode = 2
        elif self.keyMiddle.check(self.keyMiddle.key['5']):
            self.mode = 3
        elif self.keyMiddle.check(self.keyMiddle.key['q']):
            self.icon = 1
            self.fileopen()            
        elif self.keyMiddle.check(self.keyMiddle.key['w']):
            self.icon = 2
            self.fileopen()            
        elif self.keyMiddle.check(self.keyMiddle.key['e']):
            self.icon = 3
            self.fileopen()   

        else:
            self.icon = 0



    def fileopen(self):
        print ('Fileopen')
        print (self.icon)
        if self.mode == 1:
            if self.icon == 1:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"
            elif self.icon == 2:
                self.scene.filename = "Midi/Music/minimal.mid"
            elif self.icon == 3:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"
        if self.mode == 2:
            if self.icon == 1:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"
            elif self.icon == 2:
                self.scene.filename = "Midi/Music/minimal.mid"
            elif self.icon == 3:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"
        if self.mode == 3:
            if self.icon == 1:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"
            elif self.icon == 2:
                self.scene.filename = "Midi/Music/minimal.mid"
            elif self.icon == 3:
                self.scene.filename = "Midi/Music/Twinkle Twinkle Little Star.mid"

        self.fileSelected = True

    def drawIcons(self):
        leftTop = (0,300)
        self.drawImage (self.icon_unpressed, leftTop)
        leftTop = (200,300)
        self.drawImage (self.icon_unpressed, leftTop)
        leftTop = (400,300)
        self.drawImage (self.icon_unpressed, leftTop)
        if self.icon == 1:
            leftTop = (0,300)
            self.drawImage (self.icon_pressed, leftTop)
        elif self.icon == 2:
            leftTop = (200,300)
            self.drawImage (self.icon_pressed, leftTop)
        elif self.icon == 3:
            leftTop = (400,300)
            self.drawImage (self.icon_pressed, leftTop)

        if self.mode == 1:
            leftTop = (0,500)
            self.drawImage (self.title1, leftTop)
            leftTop = (0,500)
            self.drawImage (self.title1, leftTop)

        if self.mode == 2:
            leftTop = (0,500)
            self.drawImage (self.title1, leftTop)
        if self.mode == 3:
            leftTop = (0,500)
            self.drawImage (self.title1, leftTop)



            
