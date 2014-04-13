from ..Scene.GameScene import GameScene



class SceneManager:
    def __init__(self, startSceneClass, window, tkroot = None):

        self.tkroot = tkroot
        self.startWindow = window
        scene = startSceneClass(self, window)
        self.sceneStack = [scene]

        
    def getScene(self):
        return self.sceneStack[-1]


    def pushGameScene(self, filename):
        scene = GameScene(self, self.startWindow)
        scene.setSong(filename)
        self.sceneStack.append(scene)
