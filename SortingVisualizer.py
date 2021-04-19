import random
import pygame
import sys
import time
from button import Button
from bar import BarS


class SortingVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 560))
        pygame.display.set_caption("sortingVisualizer")
        self.clock = pygame.time.Clock()
        self.n = [BarS() for i in range(48)]

        self.bButton = Button(self.screen, 'Bubblesort', 20, 520)
        self.sButton = Button(self.screen, 'start', 410, 520)
        self.rButton = Button(self.screen, 'reset', 500, 520)

        self.started = False

        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill((100,200,0))
        self.bButton.draw_button()
        self.sButton.draw_button()
        self.rButton.draw_button()

        for i, bar in enumerate(self.n):
            bar.draw(self.screen, i)
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.started:
                        self.start()

            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                
                if pos[0] > self.rButton.x and pos[0] < self.rButton.x + self.rButton.msg_image.get_width():
                    self.reset()

                elif pos[0] > self.sButton.x and pos[0] < self.sButton.x + self.sButton.msg_image.get_width() and not self.started:
                    self.start()

    def reset(self):
        self.started = False
        self.n = [BarS() for i in range(48)]

    def start(self):
        self.started = True
        self.BubbleSort()

    def BubbleSort(self):
        for j in range(len(self.n)):
            swapped = False
            i = 0
            while i < len(self.n) - 1:
                if self.n[i].val > self.n[i+1].val:
                    self.n[i].color = (0, 0, 0)
                    self.n[i],self.n[i+1] = self.n[i+1],self.n[i]
                    swapped = True
                    self.update_screen()
                    self.clock.tick(40)
                    self.n[i+1].color = (200, 200, 200)
                i = i+1
            if swapped == False:
                break