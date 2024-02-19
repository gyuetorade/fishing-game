import pygame
import sys
from button import Button
from movement import set_direction
from character import Character
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BGP = pygame.image.load("assets/map 3.png")
button_image_path = "assets/Button_Play.png"

character_images = [
    pygame.image.load("assets/CharacterBack.png"),
    pygame.image.load("assets/CharacterFront.PNG"),
    pygame.image.load("assets/CharacterLeft.png"),
    pygame.image.load("assets/CharacterRight.png")
]

def get_font(size):
    return pygame.font.Font("assets/Retro Gaming.ttf", size)

class Game:
    def __init__(self):
        self.character = Character(character_images, (870, 420), scale=0.43)
        self.obstacle_rect = pygame.Rect(500, 300, 100, 100)  # Example obstacle, adjust as needed
    def play(self):
        while True:
            SCREEN.blit(BGP, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            PLAY_BACK =  Button("assets/Button_Menu.png", (50, 50), "White", "Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return  # Return from the play function to go back to the main menu

            keys = pygame.key.get_pressed()  # Get pressed keys
            set_direction(self.character, keys)  # Call set_direction function

            pygame.display.update()

    def update(self):
        keys = pygame.key.get_pressed()  # Get pressed keys
        set_direction(self.character, keys)  # Call set_direction function

    def display(self):
        self.character.update()
        SCREEN.blit(self.character.image, self.character.rect)


def main_menu():
    in_game = False  # New variable to track whether the player is in the game

    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Life Under the Sea", True, (255, 255, 255))

        PLAY_BUTTON = Button("assets/Button_Play.png", (SCREEN_WIDTH // 2, 450), "White", "Green")

        QUIT_BUTTON = Button("assets/Button_Quit.png", (SCREEN_WIDTH // 2, 550), "White", "Green")

        SCREEN.blit(MENU_TEXT,(50, 100))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    in_game = True  # Set in_game to True when PLAY is pressed

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        if in_game:
            game = Game()
            while in_game:
                game.play()
                in_game = False  # Reset in_game when returning from play to the main menu

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
