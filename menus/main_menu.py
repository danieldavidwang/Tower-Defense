import asyncio
import pygame

play_button = pygame.image.load("./sprites/play_button.png")

class MainMenu:
    def __init__(self, win):
        self.width = 900
        self.height = 700
        self.win = win
        self.background = pygame.image.load("./sprites/background.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.button = (self.width/2 - play_button.get_width()/2, 350, play_button.get_width(), play_button.get_height())
        self.title = pygame.transform.scale(pygame.image.load("./sprites/title.png"), (500, 200))

    async def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if self.button[0] <= x <= self.button[0] + self.button[2]:
                        if self.button[1] <= y <= self.button[1] + self.button[3]:
                            return "game"
            self.draw_menu()
            # Pygbag needs the event loop to yield once per frame so the
            # browser can draw the canvas and process input.
            await asyncio.sleep(0)
    
    def draw_menu(self):
        self.win.blit(self.background, (0,0))
        self.win.blit(self.title, (self.width/2 - self.title.get_width()/2, self.height/2 - self.title.get_height()/2 - 100))
        self.win.blit(play_button, (self.button[0], self.button[1]))
        pygame.display.update()
