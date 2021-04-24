import pygame
from src.utilities.mouse import cursor
from src.utilities.palette import col
# import config
# ok so youre supposed to make a config file for like tokens and whatever but idk if we are doing to be using any tokens or whatever but anyways config is just going to exist and will go into gitignore

# put display updates in here
def update_display():
    gameWindow.fill(col["white"])

    pygame.display.update()

# put event updates here
def update_events():
    cursor.update(scroll)
    keysdown = pygame.key.get_pressed()

if __name__ == '__main__':
    pygame.init()
    
    # dimmensions of window
    WIDTH, HEIGHT = 800, 600

    gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("untitled project!!")

    clock = pygame.time.Clock()

    running = True

    while running:
        keyspressed = []
        scroll = 0

        # poll events from window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break 
            elif event.type == pygame.KEYDOWN:
                keyspressed.append(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll -= 1
                elif event.button == 5:
                    scroll = 1
        
        # update events
        update_events()

        # update screen
        update_display()
        clock.tick(60)
                

    pygame.quit() 