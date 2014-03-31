import gameapi
import apiVar

from RefVector import RefVector

class View:
    def __init__(self, scene, parentView, offsetRefVec = RefVector()):
        self.childList = []
        
        self.scene = scene
        self.parentView = parentView
        self.offsetRefVec = offsetRefVec

        self.onInit()
        

    def draw(self, refVec = RefVector()):
        self.absRefVec = refVec + self.offsetRefVec
        gameapi.refVec = self.absRefVec

        self.onDraw()
        
        for child in self.childList:
            child.draw(self.absRefVec)

    def event(self, eventObj):
        for child in self.childList:
            child.event(eventObj)
            
        self.onEvent(eventObj)
        

    def onInit(self):
        pass

    def onDraw(self):
        pass

    def onEvent(self, eventObj):
        pass
