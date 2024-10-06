import pygame, sys
pygame.init(); screen = pygame.display.set_mode((800, 600)); x, speed = 0, 5
while True: 
    for e in pygame.event.get(): e.type==pygame.QUIT and sys.exit()
    x += speed * (1 if (x<800) else -1) if (x<800 or x>0) else speed*-1; screen.fill((255, 255, 255)); pygame.draw.rect(screen, (255, 0, 0), (x, 275, 50, 50)); pygame.display.flip(); pygame.time.delay(16)

import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Left to Right Animation")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
rect_width, rect_height = 50, 50
x = 0
y = (HEIGHT - rect_height) // 2
speed = 5
direction = 1
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed * direction
    if x + rect_width > WIDTH or x < 0:
        direction *= -1
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
