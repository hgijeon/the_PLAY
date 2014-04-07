from Scene import *

from GameScreenView import GameScreenView


class GameScene(Scene):
    def initModel(self):
        self.barStartY = -200
        self.lineY = 100
        self.setBarSpeed(100)
        

    def setBarSpeed(self, pixelPerSecond):
        self.barSpeed = pixelPerSecond
        self.timeOffset = (self.lineY - self.barStartY) / pixelPerSecond
    
    def initMainView(self):
        self.mainView = GameScreenView(self, None, (1000, 1000))
