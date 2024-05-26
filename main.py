import pygame, sys, random, click, config

# Pygame setup
pygame.init()

bg_color = [0, 0, 0]

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
dt :float= 0
font = pygame.font.Font(None, 16)
mouse_pos = [0, 0]

for i in range(4):
    click.Click.spawnClick(config.click_size, [255-bg_color[0], 255-bg_color[1], 255-bg_color[2]], font, random.randint(0, config.max_clicks))

while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hit_a_box = False
                
                for c in click.Click.click_list:
                    if c.click(mouse_pos, config.mouse_rect_size):
                        hit_a_box = True
                        if config.allow_hit_multiple == False:
                            break
                
                s = None
                
                if hit_a_box:
                    s = pygame.mixer.Sound('assets/hit_click.wav')
                else:
                    s = pygame.mixer.Sound('assets/miss_click.wav')
                    
                s.play()
                
                # Add scoring, accuracy, anything that checks if the user hit a box
    
    # Update
    
    screen.fill(bg_color)
    
    # Draw
    
    for c in click.Click.click_list:
        c.draw(screen)
    
    dt = clock.tick(60) / 1000
    pygame.display.update()
    