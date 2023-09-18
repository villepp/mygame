import pygame

import config
from game_state import GameState
from monsterfactory import MonsterFactory

class PickMonsterEvent:
    def __init__(self, screen, game, player, monster):
        self.screen = screen
        self.game = game
        self.player = player
        self.dialog = pygame.image.load("imgs/dialog.png")
        self.monster_factory = MonsterFactory()
        self.font = pygame.font.Font('fonts/PokemonGb.ttf', 20)

        self.monster_mapping = {
            "monster_cage_starter_01": 1,
            "monster_cage_starter_02": 4,
            "monster_cage_starter_03": 7
        }

        monster_index = self.monster_mapping.get(monster.name)
        if monster_index:
            self.monster = self.monster_factory.create_monster_index(monster_index)
        else:
            raise ValueError(f"Monster name {monster.name} not recognized.")

    def render(self):
        self.screen.blit(self.dialog, (0, 300))
        self.screen.blit(self.monster.image, (100, 100))

        monster_text = self.font.render("You picked... " + str(self.monster.name), True, config.BLACK)
        self.screen.blit(monster_text, (40, 350))

        confirmation_text = self.font.render("Are you sure? (y/n)", True, config.BLACK)
        self.screen.blit(confirmation_text, (40, 400))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_y:
                    self.player.monsters.append(self.monster)
                    self.game.event = None
                elif event.key == pygame.K_n:
                    self.game.event = None  # Optionally transition to a different event or screen
