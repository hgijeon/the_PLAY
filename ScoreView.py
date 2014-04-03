from View import *


class ScoreView(View):
    def onInit(self):
        self.black = gameapi.Color(0,0,0)
        
        
    def onDraw(self):
        window = self.scene.window

        gameapi.draw.rect(window, self.black, (0, 0, 150, 100))
