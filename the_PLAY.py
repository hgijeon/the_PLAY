import gameapi
import apiVar

import SceneManager
import LoadingScene

class the_PLAY:
    def __init__(self):
        self.main()

    def main(self):
        gameapi.init()
        fpsClock = gameapi.time.Clock()

        mainWindow = gameapi.display.set_mode((640, 480))
        sceneManager = SceneManager.SceneManager(LoadingScene.LoadingScene, mainWindow)

        while True:
            currentScene = sceneManager.getScene()
            
            for event in gameapi.event.get():
                currentScene.event(event)

            currentScene.draw()
            gameapi.display.update()
            fpsClock.tick(30)








if __name__ == '__main__':
    the_PLAY()
