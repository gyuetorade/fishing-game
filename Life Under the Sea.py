import pygame
import sys
from button import Button
from character import Character
from collision import maskcollision
from fishies import get_random_fish
from pygame.locals import Rect

pygame.init()

# Set up the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

# Load background images
BG = pygame.image.load(r"assets\Map\Background Menu.png")
BGP = pygame.image.load(r"assets\Map\BackgroundPlay.png")
FISHING_BG = pygame.image.load(r"assets/Map/BackgroundFishing.png")
TEXTBOX_IMAGE = pygame.image.load(r"assets/Others/textbox.png")

# Load character images
character_images = [
    pygame.image.load(r"assets/Character/CharacterBack.PNG"),
    pygame.image.load(r"assets\Character\CharacterFront.PNG"),
    pygame.image.load(r"assets\Character/CharacterLeft.PNG"),
    pygame.image.load(r"assets/Character/CharacterRight.PNG")
]

# Initialize mixer and load main menu song
pygame.mixer.init()
gamesound = pygame.mixer.Sound(r"assets/audio/Audio_Game.mp3")
main_menu_song = pygame.mixer.Sound(r"assets/audio/Audio_Menu.mp3")
main_menu_song.set_volume(0.5)  # Set initial volume
Play = pygame.mixer.Sound(r"assets/audio/Audio_Play.wav")
buttonsfx = pygame.mixer.Sound(r"assets/audio/Audio_Play.wav")
cookingdonesound = pygame.mixer.Sound(r"assets/audio/Audio_Cook.mp3")
descsound = pygame.mixer.Sound(r"assets/audio/descsound.wav")
cookingsound = pygame.mixer.Sound(r"assets/audio/Audio_Cooking.mp3")
cooka = pygame.mixer.Sound(r"assets/audio/Audio_Cook.mp3")
cookb = pygame.mixer.Sound(r"assets/audio/Audio_Jail.mp3")
fishcaught = pygame.mixer.Sound(r"assets/audio/Audio_Fish.mp3")


# Function to get font
def get_font(size):
    return pygame.font.Font(r"assets/Font/Daydream.ttf", size)


# Function to draw text with outline
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


