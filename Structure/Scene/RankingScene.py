from .Scene import *

from ..View.RankingScreenView import RankingScreenView
from ..Model.Score import HighScore

rankN = 5

class RankingScene(Scene):
    def initModel(self):
        self.font = gameapi.font.Font('freesansbold.ttf', 32)        
        self.filepath = None
        self.nameEntered = False
        self.doneTime = None

    def initMainView(self):
        self.mainView = RankingScreenView(self, None)

    def setTarget(self, filepath, score):
        self.filepath = filepath
        self.score = score
        
        self.highScore = HighScore()
        self.highScore.loadFile()

        (self.song, self.rank) = self.highScore.getTarget(filepath, score)
        if self.rank >= rankN:
            self.done()

    def addLetter(self, ch):
        if self.nameEntered == False:
            self.song.slotList[self.rank].name += ch

    def done(self):
        self.highScore.saveFile()
        self.nameEntered = True

    def getSong(self):
        return self.song

    def updateTime(self, time):
        if self.nameEntered:
            if self.doneTime == None:
                self.doneTime = time
            elif time - self.doneTime > 5:
                self.sceneManager.setSelectScene()
                           
        super().updateTime(time)
