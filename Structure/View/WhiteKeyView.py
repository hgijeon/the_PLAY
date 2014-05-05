from .KeyView import *



class WhiteKeyView(KeyView):
    def onInit(self):
        self.dotImage = self.scene.whiteDot
        self.lineDotImage = self.scene.lineWhiteDot
        
        self.width = self.scene.whiteWidth
        self.height = self.scene.whiteHeight

        self.upColor = (255,255,255,0)
        super().onInit()

    def onDraw(self):
        self.drawDots()
        self.drawRect(self.keyColor, (0, 0, self.width, self.height))
        self.drawBar()

    
    def getDotLeftRight(self):
        return (5, self.width - 10)
