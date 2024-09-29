from __future__ import annotations

from directions import Direction


class Tile:
    def __init__(
        self,
        name: str = "NONE",
        sockets: dict = {},
        tile_path: str | None = None,
        rotation=0,
    ):
        self.name = name
        self.sockets = sockets
        self.collapsed = False
        self.tile_path = tile_path
        self.rotation = rotation

    def get_sockets(self):
        return self.sockets

    def possible_connections(self, tile: Tile):
        """
        Check the possible connections of tile sockets for directions.
        """
        connections = {
            Direction.UP: False,
            Direction.RIGHT: False,
            Direction.DOWN: False,
            Direction.LEFT: False,
        }
        if self.sockets[Direction.UP] == tile.get_sockets()[Direction.DOWN]:
            connections[Direction.UP] = True
        if self.sockets[Direction.DOWN] == tile.get_sockets()[Direction.UP]:
            connections[Direction.DOWN] = True
        if self.sockets[Direction.RIGHT] == tile.get_sockets()[Direction.LEFT]:
            connections[Direction.RIGHT] = True
        if self.sockets[Direction.LEFT] == tile.get_sockets()[Direction.RIGHT]:
            connections[Direction.LEFT] = True
        return connections

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_collapsed(self):
        return self.collapsed
