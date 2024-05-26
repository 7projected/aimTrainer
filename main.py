import pygame, sys, random, click

# Pygame setup
pygame.init()

bg_color = [10, 10, 50]

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
dt :float= 0
font = pygame.font.Font(None, 16)
mouse_pos = [0, 0]

def leftClick(mousePos):
    for c in click.Click.click_list:
        c.click(mousePos, 1)

for i in range(4):
    click.Click.spawnClick(32, [255-bg_color[0], 255-bg_color[1], 255-bg_color[2]], font)

while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftClick(mouse_pos)
    
    # Update
    
    screen.fill(bg_color)
    
    # Draw
    
    for c in click.Click.click_list:
        c.draw(screen)
    
    dt = clock.tick(60) / 1000
    pygame.display.update()
    