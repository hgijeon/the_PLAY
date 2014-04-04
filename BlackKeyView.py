from View import *

width = 40

class BlackKeyView(View):
    def onInit(self):
        self.keyColor = gameapi.Color(200,200,200)

    def onDraw(self):
        self.drawRect(self.keyColor, (0, 0, width, 150))
