from .View import *
import os

class StartScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.background = self.resizeImage(gameapi.image.load(os.path.join("Image","piano-photo-1.jpg")), (800,600))
        self.start_button = self.resizeImage(gameapi.image.load(os.path.join("Image","start_game.png")), (120, 120))
        

    def onDraw(self):
        leftTop = (0,0)
        self.drawImage (self.background, leftTop)
        leftTop = (350,400)
        self.drawImage (self.start_button, leftTop)


    def onUpdateTime(self, time):
        if self.keyMiddle.check(self.keyMiddle.key["\\"]):
            self.scene.sceneManager.setSelectScene()
            
    #def buttonPressed(self)
     #   start_button = pygame.image.load("Image\start_game_pressed.png")
      #  rect = (400,300,30,30)
       # drawResizeImage (start_button, rect)
