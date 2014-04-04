from View import *


class ScoreView(View):
    def onInit(self):
        self.black = gameapi.Color(0,0,0)
        
        
    def onDraw(self):
        self.drawRect(self.black, (0, 0, 150, 100))
