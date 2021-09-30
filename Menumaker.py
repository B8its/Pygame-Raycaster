import pygame

screen = pygame.display.set_mode((500,500))
pygame.font.init()
class button:
    def __init__(self, x, y, width, height, func, colour = (255,255,255), colourb = (150,150,150)):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.colour = colour
        self.on = False
        self.clicked = False
        self.func = func
        self.colourb = colourb

    def __str__(self):
        return f'button({self.x, self.y, self.width, self.height, self.colour})'


    def __repr__(self):
        return f'button({self.x, self.y, self.width, self.height, self.colour})'

    def draw(self):
        global screen
        if self.on == True:
            pygame.draw.rect(screen, self.colourb, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        
    
    def OnButton(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0] > self.x and mouse[0] < self.x+self.width and mouse[1] > self.y and mouse[1] < self.y+self.height:
            self.on = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = True
    
                    self.func()
                    break
                else:
                    self.clicked = False
        else:
            self.on = False
            self.clicked = False
            

class texts:
    def __init__(self, x, y, text, size, centered = True, font = "arial"):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.centered = centered
    def draw(self):
        global screen
        rendered = self.font.render(self.text, True, (255,255,255))
        length = rendered.get_size()[0]/2
        if self.centered:
            screen.blit(rendered, (self.x-length, self.y))
        else:
            screen.blit(rendered, (self.x, self.y))
        
    def __str__(self):
        return f'texts({self.x, self.y, self.text, self.font})'

    def __repr__(self): 
        return f'texts({self.x, self.y, self.text, self.font})'

class menu:
    def __init__(self, buttons, text):
        self.buttons = buttons
        self.texts = text

    def __str__(self):
        return f'menu({self.buttons})'
    def draw(self):

        for button in self.buttons:
            button.OnButton()
            button.draw()
        for text in self.texts:
            text.draw()

    
    def addButton(self, button):
        self.buttons.append(button)
    
    def addText(self, text):
        
        self.texts.append(text)

def react():
    print("Yay")

def main():
    global menu
    global screen
    menus = menu([], [])
    #x = print("nice")
    reac = react
    while True:    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    mouse = pygame.mouse.get_pos()

                    menus.addButton(button(mouse[0], mouse[1], 50, 50, reac))
            
                if event.key == pygame.K_q:
                    mouse = pygame.mouse.get_pos()
                    menus.addText(texts(mouse[0], mouse[1], input("Text: "), 30))
        screen.fill((0,0,0))
        menus.draw()
        #print(str(menus))
        pygame.display.update()
        pygame.display.flip()

main()