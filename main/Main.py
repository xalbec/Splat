import pygame
from main.scenes.MainMenu import MainMenu

pygame.init()

WIDTH = 0
HEIGHT = 0
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 60

active_scene = MainMenu()
active_scene.setup(screen)

# Game Loop
while active_scene is not None:

    pressed_keys = pygame.key.get_pressed()

    # Event Filtering
    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_F4 and alt_pressed:
                quit_attempt = True
        if quit_attempt:
            active_scene.terminate()
        else:
            filtered_events.append(event)

    # Player input
    active_scene.process_input(filtered_events, pressed_keys)
    # Make stuff happen
    active_scene.update()
    # Doodle it
    active_scene.render(screen)

    # Runs the set up for the next Scene.
    # Ignores the None case so I don't get an error just prior to closing.
    if active_scene is not active_scene.next and active_scene.next is not None:
        active_scene.next.setup(screen)
    active_scene = active_scene.next

    pygame.display.flip()
    clock.tick(fps)


pygame.quit()
