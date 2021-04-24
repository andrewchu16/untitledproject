import pygame
from src.utilities.mouse import cursor
from statemachine import StateMachine
from src.utilities.palette import col
# import config

# put display updates in here
def update_display():
    gameWindow.fill(col["white"])
    
    state.render(gameDisplay, screen_heigh, screen_width)

    pygame.display.update()

# put event updates here
def update_events():
    cursor.update(scroll)
    keysdown = pygame.key.get_pressed()
    state.update(keyspressed, keysdown)

if __name__ == '__main__':
    pygame.init()
    
    # dimmensions of window
    WIDTH, HEIGHT = 600, 600

    gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("untitled project!!")

    clock = pygame.time.Clock()

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