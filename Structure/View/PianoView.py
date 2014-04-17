from .View import *

from . import BlackKeyView
from . import WhiteKeyView
from . import OctaveImageView

from ..Middle.pianoKey import pianoKey

class PianoView(View):
    def onInit(self):
        self.scene.pianoKeyObserver.append(self)
        
        self.white = (255,255,255)

        self.keyList = []

        for octave in [3,4,5]:
            self.addOneOctaveView((self.scene.octWidth * (octave-4),0),  12 + 12*octave)
            

    def onEvent(self, event):
        self.middle.updateStatus(event)

        
    def onDraw(self):
        self.drawRect(self.white, (0, 50, 800, 300))

    def setMiddle(self, middle):
        self.middle = middle

    def addOneOctaveView(self, lt, startPitch):
        tmp = self.createOneOctaveView(lt, startPitch)
        self.scene.pianoKeyObserver += tmp

        self.childList.append(OctaveImageView.OctaveImageView(self.scene, self, (1000, 1000), RefVector(lt[0], lt[1])))
        self.childList += tmp
        

    def createOneOctaveView(self, leftTop, startPitch):
        left, top = leftTop

        width = self.scene.whiteWidth
        whiteKeys = [WhiteKeyView.WhiteKeyView(self.scene, self, (1000, 1000), RefVector(left + width*i, top)) for i in range(7)]


        bidth = self.scene.blackWidth
        blackKeys = [BlackKeyView.BlackKeyView(self.scene, self, (1000, 1000), RefVector(left + width*i - bidth/2, top)) for i in [1,2,4,5,6]]

        whitePitch = [0,2,4,5,7,9,11]
        for i in range(len(whitePitch)):
            whiteKeys[i].pitch = startPitch+whitePitch[i]

        blackPitch = [1,3,6,8,10]
        for i in range(len(blackPitch)):
            blackKeys[i].pitch = startPitch+blackPitch[i]
        
        
        return whiteKeys + blackKeys #[ whiteKeys[0], blackKeys[0], whiteKeys[1], blackKeys[1], whiteKeys[2], whiteKeys[3], blackKeys[2], whiteKeys[4], blackKeys[3], whiteKeys[5], blackKeys[4], whiteKeys[6] ]
