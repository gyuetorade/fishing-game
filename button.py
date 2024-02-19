import pygame

class Button():
    def __init__(self, image_path, pos, base_color, hovering_color):
        self.image = pygame.image.load(image_path)
        self.x_pos, self.y_pos = pos
        self.base_color, self.hovering_color = base_color, hovering_color
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            # Handle color change logic here
            pass
        else:
            # Handle color change logic here
            pass
