# -*- coding: ISO-8859-1 -*-

from MidiOutStream import MidiOutStream
from Event import Event
class MidiToSong (MidiOutStream):
    
    """
    This class renders a midi file as a list of Events
    """
    def __init__(self, songList):
        self.songList = songList
        
    def addEvent(self, pitch, startTime, eventType):
        event= Event(pitch, startTime, eventType)
        self.songList.append(event)
        
    def setTickLength(self, ticksPerQuarternote, usPerQuarternote):
        self.usPerTick = usPerQuarternote/ticksPerQuarternote
        
    def changeTempo(self, usPerQuarternote):
        self.usPerTick = self.usPerTick*usPerQuarternote/500000


    #############################
    # channel events
    
    
    def channel_message(self, message_type, channel, data):
        """The default event handler for channel messages"""
        #print 'message_type:%X, channel:%X, data size:%X' % (message_type, channel, len(data))


    def note_on(self, channel=0, note=0x40, velocity=0x40):
        time = self.abs_time()*self.usPerTick/1000000
        #print 'note_on  - ch:%02X,  note:%02X,  vel:%02X time:%s' % (channel, note, velocity, time)
        self.addEvent(note,time,0x01)

    def note_off(self, channel=0, note=0x40, velocity=0x40):
        time = self.abs_time()*self.usPerTick/1000000
        #print 'note_off - ch:%02X,  note:%02X,  vel:%02X time:%s' % (channel, note, velocity, time)
        self.addEvent(note,time,0x00)

    def header(self, format=0, nTracks=1, division=96):
        self.setTickLength(division,500000)
        print ('format: %s, nTracks: %s, division: %s' % (format, nTracks, division))
        
    def tempo(self, value):
        #print 'tempo:', value
        self.changeTempo(value)

if __name__ == '__main__':

    # get data
    test_file = 'test/midifiles/minuet1track.mid'
    f = open(test_file, 'rb')
    
    # do parsing
    from MidiInFile import MidiInFile
    midiIn = MidiInFile(MidiToText(), f)
    midiIn.read()
    f.close()
