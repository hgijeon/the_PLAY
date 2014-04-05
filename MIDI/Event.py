class Event:
   'Common base class for all events'
   eventCount = 0

   def __init__(self, pitch, startTime, eventType):
      self.pitch = pitch
      self.startTime = startTime
      self.eventType = eventType
      Event.eventCount += 1
   
   def displayCount(self):
     print ("Total Events %d" % Event.eventCount)

   def displayEvent(self):
      print ("Pitch : ", self.pitch,  ", startTime: ", self.startTime, ", eventType: ", self.eventType)
