import pygame

import config
from game_state import GameState

class ProfPickMonsterEvent:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.prof_image = pygame.image.load("imgs/prof.png")
        self.dialog = pygame.image.load("imgs/dialog.png")
        
        self.cut = 0
        self.max_cut = 2
        self.font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        self.scenes = [self.render_scene_0, self.render_scene_1, self.render_scene_2]

    def render(self):
        if self.cut <= self.max_cut:
            self.scenes[self.cut]()
            
    def render_scene_0(self):
        self._render_dialog("Hello! I am the Prof.")
        
    def render_scene_1(self):
        self._render_dialog("Pick your monster!")
        
    def render_scene_2(self):
        self._render_dialog("Choose wisely...")
        
    def _render_dialog(self, text):
        self.screen.blit(self.dialog, (0, 300))
        dialog_img = self.font.render(text, True, config.BLACK)
        self.screen.blit(dialog_img, (40, 400))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_RETURN and self.cut <= self.max_cut:
                    self.cut += 1
                    if self.cut > self.max_cut:
                        self.game.event = None
