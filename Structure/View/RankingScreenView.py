from .View import *
from ..Model.Score import HighScore

class RankingScreenView(View):
    def onInit(self):
        self.blue = gameapi.Color(0,0,255)
        self.fileSelected = False
        
        
    def onDraw(self):            
        self.fill((200,200,200))
        self.drawRect(self.blue, (200, 40, 400, 300))

        self.scene.addLetter("a")
        self.scene.addLetter("d")
        self.scene.done()
