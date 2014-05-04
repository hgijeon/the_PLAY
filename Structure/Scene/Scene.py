from ..Middle import gameapi
from ..Middle import apiVar
import pygame.midi as midi

import sys

class Scene:
    def __init__(self, sceneManager, window):
        self.sceneManager = sceneManager
        self.window = window

        self.setKeyMiddle()

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

        if event.type == apiVar.KEYDOWN or event.type == apiVar.KEYUP or event.type == midi.MIDIIN:
            self.keyMiddle.updateStatus(event)
        self.mainView.event(event)

    def updateTime(self, time):
        self.mainView.updateTime(time)

    def setKeyMiddle(self):
        self.keyMiddle = self.sceneManager.keyMiddle
