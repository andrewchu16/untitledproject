import pygame
from pygame.constants import RESIZABLE
from src.utilities.mouse import cursor
from statemachine import StateMachine
from src.utilities.palette import col
# import configa

# put display updates in here
def update_display():
    gameWindow.fill(col["black"])
    
    state.render(gameWindow, WIDTH, HEIGHT)
    
    cursor.render(gameWindow)

    pygame.display.update()
    
# put event updates here
def update_events():
    cursor.update(scroll)
    keysdown = pygame.key.get_pressed()
    
    # keyspressed = list of keys that are pressed 
    # keysdown = dictionary of all keys, with boolean of if they are pressed
    state.update(keyspressed, keysdown)

# note: variables in here are global, not local
if __name__ == '__main__':
    # initialize pygame window
    pygame.init()
    
    # dimmensions of window
    WIDTH, HEIGHT = 700, 700

    gameWindow = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
    pygame.display.set_caption("untitled project!!")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    # used to switch between menu, pause, settings, etc
    state = StateMachine()

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
