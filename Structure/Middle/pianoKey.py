from struct import unpack

from ..Middle import gameapi
from ..Middle import apiVar

from .MIDI.constants import *

from .MIDI.Song import Song
from ..Model.Dot import Dot


class pianoKey ():
    
    def __init__(self, file_name):
        song = Song(file_name)
        self.keyList = [[]]*128
        for i in range(128):
            onEvents = song.checkForEvent(i, 0x01)
            self.keyList[i] = self.createDots(onEvents)
            offEvents = song.checkForEvent(i, 0x00)
            self.addEndTimesToDots(offEvents, self.keyList[i])
            self.mergeSameEvents(self.keyList[i])
        self.endTime = song.endTime

        
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
            keyList[i].endTime = offEvents[i].startTime
        keyList[-1].endTime = offEvents[-1].startTime

    def mergeSameEvents(self, keyList):
        length = len(keyList)
        eventsToBeRemoved = []
        for i in range (0,length-1):
            if keyList[i+1].startTime < keyList[i].endTime:
                keyList[i].endTime = keyList[i+1].endTime
                eventsToBeRemoved.append(i)
        length = len(eventsToBeRemoved)
        i = length - 1
        while (i>=0):
            keyList.pop(eventsToBeRemoved[i]+1)
            i = i-1

    def getData(self, pitch, playtime = None):
        if playtime == None:
            playtime = self.scene.playTime - self.scene.startTimeOffset

            
        dotSpeed = self.scene.dotSpeed
        lineY = self.scene.lineY
        dotStartY = self.scene.dotStartY
        dotEndY = self.scene.dotEndY

        dotList = self.keyList[pitch]

        removeList = []        
        for dot in dotList:
            startY = (playtime - dot.startTime) * dotSpeed + lineY
            if startY > dotEndY:
                startY = dotEndY
            elif startY < dotStartY:
                dot.info = None
                continue

            if dot.endTime == None:
                endY = dotStartY
            else :
                endY = (playtime - dot.endTime) * dotSpeed + lineY
                if endY > dotEndY:
                    removeList.append(dot)
                    continue
                elif endY < dotStartY:
                    endY = dotStartY

            dot.info = (startY, endY)

        for e in removeList:
            dotList.remove(e)

        return dotList
        
