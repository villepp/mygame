import pygame
import config

PLAYER_IMG_PATH = "imgs/player.png"


class Player:
    def __init__(self, x_position, y_position):
        """
        Initializes the player with the given position, loads and scales the player's image.
        """
        print("player created")
        self.position = [x_position, y_position]
        self.last_position = self.position.copy()
        
        self.image = self.load_and_scale_image(PLAYER_IMG_PATH)
        self.rect = self.create_rect(self.position)
        
        self.monster = None
        self.monsters = []

    @staticmethod
    def load_and_scale_image(image_path):
        """Load and scale an image to the configured SCALE."""
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (config.SCALE, config.SCALE))

    @staticmethod
    def create_rect(position):
        """Creates a pygame rectangle based on the given position and SCALE."""
        x, y = position
        return pygame.Rect(x * config.SCALE, y * config.SCALE, config.SCALE, config.SCALE)

    def update_position(self, new_position):
        """Update the player's position to the new position."""
        self.last_position = self.position.copy()
        self.position[0], self.position[1] = new_position

    def render(self, screen, camera):
        """Render the player's image on the screen at the updated position."""
        cam_x, cam_y = camera
        self.rect = self.create_rect([self.position[0] - cam_x, self.position[1] - cam_y])
        screen.blit(self.image, self.rect)
