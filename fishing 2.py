import pygame
import sys
import time
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

def get_font(size):
    return pygame.font.Font(r"assets/Font/Daydream.ttf", size)



class Game:
    def __init__(self):
        self.character = Character(character_images, (870, 420), scale=0.53)
        self.path_mask = maskcollision(r"assets/Map/mask.png")
        self.fishing_mask = maskcollision(r"assets/Map/fishingmask.png")
        self.buttons_on_screen = []
        self.fishing_in_progress = False
        self.fishing_start_time = 0
        self.show_fish_caught_text = False

    def play(self):
        fishing_screen = FishingScreen()
        fishing_button = Button(r"assets/Button/Button_Fish.png", (751, 100))
        back_button = Button(r"assets/Button/Button_Back.png", (50, 50))
        fish_caught_font = get_font(36)

        while True:

            SCREEN.blit(BGP, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            back_button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            # Update character direction and check collision with the path mask
            keys = pygame.key.get_pressed()
            self.character.set_direction(keys, self.path_mask)
            path_overlap = self.check_collision(self.path_mask)

            fishing_overlap = self.check_collision(self.fishing_mask)

            # Draw fishing background
            SCREEN.blit(fishing_screen.background, (0, 0))

            # Draw character
            self.character.update()
            SCREEN.blit(self.character.image, self.character.rect)

            if fishing_overlap and not self.fishing_in_progress:
                fishing_button.update(SCREEN)

                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    if fishing_button.checkForInput(PLAY_MOUSE_POS):
                        self.fishing_in_progress = True
                        self.fishing_start_time = time.time()

            if self.fishing_in_progress:
                fishing_screen.display()

                if time.time() - self.fishing_start_time >= 1:
                    # Reset fishing_in_progress and set show_fish_caught_text flag
                    self.fishing_in_progress = False
                    self.show_fish_caught_text = True

            if self.show_fish_caught_text:
                # Draw "Fish Caught!" text
                fish_caught_text = fish_caught_font.render("Fish Caught!", True, (255, 255, 255))
                fish_caught_rect = fish_caught_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1))
                SCREEN.blit(fish_caught_text, fish_caught_rect)

                # Draw back button
                back_button.update(SCREEN)

                # Handle back button press
                if back_button.checkForInput(PLAY_MOUSE_POS):
                    self.show_fish_caught_text = False  # Reset the flag when back button is pressed

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
class FishingScreen:
    def __init__(self):
        self.background = pygame.image.load(r"assets\Map\FishingScreenBackground.png")
        self.font = pygame.font.Font(None, 36)
        self.text = "Fishing"
        self.dot_count = 0
        self.max_dots = 3
        self.catch_text = ""

        # Add a delay (in seconds) between each dot update
        self.delay_between_dots = 0.5  # Adjust this value to control the animation speed
        self.last_dot_update_time = time.time()
        self.animation_complete = False  # Flag to track the completion of the animation

    def update_text(self):
        # Check if it's time to update the dots
        current_time = time.time()
        if current_time - self.last_dot_update_time >= self.delay_between_dots:
            self.dot_count = (self.dot_count + 1) % (self.max_dots + 1)
            self.catch_text = "." * self.dot_count
            self.last_dot_update_time = current_time

            if self.dot_count == self.max_dots:
                self.animation_complete = True

    def display(self):
        while not self.animation_complete:
            SCREEN.blit(self.background, (0, 0))

            # Update text with animated dots
            self.update_text()
            text_render = get_font(75).render(f"{self.text} {self.catch_text}", True, (150, 10, 23))
            text_rect = text_render.get_rect(center=(660, 660))
            SCREEN.blit(text_render, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

        # Reset animation complete flag for the next use
        self.animation_complete = False
if __name__ == "__main__":
    main_menu()
