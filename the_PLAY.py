import gameapi
import apiVar
import time

import SceneManager
import LoadingScene
from GameScene import GameScene

class the_PLAY:
    def __init__(self):
        self.main()

    def main(self):
        gameapi.init()

        mainWindow = gameapi.display.set_mode((640, 480))
        gameapi.display.set_caption('the_PLAY')
        sceneManager = SceneManager.SceneManager(GameScene, mainWindow)

        while True:
            startTime = time.time()
            
            currentScene = sceneManager.getScene()

            currentScene.timeEvent(startTime)
            for event in gameapi.event.get():
                currentScene.event(event)

            currentScene.draw()
            gameapi.display.update()

            
            endTime = time.time()
            print("%.2f fps"%(1/(endTime-startTime)))



if __name__ == '__main__':
    the_PLAY()
