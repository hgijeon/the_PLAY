from View import *


class PianoView(View):
    def onInit(self):
        self.black = gameapi.Color(0,0,0)
        
        
    def onDraw(self):
        window = self.scene.window

        gameapi.draw.rect(window, self.black, (0, 200, 300, 100))
