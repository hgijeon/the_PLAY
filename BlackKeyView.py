from View import *

width = 40

class BlackKeyView(View):
    def onInit(self):
        self.keyColor = gameapi.Color(200,200,200)

    def onDraw(self):
        surface = self.surface

        gameapi.draw.rect(surface, self.keyColor, (0, 0, width, 150))
