import pygame
import sys
from button import Button
from movement import set_direction
from character import Character
from collision import maskcollision
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load(r"assets\Map\Background Menu.png")
BGP = pygame.image.load(r"assets\Map\BackgroundPlay.png")
button_image_path = r"assets\Button\Button_Play.png"

character_images = [
    pygame.image.load(r"assets\Character\CharacterBack.PNG"),
    pygame.image.load(r"assets\Character\CharacterFront.PNG"),
    pygame.image.load(r"assets\Character\CharacterLeft.PNG"),
    pygame.image.load(r"assets\Character\CharacterRight.PNG")
]

def get_font(size):
    return pygame.font.Font(r"assets\Font\Retro Gaming.ttf", size)


class Game:
    def __init__(self):
        self.character = Character(character_images, (870, 420), scale=0.53)
        self.path_mask = maskcollision(r"assets/Map/mask.png")

    def play(self):
        while True:
            SCREEN.blit(BGP, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            PLAY_BACK = Button(r"assets\Button\Button_Menu.png", (50, 50), "White", "Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return  # Return from the play function to go back to the main menu

            keys = pygame.key.get_pressed()
            self.character.set_direction(keys, self.path_mask)  # Pass the collision mask to set_direction

            print(f"Character Rect (play): {self.character.rect}")

            self.check_collision()  # Check for collision after updating the character's position

            pygame.display.update()
    def update(self):
        keys = pygame.key.get_pressed()  # Get pressed keys
        set_direction(self.character, keys)  # Call set_direction function

    def display(self):
        self.character.update()
        SCREEN.blit(self.character.image, self.character.rect)


    def check_collision(self):
        character_mask = pygame.mask.from_surface(self.character.image)

        # Calculate the offset based on the character's rect and path mask's rect
        offset = (self.character.rect.x - self.path_mask.get_rect().x, self.character.rect.y - self.path_mask.get_rect().y)

        # Use the character's mask and path mask for the overlap check
        overlap = self.path_mask.overlap(character_mask, offset)

        print(f"Character Rect: {self.character.rect}")
        print(f"Character Mask Rect: {self.character.mask.get_rect(center=self.character.rect.center)}")
        print(f"Overlap: {overlap}")

        # Draw the character's and path mask on the screen for debugging
        SCREEN.blit(pygame.Surface(self.character.rect.size, pygame.SRCALPHA), self.character.rect)
        SCREEN.blit(pygame.Surface(self.path_mask.get_rect().size, pygame.SRCALPHA), self.path_mask.get_rect())

        if overlap:
            # Collision detected, handle accordingly
            print("Collision detected!")
            # You can implement actions like stopping the character, showing a message, etc.
        else:
            # No collision, continue normal movement
            pass

        pygame.display.update()

def main_menu():
    in_game = False  # New variable to track whether the player is in the game

    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Life Under the Sea", True, (255, 255, 255))

        PLAY_BUTTON = Button(r"assets\Button\Button_Play.png", (SCREEN_WIDTH // 2, 450), "White", "Green")

        QUIT_BUTTON = Button(r"assets\Button\Button_Quit.png", (SCREEN_WIDTH // 2, 550), "White", "Green")

        SCREEN.blit(MENU_TEXT, (50, 100))

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
