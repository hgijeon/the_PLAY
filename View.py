import gameapi
import apiVar

from RefVector import RefVector

class View:
    def __init__(self, scene, parentView, wh, offsetRefVec = RefVector()):
        self.childList = []
        
        self.scene = scene
        self.parentView = parentView
        self.offsetRefVec = offsetRefVec
        #self.surface = gameapi.Surface(wh, apiVar.SRCALPHA)

        self.onInit()
        

    def draw(self, refVec = RefVector()):
        self.absRefVec = refVec + self.offsetRefVec
        #self.surface.fill((0,0,0,0))
        self.onDraw()
        #self.scene.window.blit(self.surface, absRefVec.lt)
        
        for child in self.childList:
            child.draw(self.absRefVec)

    def event(self, eventObj):
        for child in self.childList:
            child.event(eventObj)
            
        self.onEvent(eventObj)

    def updateTime(self, time):
        for child in self.childList:
            child.updateTime(time)
            
        self.onUpdateTime(time)

    def drawRect(self, color, rect):
        cvrt=(rect[0]+self.absRefVec.lt[0],rect[1]+self.absRefVec.lt[1],rect[2],rect[3]) 
        gameapi.draw.rect(self.scene.window, color, cvrt)
        #gameapi.draw.rect(self.surface, color, rect)

    def fill(self, color):
        self.scene.window.fill(color)

    def onInit(self):
        pass

    def onDraw(self):
        pass

    def onEvent(self, eventObj):
        pass

    def onUpdateTime(self, time):
        pass
