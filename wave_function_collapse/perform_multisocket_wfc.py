from __future__ import annotations

import os

from grid import Grid
from tile import Tile
from tile_multisockets import (
    big_curve_sockets,
    blank_sockets,
    cross_sockets,
    middle_straight_sockets,
    right_sockets,
    side_straight_sockets,
    small_curve_sockets,
)

# https://github.com/mxgmn/WaveFunctionCollapse?tab=readme-ov-file


# TILES
path_to_tiles = "tiles/rail"
BLANK = Tile(
    name="BLANK",
    sockets=blank_sockets,
    tile_path=os.path.join(path_to_tiles, "blank.png"),
)
TRI = Tile(
    name="TRI",
    sockets=right_sockets,
    tile_path=os.path.join(path_to_tiles, "right.png"),
)

MIDDLE_STRAIGHT = Tile(
    name="MIDDLE_STRAIGHT",
    sockets=middle_straight_sockets,
    tile_path=os.path.join(path_to_tiles, "middle_straight.png"),
)

SMALL_CURVE = Tile(
    name="SMALL_CURVE",
    sockets=small_curve_sockets,
    tile_path=os.path.join(path_to_tiles, "small_curve.png"),
)

CROSS = Tile(
    name="CROSS",
    sockets=cross_sockets,
    tile_path=os.path.join(path_to_tiles, "cross.png"),
)

SIDE_STRAIGHT = Tile(
    name="SIDE_STRAIGHT",
    sockets=side_straight_sockets,
    tile_path=os.path.join(path_to_tiles, "side_straight.png"),
)

BIG_CURVE = Tile(
    name="BIG_CURVE",
    sockets=big_curve_sockets,
    tile_path=os.path.join(path_to_tiles, "big_curve.png"),
)


# GRID
grid = Grid(dimension=6, tile_list=[BLANK, TRI, MIDDLE_STRAIGHT, CROSS, SIDE_STRAIGHT, SMALL_CURVE])
print(grid.tile_list)
grid.initiate_collapse(grid.tile_list[2], animate=True)
grid.save_grid(path="grids/test.png")
