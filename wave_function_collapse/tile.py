from __future__ import annotations

class Tile:
    def __init__(self, name: str = "NONE", sockets: dict = {}, tile_path: str | None = None, rotation = 0):
        self.name = name
        self.sockets = sockets
        self.collapsed = False
        self.tile_path = tile_path
        self.rotation = rotation
    
    def get_sockets(self):
        return self.sockets

    def possible_connections(self, tile: Tile):
        connections = {"up": False, "right": False, "down": False, "left": False}
        if self.sockets["up"] == tile.get_sockets()["down"]:
            connections["up"] = True
        if self.sockets["down"] == tile.get_sockets()["up"]:
            connections["down"] = True
        if self.sockets["right"] == tile.get_sockets()["left"]:
            connections["right"] = True
        if self.sockets["left"] == tile.get_sockets()["right"]:
            connections["left"] = True
        return connections
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_collapsed(self):
        return self.collapsed
