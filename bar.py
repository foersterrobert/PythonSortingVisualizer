import pygame
import random

class BarS:
    def __init__(self):
        self.val = random.randint(1, 100)
        self.color = (200, 200, 200)

    def draw(self, screen, i):
        pygame.draw.rect(screen, self.color, (i*12+12, 10, 10, self.val*5))