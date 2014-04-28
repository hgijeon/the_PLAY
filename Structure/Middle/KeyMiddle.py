from ..Middle import gameapi
from ..Middle import apiVar



class KeyMiddle ():
    def __init__(self):
        self.key = {
        'a':60,
        'w':61,
        's':62,
        'e':63,
        'd':64,
        'f':65,
        't':66,
        'g':67,
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
        except:
            print("not supported key")
        
