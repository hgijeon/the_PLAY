from .View import *

from . import BlackKeyView
from . import WhiteKeyView

from ..Middle.pianoKey import pianoKey

class PianoView(View):
    def onInit(self):
        self.scene.pianoKeyObserver.append(self)
        
        self.white = (255,255,255)

        self.keyList = []
        
        tmp = self.createOneOctaveView((0,0), 60)
        self.scene.pianoKeyObserver += tmp
        self.childList += tmp
        tmp = self.createOneOctaveView((WhiteKeyView.width*7,0), 72)
        self.scene.pianoKeyObserver += tmp
        self.childList += tmp

        
    def onDraw(self):
        self.drawRect(self.white, (0, 50, 800, 300))

    def setMiddle(self, middle):
        self.middle = middle
        

    def createOneOctaveView(self, leftTop, startPitch):
        left, top = leftTop

        width = WhiteKeyView.width
        whiteKeys = [WhiteKeyView.WhiteKeyView(self.scene, self, (1000, 1000), RefVector(left + width*i, top)) for i in range(7)]


        bidth = BlackKeyView.width
        blackKeys = [BlackKeyView.BlackKeyView(self.scene, self, (1000, 1000), RefVector(left + width*i - bidth/2, top)) for i in [1,2,4,5,6]]

        whitePitch = [0,2,4,5,7,9,11]
        for i in range(len(whitePitch)):
            whiteKeys[i].pitch = startPitch+whitePitch[i]

        blackPitch = [1,3,6,8,10]
        for i in range(len(blackPitch)):
            blackKeys[i].pitch = startPitch+blackPitch[i]
        
        
        return whiteKeys + blackKeys #[ whiteKeys[0], blackKeys[0], whiteKeys[1], blackKeys[1], whiteKeys[2], whiteKeys[3], blackKeys[2], whiteKeys[4], blackKeys[3], whiteKeys[5], blackKeys[4], whiteKeys[6] ]
