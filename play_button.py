import pygame.font

class PlayButton:
    def __init__(self, game_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_rect.center = (game_settings.screen_width / 2, 
             game_settings.screen_height / 2)

        self.width, self.height = 180, 50
        self.button_color = (10, 10, 10)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (game_settings.screen_width + 250 / 2, 50)

        self.msg_image = self.font.render(message, True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
       
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

