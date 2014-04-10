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
            if dot.rect != None :
                self.drawRect((0,0,128), dot.rect)

    def updateDots(self, playtime):
        self.dotList = self.middle.keyList[self.pitch]
        
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
            
                


        
