import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, images, pos, scale, speed=5):
        super().__init__()

        self.angle = 0
        self.scale = 0.40
        self.speed = speed
        self.direction = (0, 0)

        if isinstance(images, str):
            self.original_images = [pygame.image.load(images)]
        else:
            self.original_images = images

        self.index = 0
        self.original_image = self.original_images[self.index]
        self.image = self.original_image.copy() if isinstance(self.original_image,
                                                              pygame.Surface) else self.original_image

        # Initialize self.rect after creating self.image
        self.rect = self.image.get_rect(center=pos)

        # Initialize self.mask

        self.resize_images()

    def resize_images(self):
        self.original_images = [pygame.transform.scale
                                (img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
                                for img in self.original_images]
        self.original_image = self.original_images[self.index]
        self.image = self.original_image.copy() if isinstance(self.original_image, pygame.Surface)\
            else self.original_image
        self.rect = self.image.get_rect(center=self.rect.center)

        # Update self.mask after resizing
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        rotated_image = pygame.transform.rotate(self.original_images[self.index], self.angle)
        self.image = rotated_image
        self.rect = rotated_image.get_rect(center=self.rect.center)

        # Update self.mask after rotating
        self.mask = pygame.mask.from_surface(self.image)

    def set_direction(self, keys, collision_mask):
        new_rect = self.rect.copy()  # Create a copy of the current rect

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            new_rect.y -= self.speed
            self.index = 0
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            new_rect.y += self.speed
            self.index = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            new_rect.x -= self.speed
            self.index = 2
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            new_rect.x += self.speed
            self.index = 3

        # Check if the new position is within the collision mask
        if collision_mask.overlap(pygame.mask.from_surface(self.image),
                                  (new_rect.x - collision_mask.get_rect().x, new_rect.y - collision_mask.get_rect().y)):
            self.rect = new_rect  # Update the position if within the collision zone

        # Update the character's mask after changing position
        self.mask = pygame.mask.from_surface(self.image)
