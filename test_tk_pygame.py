import tkinter as tk
import os

w, h = 500, 200

# Add a couple widgets. We're going to put pygame in `embed`.
root = tk.Tk()
embed = tk.Frame(root, width=w, height=h)
embed.pack()
#text = tk.Button(root, text='Blah.')
#text.pack()

# Tell pygame's SDL window which window ID to use    
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

# The wxPython wiki says you might need the following line on Windows
# (http://wiki.wxpython.org/IntegratingPyGame).
#os.environ['SDL_VIDEODRIVER'] = 'windib'

# Show the window so it's assigned an ID.
#root.update()

# Usual pygame initialization
import pygame as pg
pg.display.init()
screen = pg.display.set_mode((w,h))

pos = 0
root.withdraw() # we don't want a full GUI, so keep the root window from appearin
#print(tk.filedialog.askopenfilename())

while 1:
    # Do some pygame stuff
    screen.fill(pg.Color(0,0,0))
    pos = (pos + 1) % screen.get_width()
    pg.draw.circle(screen, pg.Color(255,255,255), (pos,100), 30)

    
    for event in pg.event.get():
        print("aaa")

    # Update the pygame display
    pg.display.flip()

    # Update the Tk display
    #root.update()
