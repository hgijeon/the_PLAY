from .Scene import *

from ..View.RankingScreenView import RankingScreenView
from ..Model.Score import HighScore

class RankingScene(Scene):
    def initModel(self):
        self.font = gameapi.font.Font('freesansbold.ttf', 32)        
        self.filepath = None

    def initMainView(self):
        self.mainView = RankingScreenView(self, None)

    def setTarget(self, filepath, score):
        self.filepath = filepath
        self.score = score
        
        self.highScore = HighScore()
        self.highScore.loadFile()

        (self.song, self.rank) = self.highScore.getTarget(filepath, score)
        self.song.slotList[self.rank].name = 'testtest'

        self.highScore.saveFile()

    def getSong(self):
        return self.song
