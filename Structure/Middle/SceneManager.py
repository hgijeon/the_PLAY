
class SceneManager:
    def __init__(self, startSceneClass, window):
        self.initModel()
        self.startWindow = window
        self.sceneStack = [startSceneClass(self, window)]

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
