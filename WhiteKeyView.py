from View import *

width = 80

class WhiteKeyView(View):
    def onInit(self):
        self.keyColor = gameapi.Color(128,128,128)

    def onDraw(self):
        surface = self.surface

        gameapi.draw.rect(surface, self.keyColor, (5, 0, width-10, 300))
