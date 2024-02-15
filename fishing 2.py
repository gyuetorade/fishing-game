import pygame
import sys
import math
from button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")

class Character(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.original_image = pygame.image.load(image)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update_angle(self, mouse_pos):
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        self.angle = (180 / math.pi) * -math.atan2(dy, dx)

def get_font(size):
    return pygame.font.Font("assets/Retro Gaming.ttf", size)

def play():
    character = Character("assets/CharacterFront.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    while True:
        SCREEN.fill((192, 192, 192))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        character.update_angle(PLAY_MOUSE_POS)
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

        character.update_angle(MENU_MOUSE_POS)
        character.update()
        SCREEN.blit(character.image, character.rect)

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
