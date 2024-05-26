import pygame, random

class Click:
    click_list = []
    
    def spawnClick(size, color, font):
        rngX = random.randint(0+(size/2), 1280-(size/2))
        rngY = random.randint(0+(size/2), 720-(size/2))
        
        Click.click_list.append(Click(rngX, rngY, size, font, [color[0], color[1], color[2]], Click.die))

    def __init__(self, x:int, y:int, size:int, font:pygame.font, color:list, callback:callable):
        self.x = x
        self.y = y
        self.size = size
        self.font = font
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = [x, y]
        self.color = color
        self.callback = callback
    
    def die(self):
        for c in Click.click_list:
            if c == self:
                Click.click_list.remove(self)
                Click.spawnClick(self.size, self.color, self.font)
    
    def click(self, position, clickSize):
        mr = pygame.Rect(0, 0, clickSize, clickSize)
        mr.center = position
        
        if self.rect.colliderect(mr) == True:
            self.callback(self)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)