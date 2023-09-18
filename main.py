"""
main.py
A script to initialize and control the main game loop for "Game Title".
"""

import pygame
import config
from game_state import GameState
from game import Game
from menu import Menu

# Initialization
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 50

game = Game(screen)
menu = Menu(screen, game)
menu.set_up()

# Mapping game states to corresponding update functions.
# This acts like a substitute for a switch-case.
update_functions = {
    GameState.NONE: menu.update,
    GameState.RUNNING: game.update
}

# Main Game Loop
while game.game_state != GameState.ENDED:
    clock.tick(FRAMES_PER_SECOND)
    
    # Update the game or menu based on the current game state
    update_function = update_functions.get(game.game_state)
    if update_function:
        update_function()
        
    pygame.display.flip()
