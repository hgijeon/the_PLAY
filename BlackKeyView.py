from KeyView import *

width = 40
height = 150

class BlackKeyView(KeyView):
    def onInit(self):
        super().onInit()
        self.width = width
        self.height = height
        
        self.keyColor = gameapi.Color(200,200,200)

    def onDraw(self):
        self.drawRect(self.keyColor, (0, 0, width, height))
        self.drawDots()
        self.drawBar()
