import gameapi
import apiVar

from RefVector import RefVector

class View:
    def __init__(self, scene, parentView, wh, offsetRefVec = RefVector()):
        self.childList = []
        
        self.scene = scene
        self.parentView = parentView
        self.offsetRefVec = offsetRefVec
        self.surface = gameapi.Surface(wh, apiVar.SRCALPHA)

        self.onInit()
        

    def draw(self, refVec = RefVector()):
        absRefVec = refVec + self.offsetRefVec
        self.surface.fill((0,0,0,0))
        self.onDraw()
        self.scene.window.blit(self.surface, absRefVec.lt)
        
        for child in self.childList:
            child.draw(absRefVec)

    def event(self, eventObj):
        for child in self.childList:
            child.event(eventObj)
            
        self.onEvent(eventObj)

    def updateTime(self, time):
        for child in self.childList:
            child.updateTime(time)
            
        self.onUpdateTime(time)

    def drawRect(self, color, rect):
        gameapi.draw.rect(self.surface, color, rect)

    def onInit(self):
        pass

    def onDraw(self):
        pass

    def onEvent(self, eventObj):
        pass

    def onUpdateTime(self, time):
        pass
