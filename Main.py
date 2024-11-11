import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 7

block_width = 50
block_height = 50
block_speed = 5
blocks = []

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    if random.random() < 0.02:
        block_x = random.randint(0, screen_width - block_width)
        blocks.append([block_x, 0])

    for block in blocks[:]:
        block[1] += block_speed
        if (block[0] < player_x + player_width and block[0] + block_width > player_x and
            block[1] < player_y + player_height and block[1] + block_height > player_y):
            running = False
        if block[1] > screen_height:
            blocks.remove(block)
            score += 1

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

    show_score(score)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
