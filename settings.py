import pygame

class Settings:
    def __init__(self):
        self.screen_height = 402
        self.screen_width = 402
        self.board_color = (204, 255, 239)
        self.line_color = (0, 0, 0)
        self.win_line_color = (10, 10, 10)

        self.step = 0
        self.player = 'x'
        self.winner = None
        self.draw = False
        self.board = [[False] * 3, [False] * 3, [False] * 3]
        self.game_active = False

        self.x_img = pygame.image.load('images/x.png')
        self.x_img = pygame.transform.scale(self.x_img, 
            (int(self.screen_width * 2 // 9), int(self.screen_height * 2 // 9)))

        self.o_img = pygame.image.load('images/o.png')
        self.o_img = pygame.transform.scale(self.o_img, 
            (int(self.screen_width * 2 // 9), int(self.screen_height * 2 // 9)))

    def reset_game(self):
        self.step = 0
        self.player = 'x'
        self.winner = None
        self.draw = False
        self.board = [[False] * 3, [False] * 3, [False] * 3]
        self.game_active = False
        
