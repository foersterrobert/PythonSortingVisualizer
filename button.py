import pygame.font

WHITE = (255, 255, 255)

class Button():
    def __init__(self, screen, msg, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg

        self.width, self.height = 100, 50
        self.button_color = (0, 255, 0)
        self.text_color = WHITE
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(self.x - (20), self.y - (10), self.width, self.height)
        # self.rect.center = (self.x, self.y)


    def draw_button(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, None)
        self.screen.blit(self.msg_image, (self.x, self.y))