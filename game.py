import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Bird settings
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
GRAVITY = 0.9
FLAP_STRENGTH = -10

# Pipe settings
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_velocity = -4
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, RED, (x, y, BIRD_WIDTH, BIRD_HEIGHT))

def draw_pipe(pipe):
    pygame.draw.rect(screen, GREEN, pipe)

def check_collision(bird_rect, pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True
    return False

def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_STRENGTH

    # Bird movement
    bird_velocity += GRAVITY
    bird_y += bird_velocity
    bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)

    # Pipe movement
    if len(pipes) == 0 or pipes[-1].x < SCREEN_WIDTH - 200:
        pipe_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        pipes.append(pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, pipe_height))
        pipes.append(pygame.Rect(SCREEN_WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP))

    for pipe in pipes:
        pipe.x += pipe_velocity

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.right > 0]

    # Check collisions
    if check_collision(bird_rect, pipes):
        print("Game Over!")
        print(f"Final Score: {score}")
        running = False

    # Update score
    for pipe in pipes:
        if pipe.right == bird_x:
            score += 1

    # Draw everything
    draw_bird(bird_x, bird_y)
    for pipe in pipes:
        draw_pipe(pipe)
    display_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
