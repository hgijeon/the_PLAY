from Scene import *

from GameScreenView import GameScreenView


class GameScene(Scene):
    def initModel(self):
        self.dotStartY = -50
        self.lineY = 100
        self.dotEndY = 300
        self.setDotSpeed(100)

        self.playTime = 0
        self.play = True
        

    def setDotSpeed(self, pixelPerSecond):
        self.dotSpeed = pixelPerSecond
        self.startTimeOffset = (self.lineY - self.dotStartY) / pixelPerSecond
        self.endTimeOffset = (self.lineY - self.dotEndY) / pixelPerSecond
    
    def initMainView(self):
        self.mainView = GameScreenView(self, None, (1000, 1000))

    def updateTime(self, time):
        try:
            if self.play:
                self.playTime += time - self.prevTime
        except:
            self.prevTime = time
        self.prevTime = time

        super().updateTime(time)
        
