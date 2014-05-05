from .KeyView import *

class BlackKeyView(KeyView):
    def onInit(self):
        self.dotImage = self.scene.blackDot
        self.lineDotImage = self.scene.lineBlackDot

        self.width = self.scene.blackWidth
        self.height = self.scene.blackHeight
        
        self.upColor = (0,0,0,0)
        self.downColor = (128,0,0,255)
        super().onInit()

    def onDraw(self):
        self.drawRect(self.keyColor, (0, 0, self.width, self.height), 1)
        self.drawDots()
        self.drawBar()

    def getDotLeftRight(self):
        return (5, self.width - 10)
