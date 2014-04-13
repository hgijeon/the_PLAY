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
        lineY = self.scene.lineY
        self.act = False
        for dot in self.dotList:
            if dot.info != None :
                color = (0,0,128)
                if dot.info[0] > lineY and dot.info[1] < lineY :
                    color = (128,0,0)
                    self.act = True
                   
                rect = (10, dot.info[1], self.width-20, dot.info[0] - dot.info[1])
                self.drawRect(color, rect)

    def updateDots(self, playtime):
        self.dotList = self.middle.getData(self.pitch)

        
        
            
                


        
