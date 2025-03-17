import pygame
import subprocess
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
WHITE = (245, 228, 228)
BLACK = (37, 27, 27)
BG = (28, 29, 37)

FONT = pygame.font.Font("assets/Jaro-Regular.ttf", 40)
BUTTON_FONT = pygame.font.Font("assets/Jaro-Regular.ttf", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to N-Queens Game")

yes_button = pygame.Rect(WIDTH // 2 - 100, 380, 100, 40)
quit_button = pygame.Rect(WIDTH // 2 + 20, 380, 100, 40)

def welcome_screen():
    screen.fill(BG)
    
    title = FONT.render("Welcome to N-Queens Game!!", True, WHITE)
    subtitle = FONT.render("Ready to play?", True, WHITE)
    
    screen.blit(title, (60, 150))
    screen.blit(subtitle, (197, 250))
    
    pygame.draw.rect(screen, WHITE, yes_button)
    pygame.draw.rect(screen, WHITE, quit_button)

    text_yes = BUTTON_FONT.render("Yes", True, BLACK)
    text_quit = BUTTON_FONT.render("Quit", True, BLACK)

    screen.blit(text_yes, (yes_button.x + 25, yes_button.y + 3))
    screen.blit(text_quit, (quit_button.x + 25, quit_button.y + 3))

    pygame.display.update()

running = True
while running:
    welcome_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if yes_button.collidepoint(x, y):
                subprocess.run([sys.executable, "game.py"])
                running = False
            elif quit_button.collidepoint(x, y):
                running = False

pygame.quit()