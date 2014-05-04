from ..Middle import gameapi
from ..Middle import apiVar

import pygame.midi as midi



class KeyMiddle ():
    def __init__(self):
        self.key = {
        'q':48,
        '2':49,
        'w':50,
        '3':51,
        'e':52,
        'r':53,
        '5':54,
        't':55,
        '6':56,
        'y':57,
        '7':58,
        'u':59,
            
        'z':60,
        's':61,
        'x':62,
        'd':63,
        'c':64,
        'v':65,
        'g':66,
        'b':67,
        'h':68,
        'n':69,
        'j':70,
        'm':71,

        ',':72,
        'l':73,
        '.':74,
        ';':75,
        '/':76,
        'o':77,
        '0':78,
        'p':79,
        '-':80,
        '[':81,
        '=':82,
        ']':83,
        }
        self.status = [False] * 128


    def check(self, pitch):
        return self.status[pitch]

    def updateStatus(self, event):
        try:
            if event.type == apiVar.KEYDOWN:
                self.status[self.key[gameapi.key.name(event.key)]] = True
            elif event.type == apiVar.KEYUP:
                self.status[self.key[gameapi.key.name(event.key)]] = False
            elif event.type == midi.MIDIIN:
                # print(event)
                if ((event.status >> 4) & 0xf) == 9: # 1001xxxx = on
                    self.status[event.data1] = True
                elif ((event.status >> 4) & 0xf) == 8: # 1000xxxx = off
                    self.status[event.data1] = False
        except:
            print("not supported key")
        
