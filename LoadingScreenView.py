from View import *

class LoadingScreenView(View):
    def onInit(self):
        self.blue = gameapi.Color(0,0,255)
        self.red = gameapi.Color(255,0,0)
        
    def onDraw(self):
        window = self.scene.window

        window.fill(self.blue)
        gameapi.draw.rect(window, self.red, (20, 40, 100, 300))
