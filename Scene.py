import gameapi
import apiVar
import sys

class Scene:
    def __init__(self, sceneManager, window):
        self.sceneManager = sceneManager
        self.window = window

        self.initModel()
        self.initMainView()

    def initModel(self):
        pass

    def initMainView(self):
        raise NotImplementedError("Child class should implement this")

    def draw(self):
        self.mainView.draw()

    def event(self, event):
        if event.type == apiVar.QUIT:
            gameapi.quit()
            sys.exit()
            
        self.mainView.event(event)
