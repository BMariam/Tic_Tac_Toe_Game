import pygame
import sys

def start_game(screen, game_settings):
    pygame.display.update()
    screen.fill(game_settings.board_color)

    pygame.draw.line(screen, game_settings.line_color, 
         (game_settings.screen_width / 3, 0), 
         (game_settings.screen_width / 3, game_settings.screen_height), 3)
    pygame.draw.line(screen, game_settings.line_color, 
         (game_settings.screen_width * 2 / 3, 0), 
         (game_settings.screen_width * 2 / 3, game_settings.screen_height), 3)

    pygame.draw.line(screen, game_settings.line_color, 
         (0, game_settings.screen_height / 3), 
         (game_settings.screen_width, game_settings.screen_height / 3), 3)
    pygame.draw.line(screen, game_settings.line_color, 
         (0, game_settings.screen_height * 2 / 3), 
         (game_settings.screen_width, game_settings.screen_height * 2 / 3), 3)

def print_status(screen, game_settings, play_button):
    if game_settings.winner is None:
        message = 'Player:  ' + game_settings.player.upper()
    else:
        message = game_settings.winner.upper() + " won!"

    if game_settings.draw:
        message = 'Game Draw!'

    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (10, 10, 10))
    screen.fill((229, 228, 215), (402, 0, 250, 402))
    if game_settings.game_active:
        text_rect = text.get_rect(center = (game_settings.screen_width + 250 / 2, 
             game_settings.screen_height / 2))
        screen.blit(text, text_rect)
    else:
        play_button.draw_button()
    pygame.display.update()

def check_events(screen, game_settings, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_settings.game_active:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(game_settings, screen, play_button, 
                     mouse_x, mouse_y)
            elif game_settings.game_active:
                print_status(screen, game_settings, play_button)
                show_click_inputs(screen, game_settings, play_button)
                if (game_settings.winner or game_settings.draw):
                    game_settings.reset_game()

def show_click_inputs(screen, game_settings, play_button):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col_width = game_settings.screen_width / 3
    row_height = game_settings.screen_height / 3

    if (mouse_x > 0 and mouse_x < game_settings.screen_width):
        col = int(mouse_x // col_width)
    else:
        col = None

    if (mouse_y > 0 and mouse_y < game_settings.screen_height):
        row = int(mouse_y // row_height)
    else:
        row = None

    if (col != None and row != None and False == game_settings.board[row][col]):
        draw_player(screen, col_width, row_height, row, col, game_settings)
        game_settings.step += 1
        if (5 <= game_settings.step):
            check_win(screen, game_settings)
        print_status(screen, game_settings, play_button)
        if game_settings.winner or game_settings.draw:
            pygame.time.delay(1000)

def draw_player(screen, col_width, row_height, row, col, game_settings):
    game_settings.board[row][col] = game_settings.player
    pos_x = col_width * col + ((col_width - col_width * 2 / 3) / 2)
    pos_y = row_height * row + ((col_width - col_width * 2 / 3) / 2)
    if ('x' == game_settings.player):
        screen.blit(game_settings.x_img, (pos_x, pos_y))
        game_settings.player = 'o'
    else:
        screen.blit(game_settings.o_img, (pos_x, pos_y))
        game_settings.player = 'x'
    pygame.display.update()

def check_win(screen, game_settings):  
    for row in range(3):
        if (False != bool(game_settings.board[row][0])):
            if (game_settings.board[row][0] == game_settings.board[row][1]
                 == game_settings.board[row][2]):
                row_height = game_settings.screen_height / 3 
                game_settings.winner = game_settings.board[row][0]
                pygame.draw.line(screen, game_settings.win_line_color, 
                     (10, row * row_height + row_height / 2), 
                     (row_height * 3 - 10, row * row_height 
                     + row_height / 2), 7)
                return           

    for col in range(3):
        if (False != bool(game_settings.board[0][col])):
            if (game_settings.board[0][col] == game_settings.board[1][col]
                 == game_settings.board[2][col]):
                col_width = game_settings.screen_width / 3
                game_settings.winner = game_settings.board[0][col]
                pygame.draw.line(screen, game_settings.win_line_color, 
                     (col * col_width + col_width / 2,  10), 
                     (col * col_width + col_width / 2, 
                     col_width * 3 - 10), 7)
                return 

    if (False != bool(game_settings.board[0][0])):
        if (game_settings.board[0][0] == game_settings.board[1][1] 
             == game_settings.board[2][2]):   
            game_settings.winner = game_settings.board[0][0]
            pygame.draw.line(screen, game_settings.win_line_color, (10, 10), 
                 (game_settings.screen_width - 10, 
                 game_settings.screen_height - 10), 7)
            return 

    if (False != bool(game_settings.board[0][2])):
        if (game_settings.board[0][2] == game_settings.board[1][1] 
             == game_settings.board[2][0]):   
            game_settings.winner = game_settings.board[0][2]
            pygame.draw.line(screen, game_settings.win_line_color, 
                 (game_settings.screen_width - 10, 10), 
                 (10, game_settings.screen_height - 10), 7)
            return

    if (all([all(row) for row in game_settings.board]) 
         and game_settings.winner is None):
        game_settings.draw = True
   
def check_play_button(game_settings, screen, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_settings.game_active:
        start_game(screen, game_settings)
        game_settings.reset_game()      
        game_settings.game_active = True           
    
