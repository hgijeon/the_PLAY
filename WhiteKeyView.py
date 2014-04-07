from KeyView import *

width = 80
height = 300

class WhiteKeyView(KeyView):
    def onInit(self):
        self.width = width
        self.height = height

        self.keyColor = gameapi.Color(128,128,128)

    def onDraw(self):
        self.drawRect(self.keyColor, (5, 0, width-10, height))
        super().drawBar()
