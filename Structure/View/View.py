from ..Middle import gameapi
from ..Middle import apiVar

from ..Model.RefVector import RefVector

class View:
    def __init__(self, scene, parentView, wh=None, offsetRefVec = RefVector()):
        self.childList = []
        
        self.scene = scene
        self.parentView = parentView
        self.offsetRefVec = offsetRefVec
        #self.surface = gameapi.Surface(wh, apiVar.SRCALPHA)

        self.setKeyMiddle()

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

    def drawRect(self, color, rect, width = 0):
        cvrt=(rect[0]+self.absRefVec.lt[0],rect[1]+self.absRefVec.lt[1],rect[2],rect[3]) 
        gameapi.draw.rect(self.scene.window, color, cvrt, width)
        #gameapi.draw.rect(self.surface, color, rect)

    def drawChar(self, string, offset, fontObj):
        tmp = fontObj.render(string, True, (0,0,0))
        cvrt = (offset[0]+self.absRefVec.lt[0], offset[1]+self.absRefVec.lt[1])
        self.scene.window.blit(tmp, cvrt)

    def drawResizeImage(self, image, rect):
        surf = gameapi.transform.smoothscale(image, (int(rect[2]),int(rect[3])))
        cvrt = (rect[0]+self.absRefVec.lt[0], rect[1]+self.absRefVec.lt[1])
        self.scene.window.blit(surf,cvrt)

    def resizeImage(self, image, wh):
        surf = gameapi.transform.smoothscale(image, (int(wh[0]),int(wh[1])))
        return surf

    def drawImage(self, image, lt):
        cvrt = (lt[0]+self.absRefVec.lt[0], lt[1]+self.absRefVec.lt[1])
        self.scene.window.blit(image, cvrt)
    
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

    def setKeyMiddle(self):
        self.keyMiddle = self.scene.sceneManager.keyMiddle
