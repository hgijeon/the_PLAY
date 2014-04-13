from Structure.Middle import gameapi
from Structure.Middle import apiVar

import tkinter as tk
from sys import platform as _platform
import os

import time

from Structure.Middle import SceneManager
from Structure.Scene.LoadingScene import LoadingScene
from Structure.Scene.GameScene import GameScene
from Structure.Scene.SelectScene import SelectScene

class the_PLAY:
    def __init__(self):
        self.main()

    def main(self):
        tkroot = tk.Tk() # using with tk
        tkroot.withdraw() # we don't want a full GUI, so keep the root window from appearing
        embed = tk.Frame(tkroot, width=100, height=100)
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
        fontObj = gameapi.font.Font('freesansbold.ttf', 32)

        mainWindow = gameapi.display.set_mode((1280, 768))
        gameapi.display.set_caption('the_PLAY')
        sceneManager = SceneManager.SceneManager(SelectScene, mainWindow, tkroot)

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

            currentScene.updateTime(startTime)
            for event in gameapi.event.get():
                currentScene.event(event)

            currentScene.draw()
            mainWindow.blit(fpsText, fpsText.get_rect())
            
            
            gameapi.display.flip()
            endTime = time.time()
            
            tkroot.update()
            

            try:
                rate = 1/(endTime-startTime)
            except:
                rate = 500
            frameAccu[mod] = rate
            frameCount+=1

            if mod == 0:
                minfps = min(frameAccu)*0.9
                fpsText = fontObj.render("%.2f fps"%minfps, False, (128, 128, 0))
                fpsClock.tick(minfps)


if __name__ == '__main__':
    try:
        the_PLAY()
    except:        
        gameapi.quit()
        raise
