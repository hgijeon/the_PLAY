import pygame as gameapi
import pygame.midi as piano
import sys, random
import pygame.locals as apiVar

gameapi.init()
fpsClock = gameapi.time.Clock()

windowSurfaceObj = gameapi.display.set_mode((640, 480))
gameapi.display.set_caption('set_caption')

redColor = gameapi.Color(255,0,0)
greenColor = gameapi.Color(0,255,0)
blueColor = gameapi.Color(0,0,255)
mousex, mousey = 0,0

fontObj = gameapi.font.Font('freesansbold.ttf', 32)

mouseposMsg = ""
keypressMsg = "asdfasdfasdf"

piano.init()
piano_id = piano.get_default_input_id()
print (piano_id)
print(piano.get_device_info(piano_id))
midiInput = piano.Input(piano_id)


gameapi.fastevent.init()

while True:
    windowSurfaceObj.fill(greenColor)
    randomColor = gameapi.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    

    gameapi.draw.polygon(windowSurfaceObj, redColor, ((0,0), (10, 10), (10,0)))
    gameapi.draw.rect(windowSurfaceObj, redColor, (20, 40, 10, 10))

    pixArr = gameapi.PixelArray(windowSurfaceObj)
    for x in range(100,200,4):
        for y in range(100,200,4):
            pixArr[x][y] = redColor
    del pixArr

    msgSurfaceObj = fontObj.render(keypressMsg, False, blueColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (0,0)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

    mouseposSurfaceObj = fontObj.render(mouseposMsg, True, randomColor)
    windowSurfaceObj.blit(mouseposSurfaceObj, (mousex, mousey))


    while midiInput.poll():
        midiEvents = midiInput.read(10)
        for e in piano.midis2events(midiEvents, piano_id):
            gameapi.fastevent.post(e)
    
    for event in gameapi.fastevent.get():
        if event.type == apiVar.QUIT:
            gameapi.quit()
            sys.exit()
        elif event.type == piano.MIDIIN:
            print(event)
            '''
            print (event.data1)
            print (event.data2)
            print (event.data3)
            print (event.timestamp)
            print (event.vice_id)
            '''
            
        elif event.type == apiVar.MOUSEMOTION:
            mousex, mousey = event.pos
            mouseposMsg = str((mousex, mousey))
            
        elif event.type == apiVar.KEYDOWN:
            if event.key in (apiVar.K_LEFT, apiVar.K_RIGHT, apiVar.K_UP, apiVar.K_DOWN):
                keypressMsg = 'Arrow key pressed'
            elif event.key == apiVar.K_ESCAPE:
                gameapi.event.post(gameapi.event.Event(apiVar.QUIT))
            else:
                keypressMsg = str(event.key)
        

    gameapi.display.update()
    fpsClock.tick(30)

