from .Scene import *

from ..View.SelectScreenView import SelectScreenView

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from threading import Thread as thread

class SelectScene(Scene):
    def initModel(self):
        self.tkroot = self.sceneManager.tkroot
        self.filename = None
        
        
    
    def initMainView(self):
        self.mainView = SelectScreenView(self, None)
