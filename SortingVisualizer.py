import pygame
import sys
from button import TextButton, ImageButton, WHITE, BLACK
from bar import Bar

class SortingVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 560))
        pygame.display.set_caption("sortingVisualizer")
        self.clock = pygame.time.Clock()
        self.bars = [Bar() for i in range(48)]

        self.bubbleSortButton = TextButton(self.screen, 'BubbleSort', 12, 520)
        self.insertionSortButton = TextButton(self.screen, 'InsertionSort', 195, 520)
        self.startButton = ImageButton(self.screen, 'assets/start.png', 495, 514)
        self.resetButton = ImageButton(self.screen, 'assets/reset.png', 540, 514)

        self.started = False
        self.algorithm = self.bubbleSort
        self.bubbleSortButton.text_color = WHITE

        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill((100,200,0))
        self.bubbleSortButton.draw()
        self.insertionSortButton.draw()
        self.startButton.draw()
        self.resetButton.draw()

        for i, bar in enumerate(self.bars):
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

                if pos[1] > 520 and pos[1] < 565:
                    if pos[0] > 12 and pos[0] < 170:
                        self.algorithm = self.bubbleSort
                        self.bubbleSortButton.text_color = WHITE
                        self.insertionSortButton.text_color = BLACK

                    elif pos[0] > 195 and pos[0] < 385:
                        self.algorithm = self.insertionSort
                        self.insertionSortButton.text_color = WHITE
                        self.bubbleSortButton.text_color = BLACK
                    
                    elif pos[0] > self.resetButton.x and pos[0] < self.resetButton.x + 45 and not self.started:
                        self.reset()

                    elif pos[0] > self.startButton.x and pos[0] < self.startButton.x + 45 and not self.started:
                        self.start()

    def reset(self):
        self.bars = [Bar() for i in range(48)]

    def start(self):
        self.started = True
        self.algorithm()
        self.started = False

    def bubbleSort(self):
        for j in range(len(self.bars)):
            swapped = False
            i = 0
            while i < len(self.bars) - 1:
                if self.bars[i].val > self.bars[i+1].val:
                    self.bars[i].color = (0, 0, 0)
                    self.bars[i],self.bars[i+1] = self.bars[i+1],self.bars[i]
                    swapped = True
                    self.update_screen()
                    self.clock.tick(40)
                    self.bars[i+1].color = (200, 200, 200)
                i = i+1
            if swapped == False:
                break

    def insertionSort(self):
        for i in range(1, len(self.bars)):
            j = i
            while j > 0 and self.bars[j].val < self.bars[j-1].val:
                self.bars[j].color = (0, 0, 0)
                self.bars[j], self.bars[j-1] = self.bars[j-1], self.bars[j]
                j = j-1
                self.update_screen()
                self.clock.tick(40)
                self.bars[j].color = (200, 200, 200)