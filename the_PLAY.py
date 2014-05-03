from Structure.Middle import gameapi
from Structure.Middle import apiVar
import pygame.midi as midi

import tkinter as tk
from sys import platform as _platform
import os

import time

from Structure.Middle import SceneManager
from Structure.Scene.LoadingScene import LoadingScene
from Structure.Scene.GameScene import GameScene
from Structure.Scene.SelectScene import SelectScene
from Structure.Scene.StartScene import StartScene

def windowScreen():
    return gameapi.display.set_mode((800, 600), gameapi.DOUBLEBUF|gameapi.HWSURFACE)#|gameapi.FULLSCREEN) #gameapi.NOFRAME|gameapi.DOUBLEBUF|gameapi.RESIZABLE)

def fullScreen():
    return gameapi.display.set_mode((800, 600), gameapi.DOUBLEBUF|gameapi.HWSURFACE|gameapi.FULLSCREEN)

windowed=True
def toggleScreen():
    global windowed
    
    if windowed:
        fullScreen()
        windowed = not windowed
    else:
        windowScreen()
        windowed = not windowed

class the_PLAY:
    def __init__(self):
        self.main()

    def asdf(self, event):
        print ("asdfasdfasdfasdfasdf")

    def main(self):
        tkroot = tk.Tk() # using with tk
        tkroot.withdraw() # we don't want a full GUI, so keep the root window from appearing
        embed = tk.Frame(tkroot, width=100, height=100)
        embed.bind("<Key>", self.asdf)
        embed.pack()

        if _platform == "linux" or _platform == "linux2":
            os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        elif _platform == "darwin":
            os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        elif _platform == "win32":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
        else:
            print("cannot support '%s'."% _platform)

        gameapi.init()
        gameapi.fastevent.init()
        fontObj = gameapi.font.Font('freesansbold.ttf', 64)

        try:
            midi.init()
            piano_id = midi.get_default_input_id()
            print(midi.get_device_info(piano_id))
            midiInput = midi.Input(piano_id)
            midiConnect = True
            print("MIDI connection complete")
        except:
            midiConnect = False
            print("MIDI connection failed")

        mainWindow = windowScreen()
        gameapi.display.set_caption('the_PLAY')
        sceneManager = SceneManager.SceneManager(StartScene, mainWindow, tkroot)

        startFps = 33
        frameN = 30
        frameAccu = [startFps] * frameN
        frameCount = 0
        fpsText = fontObj.render("%.2f fps"%min(frameAccu), False, (128, 128, 0))
        fpsClock = gameapi.time.Clock()
        while True:
            startTime = time.time()
            mod = frameCount%frameN
            
            currentScene = sceneManager.getScene()

            if(midiConnect):
                while midiInput.poll():
                    midiEvents = midiInput.read(10)
                    for e in midi.midis2events(midiEvents, piano_id):
                        gameapi.fastevent.post(e)

            currentScene.updateTime(startTime)
            for event in gameapi.fastevent.get():
                if event.type == apiVar.KEYDOWN:
                    if event.key == apiVar.K_ESCAPE:
                        gameapi.event.post(gameapi.event.Event(apiVar.QUIT))
                    elif event.key == apiVar.K_RETURN:
                        toggleScreen()
                currentScene.event(event)

            currentScene.draw()
            mainWindow.blit(fpsText, fpsText.get_rect())
            
            
            gameapi.display.flip()
            endTime = time.time()

            

            try:
                rate = 1/(endTime-startTime)
                if rate<10:
                    rate = 10
            except:
                rate = 500
            frameAccu[mod] = rate
            frameCount+=1

            if mod == 0:
                minfps = min(frameAccu)*0.9
                fpsText = fontObj.render("%.2f fps"%minfps, False, (128, 128, 0))
                #fpsClock.tick(minfps)


if __name__ == '__main__':
    try:
        the_PLAY()
    except:        
        gameapi.quit()
        raise
