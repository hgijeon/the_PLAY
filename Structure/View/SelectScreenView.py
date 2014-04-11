from .View import *

class SelectScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        
    def onDraw(self):
        self.fill((200,200,200))
        self.drawRect(self.red, (20, 40, 400, 300))
