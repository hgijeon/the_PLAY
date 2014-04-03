from View import *

import BlackKeyView
import WhiteKeyView

class PianoView(View):
    def onInit(self):
        self.white = (255,255,255)
        self.childList += self.createOneOctaveView((0,0))
        
    def onDraw(self):
        surface = self.surface

        gameapi.draw.rect(surface, self.white, (0, 50, 800, 300))

    def createOneOctaveView(self, topLeft):
        top, left = topLeft

        width = WhiteKeyView.width
        whiteKeys = [WhiteKeyView.WhiteKeyView(self.scene, self, (100, 1000), RefVector(left + width*i, top)) for i in range(7)]

        bidth = BlackKeyView.width
        blackKeys = [BlackKeyView.BlackKeyView(self.scene, self, (50, 1000), RefVector(left + width*i - bidth/2, top)) for i in [1,2,4,5,6]]

        return whiteKeys + blackKeys
