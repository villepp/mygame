import pygame
import config

class Building:
    def __init__(self, image_name, position, size):
        self.position = list(position)
        self.size = list(size)
        self.set_image(image_name)
        self.rect = self.calculate_rect(camera=(0, 0))  # initializing with default camera position 

    def set_image(self, image_name):
        """Load and scale the building's image."""
        image_path = f"imgs/rooms/{image_name}.png"
        image = pygame.image.load(image_path)
        scaled_size = (self.size[0] * config.SCALE, self.size[1] * config.SCALE)
        self.image = pygame.transform.scale(image, scaled_size)

    def calculate_rect(self, camera):
        """Calculate the building's rect based on its position and the camera."""
        x = self.position[0] * config.SCALE - camera[0] * config.SCALE
        y = self.position[1] * config.SCALE - camera[1] * config.SCALE
        width = config.SCALE
        height = config.SCALE
        return pygame.Rect(x, y, width, height)

    def update(self):
        pass  # Placeholder for future functionality if needed

    def render(self, screen, camera):
        self.rect = self.calculate_rect(camera)
        screen.blit(self.image, self.rect)
