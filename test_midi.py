import sys
import os

import pygame
import pygame.midi
from pygame.locals import *

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()

input_id = pygame.midi.get_default_input_id()

print ("using input_id :%s:" % input_id)
i = pygame.midi.Input( input_id )

pygame.display.set_mode((1,1))



going = True
while going:
    events = event_get()
    for e in events:
        if e.type in [QUIT]:
            going = False
        if e.type in [KEYDOWN]:
            going = False
        if e.type in [pygame.midi.MIDIIN]:
            print (e)

    if i.poll():
        midi_events = i.read(10)
        # convert them into pygame events.
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
        for m_e in midi_evs:
            event_post( m_e )
del i
pygame.midi.quit()
