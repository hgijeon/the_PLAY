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
        self.icon_twinkle = self.resizeImage(gameapi.image.load(os.path.join("Image","song_icon.jpg")), (300,300))
        self.mode = 1
        self.icon = 0
        
    def onDraw(self):            
        self.fill((200,200,200))
        self.drawRect(self.red, (20, 40, 400, 300))

        if self.mode == 1:
            leftTop = (0,0)
            self.drawImage (self.easy_background, leftTop)
            #draw icons
            leftTop = (350,400)
            self.drawImage (self.icon_twinkle, leftTop)

        elif self.mode == 2:
            leftTop = (0,0)
            self.drawImage (self.normal_background, leftTop)
            #draw icons
            leftTop = (350,400)
            self.drawImage (self.icon_twinkle, leftTop)

        elif self.mode == 3:
            leftTop = (0,0)
            self.drawImage (self.hard_background, leftTop)
            #draw icons
            leftTop = (350,400)
            self.drawImage (self.icon_twinkle, leftTop)
        
    def onUpdateTime(self, time):
        if self.fileSelected:
            self.scene.sceneManager.pushGameScene(self.scene.filename)
        if self.keyMiddle.check(self.keyMiddle.key['w']):
            self.mode = 1
        elif self.keyMiddle.check(self.keyMiddle.key['e']):
            self.mode = 2
        elif self.keyMiddle.check(self.keyMiddle.key['t']):
            self.mode = 3
        elif self.keyMiddle.check(self.keyMiddle.key['a']):
            self.icon = 1
            self.fileopen()            
        elif self.keyMiddle.check(self.keyMiddle.key['s']):
            self.icon = 2
            self.fileopen()            
        elif self.keyMiddle.check(self.keyMiddle.key['d']):
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
