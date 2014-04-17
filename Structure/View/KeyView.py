from .View import *
from ..Model.Dot import Dot


threshold = 0.3


class KeyView(View):
    def onInit(self):
        self.pressTime = 0
        self.score = None
        self.prevTime = None

        height = self.scene.dotEndY - self.scene.dotStartY
        self.barSurface = gameapi.Surface((self.width, height), apiVar.SRCALPHA)
        
    
    def drawBar(self):
        self.drawRect((128,0,0), (0, self.scene.lineY, self.width, 5))

    def onUpdateTime(self, time):
        if self.prevTime == None:
            self.prevTime = time
        self.updateDots(self.scene.playTime)
        if self.middle.check(self.pitch):
            self.pressTime = time
            if self.score == None:
                self.score = 0
                
            if self.act == True:
                self.score += 1000*(time - self.prevTime)
                pass
            else :
                self.score -= 500*(time - self.prevTime)
                pass
        else:
            if self.score != None:
                self.scene.score += int(self.score)
                self.score = None
            

        timediff = time - self.pressTime
        if timediff > threshold:
            ratio = 1
        else:
            ratio = timediff/threshold
        self.keyColor = [self.downColor[i] + (self.upColor[i] - self.downColor[i]) * ratio for i in [0,1,2,3]]

        self.prevTime = time

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
                self.drawResizeImage(self.dotImage, rect)
                
                ''' draw rectangle
                self.drawRect(color, rect)
                '''


        if self.score != None:
            self.drawScore()

    

    def drawScore(self):
        self.drawChar(str(int(self.score)), (0,200), self.scene.scoreFont)

    def updateDots(self, playtime):
        self.dotList = self.middle.getData(self.pitch)



        
        
            
                


        
