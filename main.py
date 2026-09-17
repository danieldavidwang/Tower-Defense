import asyncio

import pygame


WIDTH = 900
HEIGHT = 700


async def main():
    """Run the game on desktop Python or in a Pygbag browser build."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")

    # Import after creating the display because several modules load and
    # convert image assets as soon as they are imported.
    from game import Game
    from menus.main_menu import MainMenu
    from menus.win_menu import WinMenu

    state = "menu"
    screens = {
        "menu": MainMenu,
        "game": Game,
        "win": WinMenu,
    }

    while state != "quit":
        state = await screens[state](window).run()

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
