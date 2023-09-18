import pygame
import config

from game_state import GameState


class Battle:
    def __init__(self, screen, monster, player):
        self.screen = screen
        self.monster = monster
        self.player = player
        self.battle_images = self.load_battle_images()
        self.font = pygame.font.Font("fonts/PokemonGb.ttf", 16)

    def load(self):
        """Placeholder for loading battle-specific resources if needed in the future."""
        pass

    def load_battle_images(self):
        """Load and scale battle-related images."""
        return {
            "monster_pad": pygame.transform.scale(pygame.image.load("imgs/battle/monster_pad.png"), (300, 88)),
            "name_card": pygame.transform.scale(pygame.image.load("imgs/battle/name_card.png"), (300, 80)),
            "hp_bar": pygame.transform.scale(pygame.image.load("imgs/battle/hp_bar.png"), (250, 20)),
            "menu": pygame.image.load("imgs/battle/menu.png"),
        }

    def render(self):
        """Render the battle screen and its components."""
        self.screen.fill(config.WHITE)
        self.draw_battle_elements()
        self.draw_monsters_and_data()
        self.draw_battle_message()

    def draw_battle_elements(self):
        """Draw static elements like the monster pad, name card, and other UI components."""
        self.screen.blit(self.battle_images["monster_pad"], (0, 300))
        self.screen.blit(self.battle_images["name_card"], (310, 300))
        self.screen.blit(self.battle_images["hp_bar"], (340, 335))
        self.screen.blit(self.battle_images["monster_pad"], (300, 100))
        self.screen.blit(self.battle_images["name_card"], (15, 100))
        self.screen.blit(self.battle_images["hp_bar"], (50, 135))
        self.screen.blit(self.battle_images["menu"], (0, 388))

    def draw_monsters_and_data(self):
        """Draw the monsters and related information such as health, name, level, etc."""
        # Drawing the player's monster and its details
        self.screen.blit(self.player.monsters[0].image, (70, 250))
        img = self.font.render(str(self.player.monsters[0].name), True, config.BLACK)
        self.screen.blit(img, (323, 311))
        img = self.font.render(f"Lv{self.player.monsters[0].level}", True, config.BLACK)
        self.screen.blit(img, (555, 311))
        player_monster_percent = self.player.monsters[0].health / self.player.monsters[0].base_health
        player_monster_color = self.determine_health_color(player_monster_percent)
        pygame.draw.rect(self.screen, player_monster_color, pygame.Rect(381, 337, config.BATTLE_HEALTH_BAR_WIDTH * player_monster_percent, 16))

        # Drawing the enemy monster and its details
        self.screen.blit(self.monster.image, (370, 30))
        img = self.font.render(self.monster.name, True, config.BLACK)
        self.screen.blit(img, (25, 110))
        img = self.font.render(f"Lv{self.monster.level}", True, config.BLACK)
        self.screen.blit(img, (260, 110))
        monster_percent = self.monster.health / self.monster.base_health
        monster_color = self.determine_health_color(monster_percent)
        pygame.draw.rect(self.screen, monster_color, pygame.Rect(91, 137, config.BATTLE_HEALTH_BAR_WIDTH * monster_percent, 16))
        img = self.font.render(f"health: {self.monster.health} Attack: {self.monster.attack}", True, config.BLACK)
        self.screen.blit(img, (25, 155))

    def update(self):
        """Check and process events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                self.handle_key_event(event)

    def handle_key_event(self, event):
        """Handle keypress events."""
        if event.key == pygame.K_ESCAPE:
            self.game.game_state = GameState.ENDED
        elif event.key == pygame.K_RETURN:
            self.monster.health -= 1

    def determine_health_color(self, monster_percent):
        """Determine health color based on health percentage."""
        if monster_percent < .25:
            return config.RED
        if monster_percent < .7:
            return config.YELLOW
        return config.GREEN
    
    def draw_battle_message(self):
        """Draw battle-related messages, such as instructions or battle outcomes."""
        img = self.font.render("press enter to attack!", True, config.WHITE)
        self.screen.blit(img, (30, 430))
