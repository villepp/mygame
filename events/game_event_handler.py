from events.pick_monster_event import PickMonsterEvent
from events.prof_pick_monster_event import ProfPickMonsterEvent

def handle_prof_event(game, player, npc):
    """Handle the event when the player interacts with the professor.
    
    Args:
        game (Game): The main game object.
        player (Player): The player object.
        npc (Npc): The Non-Player Character object that player interacts with.
    """
    # If player already has monsters, don't initiate the event again.
    if len(player.monsters) != 0:
        return
    
    # Create and assign a ProfPickMonsterEvent to the game.
    event = ProfPickMonsterEvent(game.screen, game, player)
    game.event = event

def handle_pick_monster_event(game, player, npc):
    """Handle the event when the player picks a monster from a cage.
    
    Args:
        game (Game): The main game object.
        player (Player): The player object.
        npc (Npc): The Non-Player Character object representing the monster cage.
    """
    # If player already has monsters, don't initiate the event again.
    if len(player.monsters) != 0:
        return
    
    # Create and assign a PickMonsterEvent to the game.
    event = PickMonsterEvent(game.screen, game, player, npc)
    game.event = event
        
def handle(game, player, npc):
    """Main event handler for player interactions with NPCs.
    
    Args:
        game (Game): The main game object.
        player (Player): The player object.
        npc (Npc): The Non-Player Character object that player interacts with.
    """
    # Revert player's position to the last known position.
    player.position = player.last_position
    
    # Check if player interacts with the professor and handle it.
    if npc.name == 'prof':
        handle_prof_event(game, player, npc)
        
    # Check if player interacts with a monster cage and handle it.
    if npc.name.startswith("monster_cage_starter_"):
        handle_pick_monster_event(game, player, npc)
