from .View import *
import os
import pygame.midi as midi
from . import PianoView
from . import BlackKeyView
from . import WhiteKeyView
from . import OctaveImageView

from ..Middle.pianoKey import pianoKey

class StartScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)
        self.background = self.resizeImage(gameapi.image.load(os.path.join("Image","piano-photo-1.jpg")), (800,340))
        self.start_button = self.resizeImage(gameapi.image.load(os.path.join("Image","start_game.png")), (200, 200))
        self.keyboard = self.resizeImage(gameapi.image.load(os.path.join("Image","keyboard.png")), (800,270))
    def onDraw(self):
        self.fill((0,0,0))
        leftTop = (0,0)
        self.drawImage (self.background, leftTop)
        leftTop = (300,120)
        self.drawImage (self.start_button, leftTop)
        leftTop = (0, 340)
        self.drawImage (self.keyboard, leftTop)

    def onEvent(self, event):
        if event.type == apiVar.KEYUP or (event.type == midi.MIDIIN and ((event.status >> 4) & 0xf) == 8):
            self.scene.sceneManager.setSelectScene()
            
    #def buttonPressed(self)
     #   start_button = pygame.image.load("Image\start_game_pressed.png")
      #  rect = (400,300,30,30)
       # drawResizeImage (start_button, rect)
