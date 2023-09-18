import pygame
import config
import math
from building import Building
from npc import Npc

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]
        self.file_name = None
        self.player_exit_position = None
        self.objects = []
        self.exit_positions = []

    def load(self, file_name, player):
        """Load the map configuration and tiles."""
        self.file_name = file_name
        self.player = player
        self.objects = [player]
        
        # Read map tiles from file
        with open(f'maps/{file_name}.txt') as map_file:
            self.map_array = [list(line[::2]) for line in map_file]
            print(self.map_array)

        # Load the map configuration (buildings, exits, etc.)
        map_config = config.MAP_CONFIG[file_name]
        player.position = map_config['start_position'][:]
        self.objects.extend([Building(data['sprite'], data['position'], data['size']) for data in map_config["buildings"]])
        self.exit_positions = map_config['exits']

    def load_room(self, map_name, room_name, player):
        """Load room details and NPCs."""
        self.player = player
        self.objects = [player]
        room_config = config.ROOM_CONFIG[map_name][str(room_name).zfill(2)]
        player.position = room_config['start_position'][:]
        self.player_exit_position = room_config['exit_position'][:]
        
        # Add NPCs to the room
        self.objects.extend([Npc(data['name'], data['image'], data['start_position'][0], data['start_position'][1]) for data in room_config['npcs']])
        
        # Read room tiles from file
        with open(f'rooms/{map_name}/{str(room_name).zfill(2)}.txt') as room_file:
            self.map_array = [list(line[::2]) for line in room_file]
            print(self.map_array)

    def render(self, screen, player):
        """Render the map and its objects."""
        self.determine_camera(player)
        
        # Render tiles on screen
        for y, line in enumerate(self.map_array):
            for x, tile in enumerate(line):
                if tile in map_tile_image:
                    image = map_tile_image[tile]
                    rect = pygame.Rect(x * config.SCALE - self.camera[0] * config.SCALE, y * config.SCALE - self.camera[1] * config.SCALE, config.SCALE, config.SCALE)
                    screen.blit(image, rect)
        
        # Render objects (like player, NPCs) on screen
        for obj in self.objects:
            obj.render(self.screen, self.camera)

    def determine_camera(self, player):
        """Determine camera position based on player position."""
        self.camera[1] = self._determine_camera_axis(player.position[1], len(self.map_array), config.SCREEN_HEIGHT)
        self.camera[0] = self._determine_camera_axis(player.position[0], len(self.map_array[0]), config.SCREEN_WIDTH)

    def _determine_camera_axis(self, position, map_length, screen_length):
        """Helper function to calculate camera axis position."""
        max_position = map_length - screen_length / config.SCALE
        current_position = position - math.ceil(screen_length / config.SCALE / 2)
        if 0 <= current_position <= max_position:
            return current_position
        elif current_position < 0:
            return 0
        else:
            return max_position
            
# Dictionary of map tiles with their corresponding images
map_tile_image = {
    key: pygame.transform.scale(pygame.image.load(value), (config.SCALE, config.SCALE))
    for key, value in {
        config.MAP_TILE_GRASS: "imgs/grass1.png",
        config.MAP_TILE_WATER: "imgs/water.png",
        config.MAP_TILE_ROAD: "imgs/road.png",
        config.MAP_TILE_LAB_FLOOR: "imgs/lab_tile.png",
        config.MAP_TILE_LAB_WALL: "imgs/lab_wall.png",
        config.MAP_TILE_ROOM_EXIT: "imgs/floor_mat.png"
    }.items()
}
