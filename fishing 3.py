import pygame
import sys
from button import Button
from character import Character
from collision import maskcollision
from fishing_screen import fishing_screen
from pygame.locals import Rect

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


def draw_text_with_outline(surface, text, font, color, rect, align="center", outline_color=(0, 0, 0), outline_width=2,
                           text_rect=None, outline_rect=None):
    # Helper function to draw text with an outline on a surface
    text_rect, outline_rect
    text_surface = font.render(text, True, color)
    outline_surface = font.render(text, True, outline_color)

    if align == "center":
        text_rect = text_surface.get_rect(center=rect.center)
        outline_rect = outline_surface.get_rect(center=rect.center)
    elif align == "topleft":
        text_rect = text_surface.get_rect(topleft=rect.topleft)
        outline_rect = outline_surface.get_rect(topleft=rect.topleft)
    # Add more cases for other alignment options if needed

    text_rect.x -= outline_width
    text_rect.y -= outline_width

    surface.blit(outline_surface, outline_rect)
    surface.blit(outline_surface, (outline_rect.x - outline_width, outline_rect.y))
    surface.blit(outline_surface, (outline_rect.x + outline_width, outline_rect.y))
    surface.blit(outline_surface, (outline_rect.x, outline_rect.y - outline_width))
    surface.blit(outline_surface, (outline_rect.x, outline_rect.y + outline_width))

    surface.blit(text_surface, text_rect)


def main_menu():
    in_game = False

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(75)
        draw_text_with_outline(SCREEN, "Life Under the Sea", MENU_TEXT, (100, 200, 50), Rect(50, 100, 0, 0), "topleft")

        PLAY_BUTTON = Button(r"assets\Button\Button_Play.png", (SCREEN_WIDTH // 2, 450))
        QUIT_BUTTON = Button(r"assets\Button\Button_Quit.png", (SCREEN_WIDTH // 2, 550))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                # if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                in_game = True
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  # Remove this line from here

        if in_game:
            game = Game()
            while in_game:
                game.play()
                in_game = False

        pygame.display.update()


class Game:
    def __init__(self):
        #character initial position
        self.character = Character(character_images, (800, 420))

        self.path_mask = maskcollision(r"assets/Map/mask.png")
        self.buttons_on_screen = []
        self.fishing_mask = maskcollision(r"assets/Map/fishingmask.png")
        self.fishing_button = Button(r"assets/Button/Button_Fish.png", (1000, 240))

    def play(self):
        while True:
            SCREEN.blit(BGP, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            PLAY_BACK = Button(r"assets\Button\Button_Back.png", (220, 50))
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS) or event.type == pygame.K_SPACE:
                        return  # Return from the play function to go back to the main menu
                    if self.fishing_button.checkForInput(PLAY_MOUSE_POS):
                        print("Fishing button clicked!")
                        fishing_screen()  # Switch to the fishing screen

            keys = pygame.key.get_pressed()
            self.character.set_direction(keys, self.path_mask)  # Pass the collision mask to set_direction
            self.check_collision()  # Check for collision after updating the character's position

            pygame.display.update()

    def display(self):
        self.character.update()
        SCREEN.blit(self.character.image, self.character.rect)

    def check_collision(self):
        character_mask = pygame.mask.from_surface(self.character.image)

        # Calculate the offset based on the character's rect and fishing mask's rect
        character_offset = (
            self.character.rect.x - self.fishing_mask.get_rect().x,
            self.character.rect.y - self.fishing_mask.get_rect().y)

        # Use the character's mask and fishing mask for the overlap check
        character_overlap = self.fishing_mask.overlap(character_mask, character_offset)

        # If there's a collision, display the fishing button
        if character_overlap:
            # Draw the fishing button on the screen
            FISHING_BUTTON = Button(r"assets/Button/Button_Fish.png", (1000, 240))  # Adjust the path and position
            SCREEN.blit(FISHING_BUTTON.image, FISHING_BUTTON.rect)

        # Draw the character's and fishing mask on the screen for debugging
        SCREEN.blit(pygame.Surface(self.character.rect.size, pygame.SRCALPHA), self.character.rect)
        SCREEN.blit(pygame.Surface(self.fishing_mask.get_rect().size, pygame.SRCALPHA), self.fishing_mask.get_rect())

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
