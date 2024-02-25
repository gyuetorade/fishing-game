import pygame
import sys
from button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fishing Screen")

FISHING_BG = pygame.image.load(r"assets/Map/FishingScreenBackground.png")  # Adjust the path

def fishing_screen():
    while True:
        SCREEN.blit(FISHING_BG, (0, 0))
        FISHING_MOUSE_POS = pygame.mouse.get_pos()

        FISHING_BACK = Button(r"assets/Button/Button_Back.png", (50, 50))  # Adjust the path and position
        FISHING_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FISHING_BACK.checkForInput(FISHING_MOUSE_POS):
                    print("Back button clicked!")
                    return  # Return from the fishing_screen function to go back to the main menu

        pygame.display.update()