import pygame

pygame.init()

N = 8 
SQUARE_SIZE = 60
WIDTH, HEIGHT = N * SQUARE_SIZE, N * SQUARE_SIZE + 50
WHITE, BLACK = (245, 228, 228), (37, 27, 27)
BG = (28, 29, 37)
YELLOW = (221, 173, 97)
HINT_COLOR = YELLOW
QUEEN_IMG = pygame.image.load("assets/game-icons_chess-queen.jpg")
QUEEN_IMG = pygame.transform.scale(QUEEN_IMG, (SQUARE_SIZE, SQUARE_SIZE))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Game")

board = [[0] * N for _ in range(N)]
hint_position = None
game_over = False
game_won = False

FONT = pygame.font.Font("assets/Jaro-Regular.ttf", 30)
BUTTON_FONT = pygame.font.Font("assets/Jaro-Regular.ttf", 15)

solve_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 40, 90, 30)
hint_button = pygame.Rect(WIDTH // 2 + 10, HEIGHT - 40, 90, 30)
restart_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2, 150, 50)

def draw_board():
    screen.fill(YELLOW)
    for row in range(N):
        for col in range(N):
            color = BLACK if (row + col) % 2 else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 1:
                screen.blit(QUEEN_IMG, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    if hint_position:
        pygame.draw.rect(screen, HINT_COLOR, (hint_position[1] * SQUARE_SIZE, hint_position[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

    draw_buttons()
    
    if game_over:
        show_game_over()
    
    if game_won:
        show_game_won()

    pygame.display.update()

def is_valid_move(row, col):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == row or j == col or abs(i - row) == abs(j - col):
                    return False
    return True

def check_game_over():
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0 and is_valid_move(row, col):
                return False
    return True 

def check_game_won():
    queen_count = sum(row.count(1) for row in board)
    return queen_count == N and all(is_valid_move(i, col) for i in range(N) for col in range(N) if board[i][col] == 1)

def restart_game():
    global board, hint_position, game_over, game_won
    board = [[0] * N for _ in range(N)]
    hint_position = None
    game_over = False
    game_won = False

def auto_solve():
    global board, game_won
    board = [[0] * N for _ in range(N)]
    solve_nqueens()
    game_won = True

def solve_nqueens(row=0):
    if row == N:
        return True
    for col in range(N):
        if is_valid_move(row, col):
            board[row][col] = 1
            if solve_nqueens(row + 1):
                return True
            board[row][col] = 0
    return False

def find_hint():
    global hint_position
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0 and is_valid_move(row, col):
                hint_position = (row, col)
                return
    hint_position = None

def draw_buttons():
    pygame.draw.rect(screen, (28, 29, 37), solve_button)
    text = FONT.render("Solve", True, (245, 228, 228))
    screen.blit(text, (solve_button.x + 12, solve_button.y - 4))
    
    pygame.draw.rect(screen, (28, 29, 37), hint_button)
    text = FONT.render("Hint", True, (245, 228, 228))
    screen.blit(text, (hint_button.x + 20, hint_button.y - 4))

def show_game_over():
    popup_width = int(WIDTH * 0.7)
    popup_height = HEIGHT // 3
    popup_x = (WIDTH - popup_width) // 2
    popup_y = HEIGHT // 3

    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, (28, 29, 37), popup_rect)
    
    game_over_text1 = FONT.render("Uh..Oh..!! Game Over..!!", True, (221, 173, 97))
    game_over_text2 = FONT.render("Want to restart?", True, (221, 173, 97))
    
    screen.blit(game_over_text1, (popup_x + 30, popup_y + 20))
    screen.blit(game_over_text2, (popup_x + 60, popup_y + 60))

    restart_button = pygame.Rect(popup_x + popup_width // 2 - 40, popup_y + 120, 80, 30)
    pygame.draw.rect(screen, (245, 228, 228), restart_button)

    text = BUTTON_FONT.render("RESTART", True, (37, 27, 27))
    screen.blit(text, (restart_button.x + 15, restart_button.y + 5))

def show_game_won():
    popup_width = int(WIDTH * 0.7)
    popup_height = HEIGHT // 3
    popup_x = (WIDTH - popup_width) // 2
    popup_y = HEIGHT // 3

    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, (28, 29, 37), popup_rect)

    game_won_text1 = FONT.render("You Conquered!!", True, (221, 173, 97))
    game_won_text2 = FONT.render("Game Finish!!", True, (221, 173, 97))
    
    screen.blit(game_won_text1, (popup_x + 60, popup_y + 30))
    screen.blit(game_won_text2, (popup_x + 80, popup_y + 70))

    restart_button = pygame.Rect(popup_x + popup_width // 2 - 40, popup_y + 120, 80, 30)
    pygame.draw.rect(screen, (245, 228, 228), restart_button)

    text = BUTTON_FONT.render("RESTART", True, (37, 27, 27))
    screen.blit(text, (restart_button.x + 10, restart_button.y + 5))

running = True
while running:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if game_over or game_won:
                if restart_button.collidepoint(x, y):
                    restart_game()
            else:
                if solve_button.collidepoint(x, y):
                    auto_solve()
                elif hint_button.collidepoint(x, y):
                    find_hint()
                else:
                    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                    if row < N and is_valid_move(row, col):
                        board[row][col] = 1                  
                    if check_game_over():
                        game_over = True
                    elif check_game_won():
                        game_won = True

pygame.quit()