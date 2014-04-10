from struct import unpack

from constants import *

from Song import Song
from Dot import Dot

class pianoKey ():
    
    def __init__(self, test_file):
        song = Song(test_file)
        self.keyList = []
        for i in range (0,128):
            onEvents = song.checkForEvent(i, 0x01)
            self.keyList[i] = self.createDots(onEvents)
            offEvents = song.checkForEvent(i, 0x00)
            self.addEndTimesToDots(offEvents, self.keylist[i])
        
    def createDots (self, onEvents):
        length = len(onEvents)
        dotList = []
        for i in range (0,length):
            dot = Dot(onEvents[i].startTime)
            dotList.append(dot)
        return dotList

    def addEndTimesToDots(self, offEvents,  keyList):
        length = len(onEvents)
        for i in range (0,length):
            if (keylist[i+1].startTime > offevents[i].endTime):
                keylist[i].endTime = offevents[i].endTime
