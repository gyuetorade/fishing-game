import pygame
import sys
from button import Button
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
    pygame.image.load(r"assets/Character/CharacterBack.PNG"),
    pygame.image.load(r"assets\Character\CharacterFront.PNG"),
    pygame.image.load(r"assets\Character\CharacterLeft.PNG"),
    pygame.image.load(r"assets\Character\CharacterRight.PNG")

]

def get_font(size):
    return pygame.font.Font(r"assets/Font/Daydream.ttf", size)


class Game:
    def __init__(self):
        self.character = Character(character_images, (870, 420), scale=0.53)
        self.path_mask = maskcollision(r"assets/Map/mask.png")
        self.fishing_mask = maskcollision(r"assets/Map/fishingmask.png")
        self.buttons_on_screen = []
        self.is_fishing_overlap = False  # Flag to track fishing mask overlap

    def play(self):
        fishing_button = Button(r"assets/Button/Button_Fish.png", (751, 100))

        while True:
            SCREEN.blit(BGP, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            PLAY_BACK = Button(r"assets\Button\Button_Menu.png", (50, 50))
            PLAY_BACK.update(SCREEN)

            path_overlap = self.check_collision(self.path_mask)
            fishing_overlap = self.check_collision(self.fishing_mask)

            if fishing_overlap:
                fishing_button.update(SCREEN)

                # Handle mouse events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Check if the fishing button is clicked
                        if fishing_button.checkForInput(PLAY_MOUSE_POS):
                            print("Button Clicked!")

            # Handle mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return  # Return from the play function to go back to the main menu

            # Update character direction and check collision with the path mask
            keys = pygame.key.get_pressed()
            self.character.set_direction(keys, self.path_mask)
            self.check_collision(self.path_mask)

            pygame.display.update()

    def display(self):
        self.character.update()
        SCREEN.blit(self.character.image, self.character.rect)

    def check_collision(self, collision_mask):
        character_mask = pygame.mask.from_surface(self.character.image)

        # Calculate the offset based on the character's rect and the collision mask's rect
        offset = (
        self.character.rect.x - collision_mask.get_rect().x, self.character.rect.y - collision_mask.get_rect().y)

        # Use the character's mask and the collision mask for the overlap check
        overlap = bool(collision_mask.overlap(character_mask, offset))

        # Draw the character's and the collision mask on the screen for debugging
        SCREEN.blit(pygame.Surface(self.character.rect.size, pygame.SRCALPHA), self.character.rect)
        SCREEN.blit(pygame.Surface(collision_mask.get_rect().size, pygame.SRCALPHA), collision_mask.get_rect())

        return overlap

def main_menu():
    in_game = False  # New variable to track whether the player is in the game

    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(75).render("Life Under the Sea", True, (100, 200, 50))
        PLAY_BUTTON = Button(r"assets\Button\Button_Play.png", (SCREEN_WIDTH // 2, 450))
        QUIT_BUTTON = Button(r"assets\Button\Button_Quit.png", (SCREEN_WIDTH // 2, 550))

        SCREEN.blit(MENU_TEXT, (50, 100))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
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
