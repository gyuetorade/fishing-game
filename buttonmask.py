import pygame


class ButtonMask:
    def __init__(self, image_path, function):
        self.mask = maskcollision(image_path)
        self.function = function

    def check_collision(self, character_rect):
        offset = (character_rect.x - self.mask.get_rect().x, character_rect.y - self.mask.get_rect().y)
        overlap = self.mask.overlap(pygame.mask.Mask((1, 1)), offset)  # Using a 1x1 mask for simplicity

        return overlap is not None

