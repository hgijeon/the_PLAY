from View import *

from PianoView import PianoView
from ScoreView import ScoreView

class GameScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        
        self.childList.append(PianoView(self.scene, self, (1000, 1000), RefVector(20,40)))
        self.childList.append(ScoreView(self.scene, self, (1000, 1000), RefVector(0,0)))
        
        
    def onDraw(self):
        surface = self.surface

        surface.fill(self.red)
        gameapi.draw.rect(surface, self.red, (20, 40, 100, 300))
