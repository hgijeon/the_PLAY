from .KeyView import *

width = 50
height = 200

class WhiteKeyView(KeyView):
    def onInit(self):
        self.dotImage = self.scene.whiteDot
        
        self.width = width
        self.height = height

        self.upColor = (128,128,128)
        self.downColor = (255,255,255)
        super().onInit()

    def onDraw(self):
        self.drawRect(self.keyColor, (5, 0, width-10, height), 1)
        self.drawDots()
        self.drawBar()
