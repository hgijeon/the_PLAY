from .View import *

class StartScreenView(View):
    def onInit(self):
        self.red = gameapi.Color(255,0,0)        

    def onDraw(self):
        start_button = gameapi.image.load("Image\start_game.png")
        background = gameapi.image.load("Image\piano-photo-1.jpg")
        rect = (0,0,800,600)
        self.drawResizeImage (background, rect)
        rect = (350,400,120,120)
        self.drawResizeImage (start_button, rect)

    #def buttonPressed(self)
     #   start_button = pygame.image.load("Image\start_game_pressed.png")
      #  rect = (400,300,30,30)
       # drawResizeImage (start_button, rect)
