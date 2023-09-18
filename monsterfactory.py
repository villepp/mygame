import utilities
import configmonster
from monster import Monster

class MonsterFactory:
    def __init__(self):
        self.count = 0

    def create_monster_index(self, index):
        """
        Create a monster by providing an index.
        """
        monster_type = configmonster.MONSTERS[index]['monster_type']
        monster = Monster(monster_type, index)
        self.count += 1
        return monster

    def create_monster(self, monster_type):
        """
        Create a random monster based on the provided monster type.
        """
        random_number = -1

        if monster_type == "G":
            random_number = utilities.generate_random_number(configmonster.GRASS_TYPE_START, configmonster.GRASS_TYPE_END)

        monster = Monster(monster_type, random_number)
        self.count += 1
        return monster
