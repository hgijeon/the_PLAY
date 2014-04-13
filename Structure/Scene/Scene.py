from ..Middle import gameapi
from ..Middle import apiVar
import sys

class Scene:
    def __init__(self, sceneManager, window):
        self.sceneManager = sceneManager
        self.window = window

        self.initModel()
        self.initMainView()
        print(self.__class__.__name__)

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

    def updateTime(self, time):
        self.mainView.updateTime(time)
