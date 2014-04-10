from .View import *
from ..Model.Dot import Dot

class KeyView(View):
    def onInit(self):
        self.dotList = [Dot(0,2), Dot(3,4), Dot(5,7), Dot(10,15)]
    
    def drawBar(self):
        self.drawRect((128,0,0), (0, self.scene.lineY, self.width, 5))

    def onUpdateTime(self, time):
        self.updateDots(self.scene.playTime)
        
        
    def drawDots(self):
        for dot in self.dotList:
            if dot.rect != None :
                self.drawRect((0,0,128), dot.rect)

    def updateDots(self, playtime):
        dotSpeed = self.scene.dotSpeed
        lineY = self.scene.lineY
        dotStartY = self.scene.dotStartY
        dotEndY = self.scene.dotEndY

        removeList = []        
        for dot in self.dotList:
            startY = (playtime - dot.startTime) * dotSpeed + lineY
            if startY > dotEndY:
                startY = dotEndY
            elif startY < dotStartY:
                dot.rect = None
                continue

            if dot.endTime == None:
                endY = dotStartY
            else :
                endY = (playtime - dot.endTime) * dotSpeed + lineY
                if endY > dotEndY:
                    removeList.append(dot)
                    continue
                elif endY < dotStartY:
                    endY = dotStartY

            dot.rect = (0, endY, self.width, startY-endY)

        for e in removeList:
            self.dotList.remove(e)
            
                


        
