import pygame
import sys
from button import Button
from pygame.locals import Rect

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fishing Screen")

FISHING_BG = pygame.image.load(r"assets/Map/FishingScreenBackground.png")  # Adjust the path


def draw_text(surface, text, font, color, rect, align="center"):
    # Helper function to draw centered text on a surface
    text_surface = font.render(text, True, color)

    if align == "center":
        text_rect = text_surface.get_rect(center=rect.center)
    elif align == "topleft":
        text_rect = text_surface.get_rect(topleft=rect.topleft)
    # Add more cases for other alignment options if needed

    surface.blit(text_surface, text_rect)
def fishing_screen():
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"assets/Font/Daydream.ttf", 54)  # Adjust the path and size

    fishing_text = "Fishing"
    dots = ""
    start_time = pygame.time.get_ticks()  # Record the start time

    while True:
        SCREEN.blit(FISHING_BG, (0, 0))
        FISHING_MOUSE_POS = pygame.mouse.get_pos()

        FISHING_BACK = Button(r"assets/Button/Button_Back.png", (50, 50))  # Adjust the path and position
        FISHING_BACK.update(SCREEN)

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time < 3000:  # Display "Fishing" for the first 3 seconds
            draw_text(SCREEN, f"{fishing_text}{dots}", font, (255, 255, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                      "center")
            dots += "."  # Add a dot to the animation
            if len(dots) > 3:
                dots = ""  # Reset dots after reaching three
        else:
            draw_text(SCREEN, "Fish Caught", font, (255, 255, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), "center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FISHING_BACK.checkForInput(FISHING_MOUSE_POS):
                    print("Back button clicked!")
                    return  # Return from the fishing_screen function to go back to the main menu

        pygame.display.update()
        clock.tick(5)  # Adjust the frame rate