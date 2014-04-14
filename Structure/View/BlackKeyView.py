from .KeyView import *

width = 30
height = 100

class BlackKeyView(KeyView):
    def onInit(self):
        super().onInit()
        self.width = width
        self.height = height
        
        self.upColor = (200,200,200)
        self.downColor = (0,0,0)

    def onDraw(self):
        self.drawRect(self.keyColor, (0, 0, width, height))
        self.drawDots()
        self.drawBar()
