import os, sys
import pygame
from pygame.locals import *
class PyManMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    def MainLoop(self):
        pygame.draw.line(self.screen, (0,95,0), (0,0), (80,80), 5)
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

MainWindow = PyManMain()
MainWindow.MainLoop()