# Main menu function
def main_menu():
    in_game = False

    # Play main menu song on loop
    main_menu_song.play(-1)

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(75)
        draw_text_with_outline(SCREEN, "Life Under the Sea", MENU_TEXT, (222, 180, 118), Rect(650, 100, 0, 0), "center")

        PLAY_BUTTON = Button(r"assets\Button\Button_Play.png", (SCREEN_WIDTH // 2, 450))
        QUIT_BUTTON = Button(r"assets\Button\Button_Quit.png", (SCREEN_WIDTH // 2, 550))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Stop main menu song when Play button is pressed
                    main_menu_song.stop()
                    Play.play()
                    gamesound.play()

                    in_game = True
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  # Remove this line from here

        if in_game:
            game = Game()
            while in_game:
                game.play()
                # When returning to the main menu, restart the main menu song
                main_menu_song.play(-1)
                in_game = False

        pygame.display.update()


class Game:
    def __init__(self):
        # character initial position
        self.character = Character(character_images, (660, 220))
        self.path_mask = maskcollision(r"assets/Map/mask.png")
        self.fishing_mask = maskcollision(r"assets/Map/fishingmask.png")
        self.fishing_button = Button(r"assets/Button/Button_Fish.png", (660, 620))

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
                        Play.play()
                        gamesound.stop()
                        return  # Return from the play function to go back to the main menu
                    if self.fishing_button.checkForInput(PLAY_MOUSE_POS):
                        gamesound.stop()
                        Play.play()
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
            FISHING_BUTTON = Button(r"assets/Button/Button_Fish.png", (660, 620))  # Adjust the path and position
            SCREEN.blit(FISHING_BUTTON.image, FISHING_BUTTON.rect)
        # Draw the character's and fishing mask on the screen for debugging
        SCREEN.blit(pygame.Surface(self.character.rect.size, pygame.SRCALPHA), self.character.rect)
        SCREEN.blit(pygame.Surface(self.fishing_mask.get_rect().size, pygame.SRCALPHA), self.fishing_mask.get_rect())

        pygame.display.update()


def draw_text(surface, texts, fonts, colors, rect, align="center", max_width=None, max_height=None):
    global y
    lines = []
    current_line = []
    current_line_width = 0
    current_line_height = 0

    for i, text in enumerate(texts):
        words = text.split(' ')
        space_width, space_height = fonts[i].size(' ')

        for word in words:
            word_width, word_height = fonts[i].size(word)
            if (max_width is not None and current_line and current_line_width + space_width + word_width > max_width) or \
                    (max_height is not None and current_line_height + word_height > max_height):
                lines.append(' '.join(current_line))
                current_line = [word]
                current_line_width = word_width
                current_line_height = word_height
            else:
                current_line.append(word)
                current_line_width += space_width + word_width
                current_line_height = max(current_line_height, word_height)

        if current_line:
            lines.append(' '.join(current_line))

    total_height = len(lines) * current_line_height

    if align == "center":
        y = rect.centery - total_height // 2
    elif align == "topleft":
        y = rect.y

    for i, line in enumerate(lines):
        text_surface = fonts[0].render(line, True, colors[0])
        text_rect = text_surface.get_rect(centerx=rect.centerx, y=y)

        outline_surface = fonts[0].render(line, True, (0, 0, 0))
        outline_rect = outline_surface.get_rect(centerx=rect.centerx, y=y)

        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            surface.blit(outline_surface, (outline_rect.x + offset[0], outline_rect.y + offset[1]))

        surface.blit(text_surface, text_rect)
        y += current_line_height

    return total_height


def fishing_screen():
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"assets/Font/Daydream.ttf", 76)
    textbox_font = pygame.font.Font(r"assets/Font/Daydream.ttf", 14)
    fishing_text = "Fishing"
    cooking_text = "Cooking"
    feeding_text = "Feeding"
    dots = ""
    start_time = pygame.time.get_ticks()

    fish_path = get_random_fish()
    fish_description = fish_path['description']
    fish_name = fish_path['name']
    fish_status = fish_path['endangered']

    fish_image = None
    screen_a_image = None
    screen_b_image = None

    cooking_start_time = None
    feeding_start_time = None
    feeding_image_displayed = False

    cooking_duration = 5000
    feeding_duration = 3500

    while True:

        SCREEN.blit(FISHING_BG, (0, 0))
        FISHING_MOUSE_POS = pygame.mouse.get_pos()
        FISHING_BACK = Button(r"assets/Button/Button_Back.png", (50, 50))
        FISHING_BACK.update(SCREEN)
        catch = Button(r"assets/Button/Button_Cook.png", (1100, 560))
        release = Button(r"assets/Button/Button_Release.png", (1100, 650))

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time < 3000:
            draw_text(SCREEN, [f"{fishing_text}{dots}"], [font], [(255, 255, 255)],
                      Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                      "center")
            dots += "."
            if len(dots) > 3:
                dots = ""

        else:
            if fish_image is None:
                fish_image = pygame.image.load(fish_path['image'])
                fish_image = pygame.transform.scale(fish_image, (256, 256))
            fish_rect = fish_image.get_rect(center=(320, 250))
            SCREEN.blit(fish_image, fish_rect)

            draw_text(SCREEN, ["Fish Caught"], [font], [(222, 180, 118)],
                      Rect(690, 75, 0, 0), "center")

            textbox_rect = TEXTBOX_IMAGE.get_rect(center=(320, 550))
            SCREEN.blit(TEXTBOX_IMAGE, textbox_rect)

            if fish_status:
                fish_name_description = f"{fish_name}:{fish_description} Status: ENDANGERED!"
            else:
                fish_name_description = f"{fish_name}:{fish_description}"

            draw_text(SCREEN, [fish_name_description], [textbox_font], [(255, 255, 255)], textbox_rect, "center",
                      max_width=520, max_height=500)

            catch.update(SCREEN)
            release.update(SCREEN)

            if screen_a_image is not None:
                SCREEN.blit(screen_a_image, (0, 0))
            elif screen_b_image is not None:
                SCREEN.blit(screen_b_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FISHING_BACK.checkForInput(pygame.mouse.get_pos()):
                    Play.play()
                    gamesound.play(-1)
                    # Reset cooking time when going back
                    cooking_start_time = None
                    return
                if release.checkForInput(pygame.mouse.get_pos()):
                    buttonsfx.play()  # Play button click sound
                    gamesound.play(-1)
                    return
                if catch.checkForInput(pygame.mouse.get_pos()):
                    buttonsfx.play()  # Play button click sound
                    if fish_status:
                        screen_a_image = pygame.image.load("assets/Map/Jail.png")
                        screen_b_image = None
                        cookb.play()
                    else:
                        screen_b_image = pygame.image.load("assets/Map/KitchenI.png")
                        screen_a_image = None
                        cooking_start_time = pygame.time.get_ticks()
                        cooka.play()

        if cooking_start_time:
            elapsed_cooking_time = pygame.time.get_ticks() - cooking_start_time
            if elapsed_cooking_time < cooking_duration:
                if screen_b_image is not None:
                    SCREEN.blit(screen_b_image, (0, 0))
                    draw_text(SCREEN, [f"{cooking_text}{dots}"], [font], [(255, 255, 255)],
                              Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                              "center")
                    dots += "."
                    if len(dots) > 3:
                        dots = ""
            else:
                cooking_start_time = None
                feeding_start_time = pygame.time.get_ticks()
                cookingdonesound.play()  # Play cooking done sound effect

        if feeding_start_time:
            food = pygame.image.load(r"assets/Map/BackgroundFood.png")
            elapsed_feeding_time = pygame.time.get_ticks() - feeding_start_time
            if elapsed_feeding_time < feeding_duration:
                SCREEN.blit(food, (0, 0))
                draw_text(SCREEN, [f"{feeding_text}{dots}"], [font], [(255, 255, 255)],
                          Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0), "center")
                dots += "."
                if len(dots) > 3:
                    dots = ""
            else:
                feeding_start_time = None
                feeding_image_displayed = True

        if feeding_image_displayed:
            SCREEN.blit(food, (0, 0))
            draw_text(SCREEN, ["Thank you!"], [font], [(222, 180, 118)],
                      Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0), "center")

        FISHING_BACK.update(SCREEN)
        pygame.display.update()
        clock.tick(3)


if __name__ == "__main__":
    main_menu()
