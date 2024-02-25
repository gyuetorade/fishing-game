import pygame

def set_direction(character, keys):
    # Adjust the movement speed as needed
    speed = 7

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        character.set_direction("up")
        character.rect.y -= speed
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        character.set_direction("down")
        character.rect.y += speed
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        character.set_direction("left")
        character.rect.x -= speed
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        character.set_direction("right")
        character.rect.x += speed