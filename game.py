import pygame


pygame.init()

ROWS = COLS = 8
SQUARE_LENGTH = 75
SCREEN_WIDTH,SCREEN_HEIGHT = SQUARE_LENGTH * ROWS,SQUARE_LENGTH * COLS + 100

BOARD_WIDTH,BOARD_HEIGHT = SQUARE_LENGTH * ROWS, SQUARE_LENGTH * COLS

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)

board = [[None for _ in range(COLS)] for _ in range(ROWS)]
board[3][3] = 'W'
board[3][4] = 'B'
board[4][3] = 'B'
board[4][4] = 'W'

squares_without_piece = {(i,j) for i in range(ROWS) for j in range(COLS)}
squares_without_piece.remove((4,4))
squares_without_piece.remove((3,4))
squares_without_piece.remove((4,3))
squares_without_piece.remove((3,3))


BLACK = (0,0,0)
WHITE = (255,255,255)
def draw_board():


    for x in range(0,BOARD_WIDTH,SQUARE_LENGTH):
        pygame.draw.line(screen,BLACK,(x,0),(x,BOARD_HEIGHT))


    for y in range(0,BOARD_HEIGHT + 1,SQUARE_LENGTH):
        pygame.draw.line(screen,BLACK,(0,y),(BOARD_WIDTH,y))

