import pygame

class Button:
    button_list = []
    
    def __init__(self, position:list, size:list, color:list, font, text:str, callback:callable):
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = color
        self.font = font
        self.text = self.font.render(text, True, [255-color[0], 255-color[1], 255-color[2]])
        self.text_str = text
        self.callback = callback
        
        Button.button_list.append(self)
    
    def poll_mouse_press(self, position):
        mr = pygame.Rect(position[0], position[1], 1, 1)
        
        if mr.colliderect(self.rect):
            if self.callback != None:
                self.callback(self)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        r = self.text.get_rect(center=self.rect.center)
        screen.blit(self.text, r)