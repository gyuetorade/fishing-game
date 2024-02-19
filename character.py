import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, images, pos, scale, speed=5):
        super().__init__()

        self.angle = 0
        self.scale = scale
        self.speed = speed
        self.direction = (0, 0)

        if isinstance(images, str):
            self.original_images = [pygame.image.load(images)]
        else:
            self.original_images = images

        self.index = 0
        self.original_image = self.original_images[self.index]
        self.image = self.original_image.copy() if isinstance(self.original_image, pygame.Surface) else self.original_image

        # Initialize self.rect after creating self.image
        self.rect = self.image.get_rect(center=pos)

        self.resize_images()

    def resize_images(self):
        self.original_images = [pygame.transform.scale(img, (int(img.get_width() * self.scale),
                                                             int(img.get_height() * self.scale)))
                                for img in self.original_images]
        self.original_image = self.original_images[self.index]
        self.image = self.original_image.copy() if isinstance(self.original_image, pygame.Surface) else self.original_image
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        rotated_image = pygame.transform.rotate(self.original_images[self.index], self.angle)
        self.image = rotated_image
        self.rect = rotated_image.get_rect(center=self.rect.center)

    def set_direction(self, direction):
        if direction == "up":
            self.index = 0
        elif direction == "down":
            self.index = 1
        elif direction == "left":
            self.index = 2
        elif direction == "right":
            self.index = 3
