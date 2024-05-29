import pygame, sys, random, click, config, button, custom_math
oppositeColor = [255-config.bg_color[0], 255-config.bg_color[1], 255-config.bg_color[2]]

# Pygame setup
pygame.init()

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
dt :float= 0
font = pygame.font.Font(None, 32)
mouse_pos = [0, 0]

icon = pygame.Surface([32, 32]).convert_alpha()
icon.fill([0,0,0,0])

pygame.display.set_caption("Aim Trainer")
pygame.display.set_icon(icon)

SCENE_START    = 0
SCENE_PLAY     = 1
SCENE_SETTINGS = 2

score :int= config.score_remove


def start():
    button.Button.button_list = []
    click.Click.click_list = []
    config.scene = SCENE_START
    startButton = button.Button([32, 32], [256, 48], oppositeColor, font, "Play", play)
    settingsButton = button.Button([32, 32+48+32], [256, 48], oppositeColor, font, "Settings", settings)
    quitButton = button.Button([32, 32+48+32+48+32], [256, 48], oppositeColor, font, "Quit", quit)

def play(btn):
    button.Button.button_list = []
    config.scene = SCENE_PLAY
    for i in range(config.click_amount):
        click.Click.spawnConfigClick(font)

def quit(btn):
    pygame.quit()
    sys.exit()

def settings(btn):
    config.scene = SCENE_SETTINGS
    button.Button.button_list = []
    
    max_click_sub = button.Button([480, 0], [48, 48], oppositeColor, font, "-", updateMaxClick)
    max_click_add = button.Button([480 + 48 + 10, 0], [48, 48], oppositeColor, font, "+", updateMaxClick)
    
    click_size_sub = button.Button([480, 48], [48, 48], oppositeColor, font, "-", updateClickSize)
    click_size_add = button.Button([480 + 48 + 10, 48], [48, 48], oppositeColor, font, "+", updateClickSize)
    
    click_amount_sub = button.Button([480, 48*2], [48, 48], oppositeColor, font, "-", updateClickAmount)
    click_amount_add = button.Button([480 + 48 + 10, 48*2], [48, 48], oppositeColor, font, "+", updateClickAmount)

def updateMaxClick(btn):
    match btn.text_str:
        case "-":
            config.max_clicks -= 1
        case "+":
            config.max_clicks += 1
    
    config.max_clicks = custom_math.clamp(config.max_clicks, 1, 16)

def updateClickSize(btn):
    match btn.text_str:
        case "-":
            config.click_size -= 4
        case "+":
            config.click_size += 4
    
    config.click_size = custom_math.clamp(config.click_size, 4, 256)

def updateClickAmount(btn):
    match btn.text_str:
        case "-":
            if config.click_amount > 1:
                config.click_amount -= 1
        case "+":
            config.click_amount += 1
     
   
start()


while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hit_a_box = False
                
                for clk in click.Click.click_list:
                    if clk.click(mouse_pos, config.mouse_rect_size):
                        hit_a_box = True
                        if config.allow_hit_multiple == False:
                            break
                
                for btn in button.Button.button_list:
                    btn.poll_mouse_press(mouse_pos)
                
                if config.scene == SCENE_PLAY:
                    sound = None
                    
                    if hit_a_box:
                        sound = pygame.mixer.Sound('assets/hit_click.wav')
                        score += config.score_add
                    else:
                        sound = pygame.mixer.Sound('assets/miss_click.wav')
                        score -= config.score_remove
                        
                    sound.play()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                start()
                score = config.score_remove
    
    # Update
    
    screen.fill(config.bg_color)
    
    # Draw
    
    for c in click.Click.click_list:
        c.draw(screen)
    
    for b in button.Button.button_list:
        b.draw(screen)


    if config.scene == SCENE_PLAY:
        score_text = font.render(f'Score: {score}', True, oppositeColor)
        return_text = font.render(f'Press ESCAPE to return to main menu.', True, oppositeColor)

        screen.blit(score_text, [0, 0])
        screen.blit(return_text, [0, 720-32])
    
    if config.scene == SCENE_SETTINGS:
        max_click_text = font.render(f'Max Clicks: {config.max_clicks}', True, oppositeColor)
        click_size_text = font.render(f'Click Size: {config.click_size}', True, oppositeColor)
        click_amount_text = font.render(f'Click Amount: {config.click_amount}', True, oppositeColor)
        
        screen.blit(max_click_text, [10, 0])
        screen.blit(click_size_text, [10, 48])
        screen.blit(click_amount_text, [10, 48*2])
    
    dt = clock.tick(60) / 1000
    pygame.display.update()
    