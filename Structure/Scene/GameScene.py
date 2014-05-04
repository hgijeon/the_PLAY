from .Scene import *

from ..View.GameScreenView import GameScreenView
from ..Middle.pianoKey import pianoKey

import os

class GameScene(Scene):
    def initModel(self):
        self.dotStartY = -300
        self.lineY = 100
        self.dotEndY = 300
        self.setDotSpeed(150)

        self.scoreFont = gameapi.font.Font('freesansbold.ttf', 32)
        self.score = 0

        self.octWidth = 266
        self.octHeight = 200
        tmp = gameapi.image.load(os.path.join("Image","1_octive_black.png"))
        self.octaveImg = gameapi.transform.scale(tmp, (self.octWidth, self.octHeight))

        self.whiteWidth = self.octWidth/7
        self.whiteHeight = self.octHeight
        self.blackWidth = self.octWidth * 0.095
        self.blackHeight = self.octHeight * 0.68

        self.blackDot = gameapi.image.load(os.path.join("Image","black dot.png"))
        self.whiteDot = gameapi.image.load(os.path.join("Image","white dot.png"))

        self.playTime = 0
        self.play = True

        self.pianoKeyObserver = []

    def setSong(self, path):
        self.filepath = path
        key = pianoKey(path)
        key.scene = self

        self.midiEndTime = key.endTime + self.startTimeOffset - self.endTimeOffset

        for e in self.pianoKeyObserver:
            e.setMiddle(key)
        

    def setDotSpeed(self, pixelPerSecond):
        self.dotSpeed = pixelPerSecond
        self.startTimeOffset = (self.lineY - self.dotStartY) / pixelPerSecond
        self.endTimeOffset = (self.lineY - self.dotEndY) / pixelPerSecond
    
    def initMainView(self):
        self.mainView = GameScreenView(self, None, (1000, 1000))

    def updateTime(self, time):
        try:
            if self.play:
                self.playTime += time - self.prevTime
        except:
            self.prevTime = time
        self.prevTime = time

        if self.playTime > self.midiEndTime:
            print("MIDI end")
            self.sceneManager.setRankingScene(self.filepath)

        super().updateTime(time)
        
