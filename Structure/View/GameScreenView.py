from .View import *

from .PianoView import PianoView
from .ScoreView import ScoreView

class GameScreenView(View):
    def onInit(self):
        self.bg = gameapi.Color(230,170,170)
        
        self.childList.append(PianoView(self.scene, self, (1000, 1000), RefVector(0,300)))
        self.childList.append(ScoreView(self.scene, self, (1000, 1000), RefVector(0,0)))
        
        
    def onDraw(self):
        self.fill(self.bg)

