from .Scene import *

from ..View.SelectScreenView import SelectScreenView


class SelectScene(Scene):
    def initModel(self):
        pass
    
    def initMainView(self):
        self.mainView = SelectScreenView(self, None)
