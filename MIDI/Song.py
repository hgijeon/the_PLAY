from struct import unpack

import time as timeLib
from constants import *

from MidiFileParser import MidiFileParser
from RawInstreamFile import RawInstreamFile
from MidiToSong import MidiToSong


class Song:
    
    def __init__(self, test_file):
        self.songList=[]
        self.Flags=[]

        self.createSong(test_file)

 
    def createSong (self, test_file):
        midi_to_song = MidiToSong(self.songList)
        midi_in = MidiFileParser(RawInstreamFile(test_file),midi_to_song)
        midi_in.parseMThdChunk()
        midi_in.parseMTrkChunks()
        length = len(self.songList)
        self.Flags=[0]*length

        self.lastIndex = 0

    def checkForEvent(self, time):
        eventsAtTime = []
        for i in range(self.lastIndex, len(self.songList)):
            if (self.songList[i].startTime <= time - self.startTime and self.Flags[i]==0):
                eventsAtTime.append(self.songList[i])
                self.Flags[i] = 1
                self.lastIndex = i

                
        #print len(eventsAtTime)
        return eventsAtTime
        
    def initStartTime(self, time):
        self.startTime = time
        
    def printSong(self):
        length=len(self.songList)
        print (length)
                                 
if __name__ == '__main__':

    # get data
    test_file = 'test/midifiles/minuet1track.mid'
    
    minuet = Song(test_file)
    #minuet.printSong()
    minuet.initStartTime(timeLib.time())
    while(True):
        list = minuet.checkForEvent(timeLib.time())
        if len(list) > 0:
            for e in list:
                e.displayEvent()

    '''
    time=34819200
    list = minuet.checkForEvent(time)
    print (len(list))
    i=0
    while (i<len(list)):
           list[i].displayEvent()
           i=i+1
    time=50819200
    list = minuet.checkForEvent(time)
    print ("======================================")
    i=0
    while (i<len(list)):
           list[i].displayEvent()
           i=i+1
    print (len(list))
'''
