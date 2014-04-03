from View import *

from PianoView import PianoView
from ScoreView import ScoreView

class GameScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        
        self.childList.append(PianoView(self.scene, self, RefVector(0,200)))
        self.childList.append(ScoreView(self.scene, self, RefVector(0,0)))
        
        
    def onDraw(self):
        window = self.scene.window

        window.fill(self.red)
        gameapi.draw.rect(window, self.red, (20, 40, 100, 300))
