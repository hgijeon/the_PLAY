from View import *

class LoadingScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        
    def onDraw(self):
        self.drawRect(self.red, (20, 40, 100, 300))
