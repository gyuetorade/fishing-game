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
pygame.display.set_caption("Fishing Screen")

FISHING_BG = pygame.image.load(r"assets/Map/BackgroundFishing.png")  # Adjust the path
TEXTBOX_IMAGE = pygame.image.load(r"assets/Others/textbox.png")  # Adjust the path


def draw_text(surface, text, font, color, rect, align="center", max_width=None, max_height=None, outline_color=(0, 0, 0), outline_width=2):
    # Helper function to draw centered text on a surface with word wrapping and outline
    words = text.split(' ')
    space_width, space_height = font.size(' ')

    lines = []
    current_line = []
    current_line_width = 0
    current_line_height = 0

    for word in words:
        word_width, word_height = font.size(word)
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

    for line in lines:
        # Draw the black outline first
        text_surface = font.render(line, True, outline_color)
        text_rect = text_surface.get_rect(centerx=rect.centerx, y=y)
        text_rect.inflate_ip(outline_width * 2, outline_width * 2)  # Expand the rectangle for the outline
        surface.blit(text_surface, text_rect)

        # Draw the actual text
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(centerx=rect.centerx, y=y)
        surface.blit(text_surface, text_rect)

        y += current_line_height

def fishing_screen():
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"assets/Font/Daydream.ttf", 70)  # Adjust the path and size
    textbox_font = pygame.font.Font(r"assets/Font/Daydream.ttf", 19)
    fishing_text = "Fishing"
    dots = ""
    start_time = pygame.time.get_ticks()  # Record the start time

    # Generate a random fish path and description outside the loop
    fish_path = get_random_fish()
    fish_description = ("This is a random fish description."
                        " It might be a very long description that needs to be word-wrapped "
                        "to fit inside the textbox image without errors.")

    while True:
        SCREEN.blit(FISHING_BG, (0, 0))
        FISHING_MOUSE_POS = pygame.mouse.get_pos()

        FISHING_BACK = Button(r"assets/Button/Button_Back.png", (50, 50))  # Adjust the path and position
        FISHING_BACK.update(SCREEN)

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time < 5000:  # Display "Fishing" for the first 3 seconds
            draw_text(SCREEN, f"{fishing_text}{dots}", font, (255, 255, 255),
                      Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
                      "center")
            dots += "."  # Add a dot to the animation
            if len(dots) > 3:
                dots = ""  # Reset dots after reaching three
        else:
            fish_image = pygame.image.load(fish_path)
            fish_image = pygame.transform.scale(fish_image, (256, 256))
            fish_rect = fish_image.get_rect(center=(320, 250))  # Adjust position

            SCREEN.blit(fish_image, fish_rect)
            draw_text(SCREEN, "Fish Caught", font, (222, 180, 118),
                      Rect(690, 75, 0, 0), "center")
            # Display the text box image
            textbox_rect = TEXTBOX_IMAGE.get_rect(center=(320, 550))
            SCREEN.blit(TEXTBOX_IMAGE, textbox_rect)

            # Display the fish description inside the text box with word wrapping
            draw_text(SCREEN, fish_description, textbox_font, (255, 255, 255), textbox_rect, "center", max_width=500,
                      max_height=100, outline_color=(0, 0, 0), outline_width=0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FISHING_BACK.checkForInput(FISHING_MOUSE_POS):
                    print("Back button clicked!")
                    return  # Return from the fishing_screen function to go back to the main menu

        pygame.display.update()
        clock.tick(3)  # Adjust the frame rate
