class FishingScreen:
    def __init__(self):
        self.background = pygame.image.load(r"assets\Map\FishingScreenBackground.png")

    def play(self):
        while True:
            SCREEN.blit(self.background, (0, 0))

            # Add fishing screen logic here

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
