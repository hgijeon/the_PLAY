from .Scene import *

from ..View.StartScreenView import StartScreenView

class StartScene(Scene):
    def initModel(self):
        pass

    def initMainView(self):
        self.mainView = StartScreenView(self, None)
