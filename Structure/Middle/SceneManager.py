from ..Scene.GameScene import GameScene

class SceneManager:
    def __init__(self, startSceneClass, window):
        self.initModel()
        self.startWindow = window
        scene = startSceneClass(self, window)
        self.sceneStack = [scene]

        if isinstance(scene, GameScene):
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
