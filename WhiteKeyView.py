from View import *

width = 80

class WhiteKeyView(View):
    def onInit(self):
        self.keyColor = gameapi.Color(128,128,128)

    def onDraw(self):
        self.drawRect(self.keyColor, (5, 0, width-10, 300))
