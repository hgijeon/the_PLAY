from ..Scene.GameScene import GameScene
from ..Scene.SelectScene import SelectScene
from ..Scene.RankingScene import RankingScene
from .KeyMiddle import KeyMiddle

class SceneManager:
    def __init__(self, startSceneClass, window, tkroot = None):
        self.keyMiddle = KeyMiddle()
        self.tkroot = tkroot
        self.startWindow = window

        scene = startSceneClass(self, window)
        self.sceneStack = [scene]


        
    def getScene(self):
        return self.sceneStack[-1]


    def pushGameScene(self, filepath):
        scene = GameScene(self, self.startWindow)
        scene.setSong(filepath)
        self.sceneStack[-1] = scene

    def setSelectScene(self):
        scene = SelectScene(self, self.startWindow)
        self.sceneStack[-1] = scene

    def setRankingScene(self, filepath, score):
        scene = RankingScene(self, self.startWindow)
        scene.setTarget(filepath,score)
        self.sceneStack[-1] = scene
    
        
