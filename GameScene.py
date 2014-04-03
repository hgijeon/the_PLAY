from Scene import *

from GameScreenView import GameScreenView


class GameScene(Scene):
    def initModel(self):
        pass
    
    def initMainView(self):
        self.mainView = GameScreenView(self, None)
