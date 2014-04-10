from .View import *
from ..Model.Dot import Dot

class KeyView(View):

    
    def drawBar(self):
        self.drawRect((128,0,0), (0, self.scene.lineY, self.width, 5))

    def onUpdateTime(self, time):
        self.updateDots(self.scene.playTime)

    def setMiddle(self, middle):
        self.middle = middle
        
    def drawDots(self):
        for dot in self.dotList:
            if dot.info != None :
                rect = (0, dot.info[0], self.width, dot.info[1] - dot.info[0])
                self.drawRect((0,0,128), rect)

    def updateDots(self, playtime):
        self.dotList = self.middle.getData(self.pitch)

        
        
            
                


        
