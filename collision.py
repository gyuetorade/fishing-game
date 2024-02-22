import pygame

def load_path_mask(image_path):
    image = pygame.image.load(image_path).convert()  # Convert the image to improve performance
    return image
def maskcollision(image_path):
    image = pygame.image.load(image_path)
    mask = pygame.mask.from_surface(image)
    return mask
