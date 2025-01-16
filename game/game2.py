import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Crash Game")
clock = pygame.time.Clock()

background_image = pygame.image.load("/workspaces/python/game/background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

car_images = [
    pygame.image.load("/workspaces/python/game/car1.png"),
    pygame.transform.flip(pygame.image.load("/workspaces/python/game/car5.png"), False, False),
    pygame.transform.flip(pygame.image.load("/workspaces/python/game/car4.png"), False, False)
]
car_images = [pygame.transform.scale(img, (50, 100)) for img in car_images]
current_car_index = 0

obstacle_image = pygame.image.load("/workspaces/python/game/obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (50, 100))

coin_image = pygame.image.load("/workspaces/python/game/coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

CAR_WIDTH = 50
CAR_HEIGHT = 100
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
car_speed = 13

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
obstacle_speed = 15
obstacles = []

COIN_WIDTH = 30
COIN_HEIGHT = 30
coins = []

nitro_active = False
nitro_duration = 200
nitro_count = 0

score = 0
font = pygame.font.SysFont('Arial', 36)

highest_score = 0

coins_collected = 0

lives = 3

def draw_car(x, y, car_index):
    screen.blit(car_images[car_index], (x, y))

def draw_obstacle(obstacle):
    screen.blit(obstacle_image, obstacle)

def draw_coin(coin):
    screen.blit(coin_image, coin)

def display_score(score):
    score_text = font.render(f"Score: {score}", True, YELLOW)
    screen.blit(score_text, (10, 10))

def display_nitro(nitro_active):
    nitro_text = font.render("NITRO: ON" if nitro_active else "NITRO: OFF", True, GREEN if nitro_active else RED)
    screen.blit(nitro_text, (SCREEN_WIDTH - 150, 10))

def display_highest_score(highest_score):
    highest_score_text = font.render(f"Highest Score: {highest_score}", True, YELLOW)
    screen.blit(highest_score_text, (10, 50))

def display_coins_collected(coins_collected):
    coins_text = font.render(f"Coins: {coins_collected}", True, GREEN)
    screen.blit(coins_text, (10, 90))

def display_lives(lives):
    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 50))

def car_selection_menu():
    global current_car_index
    menu_running = True
    while menu_running:
        screen.fill(BLACK)
        title_text = font.render("Select Your Car", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
        
        for i, car_image in enumerate(car_images):
            x = SCREEN_WIDTH // 2 - car_image.get_width() // 2
            y = 150 + i * 150
            screen.blit(car_image, (x, y))
            if current_car_index == i:
                pygame.draw.rect(screen, GREEN, (x - 5, y - 5, car_image.get_width() + 10, car_image.get_height() + 10), 3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_car_index = (current_car_index - 1) % len(car_images)
                elif event.key == pygame.K_DOWN:
                    current_car_index = (current_car_index + 1) % len(car_images)
                elif event.key == pygame.K_RETURN:
                    menu_running = False
        
        pygame.display.flip()
        clock.tick(30)

car_selection_menu()
running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_d] and car_x < SCREEN_WIDTH - CAR_WIDTH:
        car_x += car_speed
    if keys[pygame.K_SPACE]:
        nitro_active = True
        nitro_count = nitro_duration

    if nitro_active:
        obstacle_speed = 20
        car_speed = 13
        nitro_count -= 1
        score += 5
        if nitro_count <= 0:
            nitro_active = False
            car_speed = 5
            obstacle_speed = 15

    if len(obstacles) == 0 or obstacles[-1].y > 200:
        obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        obstacles.append(pygame.Rect(obstacle_x, -OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    if len(coins) == 0 or coins[-1].y > 200:
        coin_x = random.randint(0, SCREEN_WIDTH - COIN_WIDTH)
        coins.append(pygame.Rect(coin_x, -COIN_HEIGHT, COIN_WIDTH, COIN_HEIGHT))

    for obstacle in obstacles:
        obstacle.y += obstacle_speed

    for coin in coins:
        coin.y += obstacle_speed

    obstacles = [obstacle for obstacle in obstacles if obstacle.y < SCREEN_HEIGHT]

    coins = [coin for coin in coins if coin.y < SCREEN_HEIGHT]

    car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
    for obstacle in obstacles:
        if car_rect.colliderect(obstacle):
            lives -= 1
            obstacles.remove(obstacle)
            if lives <= 0:
                if score > highest_score:
                    highest_score = score
                print("Game Over!")
                print(f"Final Score: {score}")
                print(f"Highest Score: {highest_score}")
                running = False

    for coin in coins:
        if car_rect.colliderect(coin):
            score += 10
            coins_collected += 1
            coins.remove(coin)

    score += 1

    draw_car(car_x, car_y, current_car_index)
    for obstacle in obstacles:
        draw_obstacle(obstacle)
    for coin in coins:
        draw_coin(coin)
    display_score(score)
    display_nitro(nitro_active)
    display_highest_score(highest_score)
    display_coins_collected(coins_collected)
    display_lives(lives)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
