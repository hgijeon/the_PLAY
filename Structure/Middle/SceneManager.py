from ..Scene.GameScene import GameScene

from tkinter import Tk
from tkinter.filedialog import askopenfilename


class SceneManager:
    def __init__(self, startSceneClass, window):
        self.initModel()
        self.startWindow = window
        scene = startSceneClass(self, window)
        self.sceneStack = [scene]

        if isinstance(scene, GameScene):
#            root = Tk()
#            root.withdraw() # we don't want a full GUI, so keep the root window from appearing
 
#            scene.setSong(askopenfilename())
            scene.setSong("Music/minuet1track.mid")
            
    def startWith(self, startScene):
        self.sceneStack = [startScene]

    def pushScene(self, scene):
        self.sceneStack.push(scene)

    def popScene(self):
        return self.sceneStack.pop()

    def setScene(self, scene):
        self.sceneStack[-1] = scene

    def getScene(self):
        return self.sceneStack[-1]

    def initModel(self):
        pass
