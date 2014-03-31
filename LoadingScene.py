from Scene import *

from LoadingScreenView import LoadingScreenView


class LoadingScene(Scene):
    def initModel(self):
        pass
    
    def initMainView(self):
        self.mainView = LoadingScreenView(self, None)
