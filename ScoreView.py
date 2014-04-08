from View import *


class ScoreView(View):
    def onInit(self):
        self.bg = gameapi.Color(200,200,200)
        
        
    def onDraw(self):
        self.drawRect(self.bg, (0, 0, 150, 100))
