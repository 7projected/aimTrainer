import pygame, random, config

class Click:
    click_list = []
    
    def spawnClick(size, color, font, clicks):
        rngX = random.randint(0+(size/2), 1280-(size/2))
        rngY = random.randint(0+(size/2), 720-(size/2))

        Click.click_list.append(Click(rngX, rngY, size, font, [color[0], color[1], color[2]], clicks))

    def __init__(self, x:int, y:int, size:int, font:pygame.font, color:list, clicks:int):
        self.x = x
        self.y = y
        self.size = size
        self.font = font
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = [x, y]
        self.color = color
        self.clicks = clicks
    
    def die(self):
        for c in Click.click_list:
            if c == self:
                Click.click_list.remove(self)
                Click.spawnClick(self.size, self.color, self.font, random.randint(0, config.max_clicks))
    
    def click(self, position, clickSize):
        mr = pygame.Rect(0, 0, clickSize, clickSize)
        mr.center = position
        
        if self.rect.colliderect(mr) == True:
            if self.clicks <= 1:
                self.die()
            else:
                self.clicks -= 1
                # Add visual notifier of self.clicks changing
            
            return True
        else:
            return False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)