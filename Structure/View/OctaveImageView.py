from .View import *


class OctaveImageView(View):
    def onInit(self):
        self.image = self.scene.octaveImg

    def onDraw(self):
        self.drawImage(self.image,(0,0))
