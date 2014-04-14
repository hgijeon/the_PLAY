from .View import *


class ScoreView(View):
    def onInit(self):
        self.bg = gameapi.Color(200,200,200)
        
        
    def onDraw(self):
        self.drawRect(self.bg, (0, 200, 150, 100))
        self.drawChar(str(self.getScore()), (0,200), self.scene.scoreFont)

    def getScore(self):
        return self.scene.score
