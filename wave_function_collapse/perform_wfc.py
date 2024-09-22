from __future__ import annotations
import os
from grid import Grid
from tile import Tile

from tile_sockets import (
    blank_sockets,
    up_sockets,
    deadend_sockets,
    cross_sockets,
    straight_sockets,
    curve_sockets,
)
# TODO rotations of unique images
# https://github.com/mxgmn/WaveFunctionCollapse?tab=readme-ov-file


# TILES
path_to_tiles = "tiles/roads"
BLANK = Tile(
    name="BLANK",
    sockets=blank_sockets,
    tile_path=os.path.join(path_to_tiles, "blank.png"),
)
TRI = Tile(
    name="TRI", sockets=up_sockets, tile_path=os.path.join(path_to_tiles, "up.png")
)
STRAIGHT = Tile(
    name="STRAIGHT",
    sockets=straight_sockets,
    tile_path=os.path.join(path_to_tiles, "straight.png"),
)
CURVE = Tile(
    name="CURVE",
    sockets=curve_sockets,
    tile_path=os.path.join(path_to_tiles, "curve.png"),
)

CROSS = Tile(
    name="CROSS",
    sockets=cross_sockets,
    tile_path=os.path.join(path_to_tiles, "cross.png"),
)

DEADEND = Tile(
    name="DEADEND",
    sockets=deadend_sockets,
    tile_path=os.path.join(path_to_tiles, "deadend.png"),
)



# GRID
grid = Grid(dimension=8, tile_list=[BLANK, TRI, STRAIGHT, CURVE, CROSS])
print(grid.tile_list)
grid.initiate_collapse(grid.tile_list[2], animate=False)
grid.save_grid(path="grids/test.png")
