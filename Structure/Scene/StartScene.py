from ..View import *
import sys, pygame


class StartScene(View):
    def __init__(self):
        start_button = pygame.image.load("Image\start_game.png")
        background = pygame.image.load("piano-photo-1.jpg")
        rect = (400,300,30,30)
        drawResizeImage (start_button, rect)
        rect = (400,300,800,600)
        drawResizeImage (background, rect)

    #def buttonPressed(self)
     #   start_button = pygame.image.load("Image\start_game_pressed.png")
      #  rect = (400,300,30,30)
       # drawResizeImage (start_button, rect)
