from .View import *
from ..Model.Score import HighScore

import pygame.midi as midi

class RankingScreenView(View):
    def onInit(self):
        self.blue = gameapi.Color(0,0,255)
        self.fileSelected = False
        
        
    def onDraw(self):            
        self.fill((200,200,200))
        self.drawRect(self.blue, (200, 40, 400, 300))

        song = self.scene.getSong()
        self.drawChar(song.name, (0,0), self.scene.font, (255,0,0))
        rank = self.scene.rank
        for i in range(5):
            if i == rank:
                color = (255,0,0)
            else:
                color = (0,255,0)
            self.drawChar(str(song.slotList[i].score), (0, 100 + 100*i), self.scene.font, color)
            self.drawChar(str(song.slotList[i].name), (300, 100 + 100*i), self.scene.font, color)

    def onEvent(self, event):
        if event.type == apiVar.KEYDOWN or event.type == midi.MIDIIN:
            pitch = self.keyMiddle.getPressedPitch(event)
            if pitch != None:
                if pitch >= 48 and pitch < 48+26:
                    c = chr(ord('a') + pitch - 48)
                    self.scene.addLetter(c)
                elif pitch == 83:
                    self.scene.backspace()
                elif pitch == 84:
                    self.scene.done()
                else:
                    self.scene.addLetter(" ")
