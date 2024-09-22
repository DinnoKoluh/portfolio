from tile import Tile
import matplotlib.pyplot as plt

import random
import numpy as np
import copy


class Grid:
    def __init__(self, dimension, tile_list: list[Tile]):
        self.tile_list = self.setup_tile_list(tile_list) # all possible tiles after rotations are done
        self.dimension = dimension
        self.grid = [[Tile() for _ in range(dimension)] for _ in range(dimension)]
        self.tile_images = self.initiate_tile_images(self.tile_list)
        self.entropy_grid = [[self.tile_list for _ in range(dimension)] for _ in range(dimension)]
        _, self.axs = plt.subplots(self.dimension, self.dimension, figsize=(2 * self.dimension, 2 * self.dimension))

    def get_grid(self):
        return self.grid
    
    @staticmethod
    def rotate_sockets(sockets: dict, k):
        """
        Rotate socket encodings of a tile by k * 90 degrees.
        """
        edge_names = list(sockets.keys())
        socket_encodings = list(sockets.values())
        rotations = k % 4 
        # Rotate the values list
        socket_encodings_rot = socket_encodings[-rotations:] + socket_encodings[:-rotations]
        # Create the new dictionary with rotated values
        rotated_sockets = dict(zip(edge_names, socket_encodings_rot))
        return rotated_sockets
    
    @staticmethod
    def is_rotation_unique(rotated_sockets: dict, rotated_tile_list: list[Tile]):
        for tile in rotated_tile_list:
            if rotated_sockets == tile.get_sockets():
                return False
        return True
    
    @staticmethod
    def setup_tile_list(tile_list: list[Tile]):
        """
        Find all the possible tile rotations and extend the tile list with these rotations.
        """
        extended_tile_list = []
        for tile in tile_list:
            rotated_tile_list = []
            rotated_tile_list.append(tile)
            for k in range(1, 4):
                rotated_sockets = Grid.rotate_sockets(copy.deepcopy(tile.get_sockets()), k)
                if Grid.is_rotation_unique(rotated_sockets, rotated_tile_list):
                    rotated_tile_list.append(Tile(name=f"{tile.name}_{k}", sockets=rotated_sockets, tile_path=tile.tile_path, rotation=k))
            extended_tile_list = extended_tile_list + rotated_tile_list
        return extended_tile_list
    
    def get_tile_image(self, tile: Tile):
        return self.tile_images[tile.name]
    
    def initiate_collapse(self, tile: Tile, coordinates: tuple[int, int] | None = None, animate=False):
        if coordinates is None:
            coordinates = (random.randint(0, self.dimension-1), random.randint(0, self.dimension-1))
            print(f"Initial coordinates: {coordinates}")
        x, y = coordinates
        tile.collapsed = True
        self.grid[x][y] = tile
        self.entropy_grid[x][y] = []

        for _ in range(self.dimension**2 - 1):
            self.evaluate_entropy_grid()
            x, y = self.get_smallest_entropy_coordinates()
            self.grid[x][y] = random.choice(self.entropy_grid[x][y]) # grid cell gets a random tile from entropy grid assigned
            self.grid[x][y].collapsed = True
            self.entropy_grid[x][y] = []
            if animate:
                plt.pause(0.1)
                self.grid_animation()
        if animate:
            plt.show()
        self.evaluate_entropy_grid()


    def get_possible_tiles_for_direction(self, tile_list: list[Tile], direction, tile: Tile):
        possible_tiles = []
        for t in tile_list:
            if tile.possible_connections(t)[direction]:
                possible_tiles.append(t)
        return possible_tiles

    def evaluate_entropy_grid(self):
        """
        Go through the whole entropy grid and check which tile choices to remove.
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grid[i][j].is_collapsed():
                    if j > 0 and not self.grid[i][j-1].is_collapsed():
                        self.entropy_grid[i][j-1] = self.get_possible_tiles_for_direction(self.entropy_grid[i][j-1], "left", self.grid[i][j])
                    if j < self.dimension - 1 and not self.grid[i][j+1].is_collapsed():
                        self.entropy_grid[i][j+1] = self.get_possible_tiles_for_direction(self.entropy_grid[i][j+1], "right", self.grid[i][j])
                    if i < self.dimension - 1 and not self.grid[i+1][j].is_collapsed():
                        self.entropy_grid[i+1][j] = self.get_possible_tiles_for_direction(self.entropy_grid[i+1][j], "down", self.grid[i][j])
                    if i > 0 and not self.grid[i-1][j].is_collapsed():
                        self.entropy_grid[i-1][j] = self.get_possible_tiles_for_direction(self.entropy_grid[i-1][j], "up", self.grid[i][j])


    def get_smallest_entropy_coordinates(self):
        min_length = float('inf')
        coordinates = []

        # Iterate through the list of lists of lists
        for i, sublist1 in enumerate(self.entropy_grid):
            for j, sublist2 in enumerate(sublist1):
                # Skip empty lists
                if len(sublist2) == 0:
                    continue
                
                # Update the minimum length and coordinates
                length = len(sublist2)
                if length < min_length:
                    min_length = length
                    coordinates = [(i, j)]
                elif length == min_length:
                    coordinates.append((i, j))
        
        return random.choice(coordinates)
    
    def save_grid(self, path: str) -> None:
        height, width, channels = list(self.tile_images.values())[0].shape
        grid_image = np.zeros((height * self.dimension, width * self.dimension, channels))
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.grid[i][j].name != "NONE":
                    grid_image[i * height:(i + 1) * height, j * width:(j + 1) * width] = self.get_tile_image(self.grid[i][j])
        plt.imsave(path, grid_image)

    def grid_animation(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                tile_name = self.grid[i][j].name
                if tile_name != "NONE":
                    self.axs[i, j].imshow(self.tile_images[tile_name])
                self.axs[i, j].axis('off')
        plt.subplots_adjust(wspace=0, hspace=0)

    @staticmethod
    def initiate_tile_images(tile_list: list[Tile]) -> dict[str, np.ndarray]:
        """
        For the tile list set tile images as np arrays from the tile path.
        Rotate the images as needed.
        """
        tile_images = {}
        for tile in tile_list:
            if tile.tile_path is not None:
                tile_images[tile.name] = np.rot90(plt.imread(tile.tile_path), tile.rotation)
        return tile_images