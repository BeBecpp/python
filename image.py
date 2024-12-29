import pygame
import random

# Pygame-г эхлүүлэх
pygame.init()

# Тоглоомын дэлгэцийн хэмжээ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Машины зургийг оруулах
car_img = pygame.image.load('car.png')  # car.png зургийг тохирох замтай оруулна

# Машины байрлал
car_width = car_img.get_width()
car_height = car_img.get_height()
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10

# Тоглоомын үндсэн цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Хамгийн сүүлд байрлуулсан машины зургийг дэлгэцэн дээр зурна
    screen.fill((255, 255, 255))  # Дэлгэцийг цагаан өнгөөр дүүргэх
    screen.blit(car_img, (car_x, car_y))  # Машины зураг дэлгэц дээр байрлуулах

    pygame.display.update()  # Дэлгэцийг шинэчлэх

pygame.quit()
