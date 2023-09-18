import pygame
import config

class Npc:
    def __init__(self, name, image, x_position, y_position):
        """
        Initializes an NPC with the provided name, image, and position.
        """
        self.name = name
        self.position = [x_position, y_position]
        self.image = self.load_and_scale_image(image)
        self.rect = self.create_rect(self.position)
        self.monster = None
        self.monsters = []

    @staticmethod
    def load_and_scale_image(image_name):
        """
        Loads and scales an image based on the image name.
        """
        image_path = f"imgs/{image_name}.png"
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (config.SCALE, config.SCALE))

    @staticmethod
    def create_rect(position):
        """
        Creates a pygame rectangle based on the given position and SCALE.
        """
        x, y = position
        return pygame.Rect(x * config.SCALE, y * config.SCALE, config.SCALE, config.SCALE)

    def update(self):
        """
        Updates the NPC (placeholder method).
        """
        pass

    def update_position(self, new_position):
        """
        Updates the NPC's position to the new position.
        """
        self.position[0], self.position[1] = new_position

    def render(self, screen, camera):
        """
        Renders the NPC on the screen at the updated position.
        """
        cam_x, cam_y = camera
        self.rect = self.create_rect([self.position[0] - cam_x, self.position[1] - cam_y])
        screen.blit(self.image, self.rect)
