import pygame
import config
from game_state import GameState

MENU_IMAGE_PATH = "imgs/menu.png"


class Menu:
    def __init__(self, screen, game):
        """
        Initializes the menu with the provided screen and game objects.
        """
        self.screen = screen
        self.game = game
        self.menu_image = self.load_image(MENU_IMAGE_PATH)

    @staticmethod
    def load_image(image_path):
        """Loads an image from the given path."""
        return pygame.image.load(image_path)

    def render_menu(self):
        """Renders the main menu on the screen."""
        self.screen.fill(config.BLACK)
        rect = self.menu_image.get_rect()
        self.screen.blit(self.menu_image, rect)

    def handle_key_events(self, event):
        """Handles key events within the menu context."""
        if event.key == pygame.K_ESCAPE:
            self.game.game_state = GameState.ENDED
        elif event.key == pygame.K_RETURN:
            self.game.set_up()
            self.game.game_state = GameState.RUNNING

    def update(self):
        """Updates the menu display and listens for events."""
        self.render_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)
                
    def set_up(self):
        """
        Any additional setup procedures for the menu can be added here.
        """
        pass
