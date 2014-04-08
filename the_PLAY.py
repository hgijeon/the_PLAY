import gameapi
import apiVar
import time

import SceneManager
from LoadingScene import LoadingScene
from GameScene import GameScene

class the_PLAY:
    def __init__(self):
        self.main()

    def main(self):
        gameapi.init()
        fontObj = gameapi.font.Font('freesansbold.ttf', 32)

        mainWindow = gameapi.display.set_mode((1280, 768))
        gameapi.display.set_caption('the_PLAY')
        sceneManager = SceneManager.SceneManager(GameScene, mainWindow)

        startFps = 33
        frameN = 30
        frameAccu = [startFps] * frameN
        frameCount = 0
        while True:
            startTime = time.time()
            mod = frameCount%frameN
            
            currentScene = sceneManager.getScene()

            currentScene.updateTime(startTime)
            for event in gameapi.event.get():
                currentScene.event(event)

            currentScene.draw()
            if True:
                fpsText = fontObj.render("%.2f fps"%min(frameAccu), False, (128, 128, 0))
                mainWindow.blit(fpsText, fpsText.get_rect())
            
            gameapi.display.update()
            endTime = time.time()

            frameAccu[mod] = 1/(endTime-startTime)
            frameCount+=1


if __name__ == '__main__':
    try:
        the_PLAY()
    except:        
        gameapi.quit()
        raise
