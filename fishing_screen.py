# fishing_screen.py

import pygame
import sys
from button import Button
from pygame.locals import Rect
from fishies import get_random_fish

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


FISHING_BG = pygame.image.load(r"assets/Map/BackgroundFishing.png")  # Adjust the path
TEXTBOX_IMAGE = pygame.image.load(r"assets/Others/textbox.png")  # Adjust the path


def draw_text(surface, texts, fonts, colors, rect, align="center", max_width=None, max_height=None):
    # Helper function to draw centered text on a surface with word wrapping
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
        text_surface = fonts[0].render(line, True, colors[0])  # Use fonts[0] and colors[0] for now
        text_rect = text_surface.get_rect(centerx=rect.centerx, y=y)

        # Create an outline surface
        outline_surface = fonts[0].render(line, True, (0, 0, 0))  # Use fonts[0] for now
        outline_rect = outline_surface.get_rect(centerx=rect.centerx, y=y)

        # Blit the outline surface multiple times to create the outline effect
        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            surface.blit(outline_surface, (outline_rect.x + offset[0], outline_rect.y + offset[1]))

        # Blit the actual text surface
        surface.blit(text_surface, text_rect)
        y += current_line_height

    return total_height


def fishing_screen():
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"assets/Font/Daydream.ttf", 76)  # Adjust the path and size
    textbox_font = pygame.font.Font(r"assets/Font/Daydream.ttf", 14)
    fishing_text = "Fishing"
    cooking_text = "Cooking"
    feeding_text = "Feeding"
    dots = ""
    cooking_start_time = None
    cooking_duration = 3000  # Adjust the cooking animation duration (in milliseconds)
    feeding_start_time = None
    feeding_duration = 3000  # Adjust the feeding animation duration (in milliseconds)
    feeding_image_displayed = False  # Initialize feeding_image_displayed

    fish_path = get_random_fish()
    fish_description = fish_path['description']
    fish_name = fish_path['name']
    fish_status = fish_path['endangered']

    fish_image = None
    screen_a_image = None
    screen_b_image = None

    while True:
        SCREEN.blit(FISHING_BG, (0, 0))
        FISHING_BACK = Button(r"assets/Button/Button_Back.png", (50, 50))  # Adjust the path and position
        FISHING_BACK.update(SCREEN)
        catch = Button(r"assets/Button/Button_Cook.png", (1100, 560))  # Adjust the path and position
        release = Button(r"assets/Button/Button_Release.png", (1100, 650))  # Adjust the path and position

        elapsed_time = pygame.time.get_ticks()  # Record elapsed time

        if elapsed_time < 3000:  # Display "Fishing" for the first 3 seconds
            draw_text(SCREEN, [f"{fishing_text}{dots}"], [font], [(255, 255, 255)],
                      Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                      "center")
            dots += "."  # Add a dot to the animation
            if len(dots) > 3:
                dots = ""  # Reset dots after reaching three
        else:
            if fish_image is None:
                fish_image = pygame.image.load(fish_path['image'])
                fish_image = pygame.transform.scale(fish_image, (256, 256))
            fish_rect = fish_image.get_rect(center=(320, 250))  # Adjust position
            SCREEN.blit(fish_image, fish_rect)

            draw_text(SCREEN, ["Fish Caught"], [font], [(222, 180, 118)],
                      Rect(690, 75, 0, 0), "center")

            # Display the text box image
            textbox_rect = TEXTBOX_IMAGE.get_rect(center=(320, 550))
            SCREEN.blit(TEXTBOX_IMAGE, textbox_rect)

            # textbox content
            if fish_status:
                fish_name_description = f"{fish_name}:{fish_description} Status: ENDANGERED!"
            else:
                fish_name_description = f"{fish_name}:{fish_description}"

            # Display the fish name and description inside the text box with word wrapping
            draw_text(SCREEN, [fish_name_description], [textbox_font], [(255, 255, 255)], textbox_rect, "center",
                      max_width=520, max_height=500)

            # Update and draw the buttons
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
                    return  # Return from the fishing_screen function to go back to the main menu
                if release.checkForInput(pygame.mouse.get_pos()):
                    return
                if catch.checkForInput(pygame.mouse.get_pos()):
                    print("Button 1 clicked!")
                    # Call the cook_fish function and pass fish_status as argument
                    if fish_status:  # If endangered is True
                        # Display screen A
                        screen_a_image = pygame.image.load("assets/Map/Jail.png")  # Adjust the path
                        screen_b_image = None
                    else:
                        # Display screen B
                        screen_b_image = pygame.image.load("assets/Map/Kitchen.png")  # Adjust the path
                        screen_a_image = None
                        cooking_start_time = pygame.time.get_ticks()  # Start cooking animation timer

        # Display cooking animation if cooking is ongoing
        if cooking_start_time:
            if elapsed_time - cooking_start_time < cooking_duration:
                if screen_b_image is not None:
                    SCREEN.blit(screen_b_image, (0, 0))
                    draw_text(SCREEN, [f"{cooking_text}{dots}"], [font], [(255, 255, 255)],
                              Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                              "center")
                    dots += "."  # Add a dot to the animation
                    if len(dots) > 3:
                        dots = ""  # Reset dots after reaching three
            else:
                cooking_start_time = None  # Stop cooking animation
                feeding_start_time = pygame.time.get_ticks()  # Start feeding animation timer

        # Display feeding animation if feeding is ongoing
        if feeding_start_time:
            if elapsed_time - feeding_start_time < feeding_duration:
                SCREEN.blit(screen_b_image, (0, 0))
                draw_text(SCREEN, [f"{feeding_text}{dots}"], [font], [(255, 255, 255)],
                          Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                          "center")
                dots += "."  # Add a dot to the animation
                if len(dots) > 3:
                    dots = ""  # Reset dots after reaching three
            else:
                feeding_start_time = None  # Stop feeding animation
                feeding_image_displayed = True

        # Display "Thank you" after feeding animation is completed
        if feeding_image_displayed:
            draw_text(SCREEN, ["Thank you!"], [font], [(222, 180, 118)],
                      Rect(690, 75, 0, 0), "center")

        FISHING_BACK.update(SCREEN)
        pygame.display.update()
        clock.tick(3)