#    pygame.draw.line(screen,BLACK,(0,BOARD_HEIGHT),(BOARD_WIDTH,BOARD_HEIGHT))


    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "W":
                pygame.draw.circle(screen,WHITE,(col * SQUARE_LENGTH + SQUARE_LENGTH//2,row * SQUARE_LENGTH + SQUARE_LENGTH//2),SQUARE_LENGTH//2)
            elif board[row][col] == "B":
                pygame.draw.circle(screen,BLACK,(col * SQUARE_LENGTH + SQUARE_LENGTH//2,row * SQUARE_LENGTH + SQUARE_LENGTH//2),SQUARE_LENGTH//2)

            if (row,col) in valid_moves:
                pygame.draw.circle(screen,(255,0,0),(col * SQUARE_LENGTH + SQUARE_LENGTH//2,row * SQUARE_LENGTH + SQUARE_LENGTH//2),5)





def check_any_valid_moves():
    opposite_color = 'W' if turn == 'B' else 'B'
    functions = [check_left,check_right,check_up,check_down,check_up_left,check_up_right,check_down_left,check_down_right]

    valid_moves = set()
    for row,col in squares_without_piece:
        for function in functions:
            result,_ = function(row,col,opposite_color,checking=True)
            if result:
                valid_moves.add((row,col))

        #if any(function(row,col,opposite_color) for function in functions):
#            return True
    

    return valid_moves





def check_if_row_and_col_valid(row,col):
    global WHITE_COUNT,BLACK_COUNT
    opposite_color = 'W' if turn == 'B' else 'B'
    
    
    functions = [check_left,check_right,check_up,check_down,check_up_left,check_up_right,check_down_left,check_down_right]
    
    result = False
    for function in functions:

        function_result,function_switches = function(row,col,opposite_color)

        result = result or function_result

        if turn == 'B':
            BLACK_COUNT += function_switches
            WHITE_COUNT -= function_switches
        else:
            WHITE_COUNT += function_switches
            BLACK_COUNT -= function_switches
    

    return result










def check_left(row,col,opposite_color,checking=False):

    
    count = 0

    current_row,current_col =row, col - 1


    while current_col >= 0 and board[current_row][current_col] == opposite_color:
        current_col -= 1
        count += 1
    

    if current_col >= 0 and board[current_row][current_col] == turn and count >= 1:
    # go backwards to switch
        current_col += 1
    
        switches = 0
        if not checking:
            while board[row][current_col] != None:
                board[row][current_col] = turn
                switches += 1
                current_col += 1



        return True,switches


    return False,0






def check_right(row,col,opposite_color,checking=False):
    

    count = 0

    current_col = col + 1

    while current_col < len(board[0]) and board[row][current_col] == opposite_color:
        current_col += 1
        count += 1
    
    if current_col < len(board[0]) and board[row][current_col] == turn and count >= 1:
        current_col -= 1


        switches = 0
        if not checking:
            while board[row][current_col] != None:
                board[row][current_col] = turn
                switches += 1
                current_col -= 1

    
        return True,switches

    return False,0












def check_up(row,col,opposite_color,checking=False):
    

    count = 0

    current_row = row - 1

    while current_row >= 0 and board[current_row][col] == opposite_color:
        current_row -= 1
        count += 1


    if current_row >= 0 and board[current_row][col] == turn and count >= 1:
        current_row += 1
        
        switches = 0
        if not checking:
            while board[current_row][col] != None:
                board[current_row][col] = turn
                current_row += 1
                switches += 1



        return True,switches
    
    return False,0


def check_down(row,col,opposite_color,checking=False):
    
    count = 0

    current_row = row + 1


    while current_row < len(board) and board[current_row][col] == opposite_color:
        current_row += 1
        count += 1


    if current_row < len(board) and board[current_row][col] == turn and count >= 1:
        current_row -= 1
        
        switches = 0
        if not checking:
            while board[current_row][col] != None:
                board[current_row][col] = turn
                current_row -= 1
                switches += 1

        return True,switches

    return False,0





def check_up_left(row,col,opposite_color,checking=False):

    
    count = 0
    current_row,current_col = row - 1,col - 1


    while current_row >= 0 and current_col >= 0 and board[current_row][current_col] == opposite_color:
        count += 1
        current_row -= 1
        current_col -= 1


    if current_row >=0 and current_col >= 0 and board[current_row][current_col] == turn and count >= 1:
        current_row += 1
        current_col += 1
        
        switches = 0
        if not checking:
            while board[current_row][current_col] != None:
                board[current_row][current_col] = turn
                current_row += 1
                current_col += 1
                switches += 1

        return True,switches

    return False,0






def check_up_right(row,col,opposite_color,checking=False):

    count = 0

    current_row,current_col = row - 1,col + 1


    while current_row >= 0 and current_col < len(board[0]) and board[current_row][current_col] == opposite_color:
        count += 1
        current_row -= 1
        current_col += 1


    if current_row >=0 and current_col < len(board[0]) and board[current_row][current_col] == turn and count >= 1:
        current_row += 1
        current_col -= 1
        switches = 0
        if not checking:
            while board[current_row][current_col] != None:
                board[current_row][current_col] = turn
                current_row += 1
                current_col -= 1
                switches += 1


        return True,switches

    return False,0



def check_down_left(row,col,opposite_color,checking=False):
    
    count = 0

    current_row,current_col = row +1,col - 1

    while current_row < len(board) and current_col >= 0 and board[current_row][current_col] == opposite_color:
        count += 1
        current_row += 1
        current_col -= 1


    if current_row < len(board) and current_col >= 0 and board[current_row][current_col] == turn and count >= 1:
        current_row -= 1
        current_col += 1
        
        switches = 0
        if not checking:
            while board[current_row][current_col] != None:
                board[current_row][current_col] = turn
                current_row -= 1
                current_col += 1


        return True,switches

    return False,0

def update_colors(row,col):
    global BLACK_COUNT,WHITE_COUNT
    functions = [check_left,check_right,check_up,check_down,check_up_left,check_up_right,check_down_left,check_down_right]


    for function in functions:

        _,switches = function(row,col,None)

        if turn == 'B':
            BLACK_COUNT += switches
            WHITE_COUNT -= switches
        else:
            WHITE_COUNT += switches
            BLACK_COUNT -= switches







def check_down_right(row,col,opposite_color,checking=False):
    

    count = 0

    current_row,current_col = row + 1,col + 1

    while current_row < len(board) and current_col < len(board[0]) and board[current_row][current_col] == opposite_color:
        count += 1
        current_row += 1
        current_col += 1

    if current_row < len(board) and current_col < len(board[0]) and board[current_row][current_col] == turn and count >= 1:
        current_row -= 1

        current_col -= 1
        switches = 0
        if not checking:
            while board[current_row][current_col] != None:
                board[current_row][current_col] = turn
                current_row -= 1
                current_col -= 1
                switches += 1

        return True,switches




    return False,0




    







pygame.display.set_caption("Othello")

done = False

DARK_GREEN = (0,100,0)

surface = pygame.Surface((SQUARE_LENGTH,SQUARE_LENGTH),pygame.SRCALPHA)
turn = 'W'

color = (255,255,255,50)


color_to_word = {'W': 'WHITE','B': 'BLACK'}
turn_to_color = {'W': (255,255,255),'B': (0,0,0)}


font = pygame.font.SysFont("comicsansms",42)
skipping_turn_font = pygame.font.SysFont("comicsansms",21)
info_text = font.render(f"{color_to_word[turn]}'S TURN",True,turn_to_color[turn])

BLACK_COUNT = WHITE_COUNT = 2

black_count_text = font.render(f"{BLACK_COUNT:02}",True,(0,0,0))
white_count_text = font.render(f"{WHITE_COUNT:02}",True,(255,255,255))
game_over = False
turns = 0


valid_moves = check_any_valid_moves()
no_more_moves = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif not game_over and event.type ==pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            row,col = y//SQUARE_LENGTH,x//SQUARE_LENGTH
            if board[row][col] == None:
                if (row,col) in valid_moves:
                    check_if_row_and_col_valid(row,col)
                    board[row][col] = turn
                    squares_without_piece.remove((row,col))
                    turns += 1
                    if turn == 'B':
                        BLACK_COUNT += 1
                    else:
                        WHITE_COUNT += 1
                    
                    if turn == 'W':
                        turn = 'B'
                        color = (0,0,0,50)
                    else:
                        turn = 'W'
                        color = (255,255,255,50)
                    valid_moves = check_any_valid_moves()
                    if not valid_moves:
                        turn = 'B' if turn == 'W' else 'W'
                        valid_moves = check_any_valid_moves()
                        if not valid_moves:
                            no_more_moves = True
                        else:
                            opposite = 'BLACK' if turn == 'W' else 'WHITE'
                            info_text =skipping_turn_font.render(f"NO MOVES! SKIPPING {opposite}'S TURN!",True,(255,0,0))
                            screen.fill(DARK_GREEN)
                            draw_board()
                            screen.blit(info_text,(BOARD_WIDTH//2 - info_text.get_width()//2,BOARD_HEIGHT + (SCREEN_HEIGHT -BOARD_HEIGHT)//2 - info_text.get_height()//2))

                            pygame.display.update()
                            color = (255,255,255,50) if turn == 'W' else (0,0,0,50)
                            pygame.time.delay(2000)


                    if no_more_moves:
                        game_over = True
                        info_text = font.render(f"NO MORE MOVES LEFT",True,(255,0,0))
                        screen.fill(DARK_GREEN)
                        draw_board()
                        screen.blit(info_text,(BOARD_WIDTH//2 - info_text.get_width()//2,BOARD_HEIGHT + (SCREEN_HEIGHT -BOARD_HEIGHT)//2 - info_text.get_height()//2))

                        pygame.display.update()
                        pygame.time.delay(1000)
                        game_over = True
                        winner = 'BLACK' if BLACK_COUNT > WHITE_COUNT else 'WHITE' if WHITE_COUNT > BLACK_COUNT else 'DRAW'

                        if winner == "DRAW":
                            info_text = font.render("DRAW!",True,(255,0,0))
                        else:
                            info_text = font.render(f"{winner} WINS!!!",True,BLACK if winner == 'BLACK' else WHITE)
                        black_count_text = font.render(f"{BLACK_COUNT:02}",True,(0,0,0))
                        white_count_text = font.render(f"{WHITE_COUNT:02}",True,(255,255,255))
                        break


                    info_text = font.render(f"{color_to_word[turn]}'S TURN",True,turn_to_color[turn])
                    black_count_text = font.render(f"{BLACK_COUNT:02}",True,(0,0,0))
                    white_count_text = font.render(f"{WHITE_COUNT:02}",True,(255,255,255))
                else:
                    info_text = font.render("INVALID MOVE!",True,(255,0,0))
                    screen.fill(DARK_GREEN)
                    draw_board()
                    screen.blit(info_text,(BOARD_WIDTH//2 - info_text.get_width()//2,BOARD_HEIGHT + (SCREEN_HEIGHT -BOARD_HEIGHT)//2 - info_text.get_height()//2))

                    pygame.display.update()
                    pygame.time.delay(500)
                    info_text = font.render(f"{color_to_word[turn]}'s TURN",True,turn_to_color[turn])





    x,y = pygame.mouse.get_pos()
    row,col = y//SQUARE_LENGTH,x//SQUARE_LENGTH

    screen.fill(DARK_GREEN)
    draw_board()

    if pygame.mouse.get_focused() and 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT and board[row][col] == None:
        pygame.draw.circle(surface,color,(SQUARE_LENGTH//2,SQUARE_LENGTH//2),SQUARE_LENGTH//2)
        #pygame.draw.rect(surface,BLACK,(0,0,SQUARE_LENGTH,SQUARE_LENGTH),1)
        screen.blit(surface,(col * SQUARE_LENGTH,row * SQUARE_LENGTH))

    screen.blit(info_text,(BOARD_WIDTH//2 - info_text.get_width()//2,BOARD_HEIGHT + (SCREEN_HEIGHT -BOARD_HEIGHT)//2 - info_text.get_height()//2))

    screen.blit(black_count_text,(3,BOARD_HEIGHT))
    screen.blit(white_count_text,(3,SCREEN_HEIGHT -2  - white_count_text.get_height()))
    pygame.display.update()











