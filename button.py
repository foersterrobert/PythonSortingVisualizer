import pygame.font

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class TextButton():
    def __init__(self, screen, msg, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg
        self.width, self.height = 100, 50
        self.text_color = BLACK
        self.font = pygame.font.SysFont(None, 44)

    def draw(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, None)
        self.screen.blit(self.msg_image, (self.x, self.y))

class ImageButton():
    def __init__(self, screen, image, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (42, 42))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))