import pygame
import config
import configmonster

class Monster:
    def __init__(self, monster_type, id):
        """
        Initializes a monster with the provided type and ID.
        """
        self.type = monster_type
        self.health = 10
        self.attack = 10
        self.id = id
        self.image = self.load_monster_image()
        self.name = self.get_monster_name()
        self.level = self.get_monster_starting_level()
        self.base_health = self.get_monster_base_health()

    def load_monster_image(self):
        """
        Loads the monster's image based on its ID.
        """
        image_path = f"imgs/monsters/{self.id:03d}.png"
        return pygame.image.load(image_path)

    def get_monster_name(self):
        """
        Retrieves the monster's name from the configuration.
        """
        return configmonster.MONSTERS[self.id]['name']

    def get_monster_starting_level(self):
        """
        Retrieves the monster's starting level from the configuration.
        """
        return configmonster.MONSTERS[self.id]['level_start']

    def get_monster_base_health(self):
        """
        Retrieves the monster's base health from the configuration.
        """
        return configmonster.MONSTERS[self.id]['base_health']

    def update(self):
        """
        Updates the monster (placeholder method).
        """
        pass
