from .Scene import *

from ..View.RankingScreenView import RankingScreenView

class RankingScene(Scene):
    def initModel(self):
        self.filepath = None

    def initMainView(self):
        self.mainView = RankingScreenView(self, None)

    def setFile(self, filepath):
        self.filepath = filepath
