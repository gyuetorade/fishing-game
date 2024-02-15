import pygame
import sys
import math
from button import Button
from movement import set_direction
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
BGP = pygame.image.load("assets/BackgroundPlay.png")
class Character(pygame.sprite.Sprite):
    def __init__(self, images, pos):
        super().__init__()
        if isinstance(images, str):  # Check if a single image file path is provided
            self.original_images = [pygame.image.load(images)]
        else:
            self.original_images = images
        self.index = 0
        self.original_image = self.original_images[self.index]
        self.image = self.original_image.copy() if isinstance(self.original_image, pygame.Surface) else self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def set_direction(self, direction):
        if direction == "up":
            self.index = 0
        elif direction == "down":
            self.index = 1
        elif direction == "left":
            self.index = 2
        elif direction == "right":
            self.index = 3

character_images = [
    pygame.image.load("assets/CharacterFront.png"),
    pygame.image.load("assets/CharacterBack.png"),
    pygame.image.load("assets/CharacterLeft.png"),
    pygame.image.load("assets/CharacterRight.png")
]
character = Character("assets/CharacterFront.png", (640, 360))

def get_font(size):
    return pygame.font.Font("assets/Retro Gaming.ttf", size)

def play():
    # Instantiate the Character class with the list of images
    character = Character(character_images, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    while True:
        SCREEN.blit(BGP, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        character.update()
        SCREEN.blit(character.image, character.rect)

        PLAY_BACK = Button(image=None, pos=(100, 50),
                           text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return

        pygame.display.update()

def main_menu():
    character = Character("assets/CharacterFront.png", (SCREEN_WIDTH // 1, SCREEN_HEIGHT // 1))

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Life Under the Sea", True, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN_WIDTH // 2, 320),
                             text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#AEC6CF")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH // 2, 450),
                             text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#AEC6CF")

        SCREEN.blit(MENU_TEXT, MENU_RECT)


        character.update()
        SCREEN.blit(character.image, character.rect)

        keys = pygame.key.get_pressed()  # Get pressed keys
        set_direction(character, keys)  # Call set_direction function

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
