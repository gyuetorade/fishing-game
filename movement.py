import pygame

def set_direction(character, keys):
    if keys[pygame.K_UP]:
        character.index = 0  # Set direction to up
    elif keys[pygame.K_DOWN]:
        character.index = 1  # Set direction to down
    elif keys[pygame.K_LEFT]:
        character.index = 2  # Set direction to left
    elif keys[pygame.K_RIGHT]:
        character.index = 3  # Set direction to right
