from __future__ import annotations
import os

import matplotlib.pyplot as plt
import numpy as np
import random

from setup_tiles import blank_links, up_links, right_links, down_links, left_links
# TODO rotations of unique images

class Tile:
    def __init__(self, name: str = "NONE", links: dict = {}):
        self.name = name
        self.links = links
        self.collapsed = False
    
    def get_links(self):
        return self.links

    def possible_connections(self, tile: Tile):
        connections = {"up": False, "right": False, "down": False, "left": False}
        if self.links["up"] == tile.get_links()["down"]:
            connections["up"] = True
        if self.links["down"] == tile.get_links()["up"]:
            connections["down"] = True
        if self.links["right"] == tile.get_links()["left"]:
            connections["right"] = True
        if self.links["left"] == tile.get_links()["right"]:
            connections["left"] = True
        return connections
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_collapsed(self):
        return self.collapsed

    def set_tile(self, tile: Tile):
        self.tile = tile


class Grid:
    def __init__(self, dimension, tile_list: list[Tile], path: str):
        self.tile_list = tile_list # all possible tiles
        self.dimension = dimension
        self.grid = [[Tile() for _ in range(dimension)] for _ in range(dimension)]
        self.tile_images = self.initiate_tile_images(path=path)
        self.entropy_grid = [[tile_list for _ in range(dimension)] for _ in range(dimension)]
        _, self.axs = plt.subplots(self.dimension, self.dimension, figsize=(2 * self.dimension, 2 * self.dimension))

    def get_grid(self):
        return self.grid
    
    def get_tile_image(self, tile: Tile):
        return self.tile_images[tile.name.lower()]
    
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
            self.grid[x][y] = random.choice(self.entropy_grid[x][y]) # grid cell gets a random entropy grid assigned
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
                if self.entropy_grid[i][j] == []:
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
                if self.grid[i][j].name.lower() != "none":
                    grid_image[i * height:(i + 1) * height, j * width:(j + 1) * width] = self.get_tile_image(self.grid[i][j])
        plt.imsave(path, grid_image)

    def grid_animation(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                tile_name = self.grid[i][j].name.lower()
                if tile_name != "none":
                    self.axs[i, j].imshow(self.tile_images[tile_name])
                self.axs[i, j].axis('off')
        plt.subplots_adjust(wspace=0, hspace=0)

    @staticmethod
    def initiate_tile_images(path) -> dict[str, np.ndarray]:
        tiles_images = {}
        filenames = os.listdir(path=path)
        for filename in filenames:
            tiles_images[filename[:-4]] = plt.imread(os.path.join(path, filename))
        return tiles_images

# TILES
BLANK = Tile(name="BLANK", links=blank_links)
UP = Tile(name="UP", links=up_links)
RIGHT = Tile(name="RIGHT", links=right_links)
DOWN = Tile(name="DOWN", links=down_links)
LEFT = Tile(name="LEFT", links=left_links)

# GRID
grid = Grid(dimension=4, tile_list=[UP, RIGHT, DOWN, LEFT], path="tiles/roads")
grid.initiate_collapse(LEFT, animate=True)
#grid.save_grid(path="grids/roads_grid.png")