from directions import Direction

blank_sockets = {
    Direction.UP: "000",
    Direction.LEFT: "000",
    Direction.DOWN: "000",
    Direction.RIGHT: "000",
}


big_curve_sockets = {
    Direction.UP: "100",
    Direction.LEFT: "000",
    Direction.DOWN: "000",
    Direction.RIGHT: "001",
}

cross_sockets = {
    Direction.UP: "010",
    Direction.LEFT: "010",
    Direction.DOWN: "010",
    Direction.RIGHT: "010",
}

side_straight_sockets = {
    Direction.UP: "100",
    Direction.LEFT: "000",
    Direction.DOWN: "001",
    Direction.RIGHT: "000",
}

right_sockets = {
    Direction.UP: "010",
    Direction.LEFT: "000",
    Direction.DOWN: "010",
    Direction.RIGHT: "010",
}

middle_straight_sockets = {
    Direction.UP: "010",
    Direction.LEFT: "000",
    Direction.DOWN: "010",
    Direction.RIGHT: "000",
}

small_curve_sockets = {
    Direction.UP: "010",
    Direction.LEFT: "000",
    Direction.DOWN: "000",
    Direction.RIGHT: "010",
}
