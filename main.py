import pygame, sys

# Pygame setup
pygame.init()

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
dt :float= 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ... # Click logic
    
    screen.fill([10, 10, 50])
    
    dt = clock.tick(60) / 1000
    pygame.display.update()
    