import pygame

def set_direction(character, keys):
    if keys[pygame.K_UP]:
        character.set_direction("up")
        character.rect.y -= 10  # Adjust the movement speed as needed
    elif keys[pygame.K_DOWN]:
        character.set_direction("down")
        character.rect.y += 10  # Adjust the movement speed as needed
    elif keys[pygame.K_LEFT]:
        character.set_direction("left")
        character.rect.x -= 10  # Adjust the movement speed as needed
    elif keys[pygame.K_RIGHT]:
        character.set_direction("right")
        character.rect.x += 10  # Adjust the movement speed as needed
