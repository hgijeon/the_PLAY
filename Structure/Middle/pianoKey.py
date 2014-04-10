from struct import unpack

from .MIDI.constants import *

from .MIDI.Song import Song
from ..Model.Dot import Dot

class pianoKey ():
    
    def __init__(self, test_file):
        song = Song(test_file)
        self.keyList = [[]]*128
        for i in range(128):
            onEvents = song.checkForEvent(i, 0x01)
            self.keyList[i] = self.createDots(onEvents)
            offEvents = song.checkForEvent(i, 0x00)
            self.addEndTimesToDots(offEvents, self.keyList[i])
        
    def createDots (self, onEvents):
        length = len(onEvents)
        dotList = []
        for i in range (0,length):
            dot = Dot(onEvents[i].startTime)
            dotList.append(dot)
        
        return dotList

    def addEndTimesToDots(self, offEvents, keyList):
        length = len(offEvents)
        if length == 0:
            return
        
        for i in range (length - 1):
            if (keyList[i+1].startTime > offEvents[i].startTime):
                keyList[i].endTime = offEvents[i].startTime
        keyList[-1].endTime = offEvents[-1].startTime
