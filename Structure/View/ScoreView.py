from .View import *


class ScoreView(View):
    def onInit(self):
        self.bg = gameapi.Color(200,200,200)
        
        
    def onDraw(self):
        self.drawCharRight(str(self.getScore()), (100,50), self.scene.scoreFont, (245,161,0))

    def getScore(self):
        return int(self.scene.score + self.scene.updatingScore)
