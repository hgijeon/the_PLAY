from .View import *
import os
import pygame.midi as midi

class StartScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.background = self.resizeImage(gameapi.image.load(os.path.join("Image","piano-photo-1.jpg")), (800,450))
        self.start_button = self.resizeImage(gameapi.image.load(os.path.join("Image","start_game.png")), (200, 200))
        

    def onDraw(self):
        leftTop = (0,0)
        self.drawImage (self.background, leftTop)
        leftTop = (300,200)
        self.drawImage (self.start_button, leftTop)


    def onEvent(self, event):
        if event.type == apiVar.KEYUP or (event.type == midi.MIDIIN and ((event.status >> 4) & 0xf) == 8):
            self.scene.sceneManager.setSelectScene()
            
    #def buttonPressed(self)
     #   start_button = pygame.image.load("Image\start_game_pressed.png")
      #  rect = (400,300,30,30)
       # drawResizeImage (start_button, rect)
