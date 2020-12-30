"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to
    take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety,
    it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you
    quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
    input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship
    is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the
    following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position
    and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's
    starting position?

Your puzzle answer was 590.

--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back
    of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is,
    if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100,
    north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170,
    north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship.
    The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214,
    south 72. The waypoint stays 4 units east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the
    ship's starting position?

Your puzzle answer was 42013.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

FACING_NORTH = 0
FACING_EAST = 1
FACING_SOUTH = 2
FACING_WEST = 3
NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"


def moveShip(lines):
    print("check")
    facing = FACING_EAST
    currentX = 0
    currentY = 0
    for line in lines:
        command = line[0]
        value = int(line[1:])

        if command == NORTH:
            currentY += value
        if command == EAST:
            currentX += value
        if command == SOUTH:
            currentY -= value
        if command == WEST:
            currentX -= value
        if command in ["L", "R"]:
            facing = rotateDirection(facing, command, value)
        if command == "F":
            if facing == FACING_NORTH:
                currentY += value
            if facing == FACING_EAST:
                currentX += value
            if facing == FACING_SOUTH:
                currentY -= value
            if facing == FACING_WEST:
                currentX -= value

    print(currentY, currentX)
    return abs(currentY) + abs(currentX)


def rotateDirection(currentFacing, direction, degrees):
    shifts = int(degrees / 90)
    for i in range(0, shifts):
        if direction == "L":
            currentFacing -= 1
            if currentFacing < 0:
                currentFacing += 4
        if direction == "R":
            currentFacing = (currentFacing + 1) % 4
    return currentFacing


def moveShipToWaypoint(lines):
    print("check")
    currentX = 0
    currentY = 0
    waypointX = 10
    waypointY = 1
    for line in lines:
        # print("Position: ", currentX, currentY)
        # print("Waypoint: ", waypointX, waypointY)
        # print("-")
        command = line[0]
        value = int(line[1:])

        if command == NORTH:
            waypointY += value
        if command == EAST:
            waypointX += value
        if command == SOUTH:
            waypointY -= value
        if command == WEST:
            waypointX -= value
        if command in ["L", "R"]:
            waypointX, waypointY = rotateWaypoint(waypointX, waypointY, command, value)
        if command == "F":
            currentX += value * waypointX
            currentY += value * waypointY

    print(currentX, currentY)
    return abs(currentY) + abs(currentX)


def rotateWaypoint(waypointX, waypointY, command, value):
    shifts = int(value/90)
    for i in range(0, shifts):
        if command == "L":
            if waypointY * waypointX > 0:
                temp = waypointY
                waypointY = waypointX
                waypointX = temp * -1
            else:
                temp = waypointX
                waypointX = waypointY * -1
                waypointY = temp
        if command == "R":
            if waypointY * waypointX > 0:
                temp = waypointY
                waypointY = waypointX * -1
                waypointX = temp * 1
            else:
                temp = waypointY
                waypointY = waypointX * -1
                waypointX = temp
    return waypointX, waypointY


def getLinesFromFile(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
        return lines


if __name__ == '__main__':
    lines = getLinesFromFile("InputFiles\input_Day12.txt")
    print(moveShip(lines))
    # Answer is 590
    lines = getLinesFromFile("InputFiles\practice_Day12.txt")
    print(moveShipToWaypoint(lines))
    # Correctly gets 286
    lines = getLinesFromFile("InputFiles\input_Day12.txt")
    print(moveShipToWaypoint(lines))
    # Answer is 42013