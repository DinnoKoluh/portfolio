from directions import Direction

blank_sockets = {
    Direction.UP: "0",
    Direction.LEFT: "0",
    Direction.DOWN: "0",
    Direction.RIGHT: "0",
}

up_sockets = {
    Direction.UP: "1",
    Direction.LEFT: "1",
    Direction.DOWN: "0",
    Direction.RIGHT: "1",
}

right_sockets = {
    Direction.UP: "1",
    Direction.LEFT: "0",
    Direction.DOWN: "1",
    Direction.RIGHT: "1",
}

down_sockets = {
    Direction.UP: "0",
    Direction.LEFT: "1",
    Direction.DOWN: "1",
    Direction.RIGHT: "1",
}

left_sockets = {
    Direction.UP: "1",
    Direction.LEFT: "1",
    Direction.DOWN: "1",
    Direction.RIGHT: "0",
}

straight_sockets = {
    Direction.UP: "1",
    Direction.LEFT: "0",
    Direction.DOWN: "1",
    Direction.RIGHT: "0",
}

curve_sockets = {
    Direction.UP: "0",
    Direction.LEFT: "0",
    Direction.DOWN: "1",
    Direction.RIGHT: "1",
}

cross_sockets = {
    Direction.UP: "1",
    Direction.LEFT: "1",
    Direction.DOWN: "1",
    Direction.RIGHT: "1",
}

deadend_sockets = {
    Direction.UP: "0",
    Direction.LEFT: "0",
    Direction.DOWN: "1",
    Direction.RIGHT: "0",
}
