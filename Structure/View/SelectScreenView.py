from .View import *

from ..Scene.GameScene import GameScene

from tkinter.filedialog import askopenfilename
class SelectScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.fileSelected = False
        
    def onDraw(self):
        if self.scene.filename == None:
            self.scene.filename = ""
            self.scene.tkroot.after(0,self.fileopen)
            
        self.fill((200,200,200))
        self.drawRect(self.red, (20, 40, 400, 300))

    def onUpdateTime(self, time):
        if self.fileSelected:
            self.scene.sceneManager.pushGameScene(self.scene.filename)

    def fileopen(self):
        self.scene.filename = askopenfilename(parent=self.scene.tkroot)
        self.fileSelected = True
