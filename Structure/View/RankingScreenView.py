from .View import *
from ..Model.Score import HighScore
import random

import pygame.midi as midi
import os

class RankingScreenView(View):
    def onInit(self):
        self.blue = gameapi.Color(0,0,255)
        self.fileSelected = False
        self.keyHelp = self.resizeImage(gameapi.image.load(os.path.join("Image","keyHelp.png")), (800, 200))
        
        
        
    def onDraw(self):            
        self.fill((0,0,0))

        song = self.scene.getSong()
        self.drawChar(song.name, (100,20), self.scene.font, (2,175,127))
        rank = self.scene.rank
        for i in range(5):
            if i == rank:
                color = (random.randint(128,255),random.randint(64,128),random.randint(64,128))
            else:
                color = (181,211,59)

            score = str(song.slotList[i].score)
            self.drawCharRight(score, (440, 90 + 40*i), self.scene.font, color)
            self.drawChar(str(song.slotList[i].name), (400, 90 + 40*i), self.scene.font, color)
        
        self.drawImage (self.keyHelp, (0,400))

    def onEvent(self, event):
        if event.type == apiVar.KEYDOWN or event.type == midi.MIDIIN:
            pitch = self.keyMiddle.getPressedPitch(event)
            if pitch != None:
                if pitch >= 48 and pitch < 48+26:
                    c = chr(ord('a') + pitch - 48)
                    self.scene.addLetter(c)
                elif pitch == 83:
                    self.scene.backspace()
                elif pitch == 81:
                    self.scene.done()
                else:
                    self.scene.addLetter(" ")
