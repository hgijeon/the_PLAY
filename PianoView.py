from View import *

import BlackKeyView
import WhiteKeyView

class PianoView(View):
    def onInit(self):
        self.white = (255,255,255)
        self.childList += self.createOneOctaveView((0,0))
        self.childList += self.createOneOctaveView((WhiteKeyView.width*7,0))
        
    def onDraw(self):
        self.drawRect(self.white, (0, 50, 800, 300))

    def createOneOctaveView(self, leftTop):
        left, top = leftTop

        width = WhiteKeyView.width
        whiteKeys = [WhiteKeyView.WhiteKeyView(self.scene, self, (100, 1000), RefVector(left + width*i, top)) for i in range(7)]

        bidth = BlackKeyView.width
        blackKeys = [BlackKeyView.BlackKeyView(self.scene, self, (50, 1000), RefVector(left + width*i - bidth/2, top)) for i in [1,2,4,5,6]]

        return [ whiteKeys[0], blackKeys[0], whiteKeys[1], blackKeys[1], whiteKeys[2], whiteKeys[3], blackKeys[2], whiteKeys[4], blackKeys[3], whiteKeys[5], blackKeys[4], whiteKeys[6] ]
