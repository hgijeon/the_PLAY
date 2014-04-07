from View import *

class KeyView(View):
    def drawBar(self):
        self.drawRect((128,0,0), (0, self.scene.lineY, self.width, 5))
