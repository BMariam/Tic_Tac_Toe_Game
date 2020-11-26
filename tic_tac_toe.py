import pygame
import sys
import game_functions as gf
from settings import Settings
from play_button import PlayButton

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width + 250,
            game_settings.screen_height))
    pygame.display.set_caption("Tic Tac Toe")
    play_button = PlayButton(game_settings, screen, "Play")
    gf.start_game(screen, game_settings)

    run = True
    while run:
        gf.print_status(screen, game_settings, play_button)
        gf.check_events(screen, game_settings, play_button)
        pygame.display.update()
        pygame.time.Clock().tick(30)    
    pygame.quit()   

run_game()
