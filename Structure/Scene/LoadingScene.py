from .Scene import *

from ..View.LoadingScreenView import LoadingScreenView


class LoadingScene(Scene):
    def initModel(self):
        pass
    
    def initMainView(self):
        self.mainView = LoadingScreenView(self, None, (1000, 1000))
