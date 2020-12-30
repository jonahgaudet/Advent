"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2211.

--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 1995.

Both parts of this puzzle are complete! They provide two gold stars: **
"""


def partA(lines):
    equal = -1
    while equal == -1:
        oldLines = lines.copy()
        equal = runCycle(lines, oldLines)
    return equal


def printLines(lines):
    for line in lines:
        print(line)
    print()
    print()


def partB(lines):
    equal = -1
    while equal == -1:
        oldLines = lines.copy()
        equal = runCycleB(lines, oldLines)
    return equal


def runCycle(lines, oldLines):
    for y in range(0, len(oldLines)):
        for x in range(0, len(oldLines[y])):
            if oldLines[y][x] == "L" and getAmountAdjacent(oldLines, y, x, "#") == 0:
                lines[y] = lines[y][:x] + "#" + lines[y][x+1:]
            if oldLines[y][x] == "#" and getAmountAdjacent(oldLines, y, x, "#") >= 4:
                lines[y] = lines[y][:x] + "L" + lines[y][x+1:]
    if checkEquality(lines, oldLines):
        return countOccupiedSeats(lines)
    return -1


def runCycleB(lines, oldLines):
    for y in range(0, len(oldLines)):
        for x in range(0, len(oldLines[y])):
            if oldLines[y][x] == "L" and amountViewable(oldLines, y, x, "#") == 0:
                lines[y] = lines[y][:x] + "#" + lines[y][x+1:]
            if oldLines[y][x] == "#" and amountViewable(oldLines, y, x, "#") >= 5:
                lines[y] = lines[y][:x] + "L" + lines[y][x+1:]
    if checkEquality(lines, oldLines):
        return countOccupiedSeats(lines)
    return -1


def getAmountAdjacent(oldLines, yValue, xValue, seachingFor):
    counter = 0
    for y in range(max(0, yValue - 1), min(len(oldLines), yValue + 2)):
        for x in range(max(0, xValue - 1), min(len(oldLines[y]), xValue + 2)):
            if oldLines[y][x] == seachingFor and (y != yValue or x != xValue):
                counter += 1
    return counter


def amountViewable(oldLines, yValue, xValue, searchingFor):
    counter = 0
    counter += characterCanBeSeen(oldLines, yValue, 1, xValue, 0, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, 1, xValue, 1, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, 1, xValue, -1, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, 0, xValue, 1, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, 0, xValue, -1, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, -1, xValue, 0, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, -1, xValue, 1, searchingFor)
    counter += characterCanBeSeen(oldLines, yValue, -1, xValue, -1, searchingFor)
    return counter


def characterCanBeSeen(oldLines, yPosition, yOffset, xPosition, xOffset, searchingFor):
    counter = 1
    while 1:
        yValue = counter * yOffset + yPosition
        xValue = counter * xOffset + xPosition
        if 0 <= yValue < len(oldLines) and 0 <= xValue < len(oldLines[0]):
            if oldLines[yValue][xValue] != ".":
                if oldLines[yValue][xValue] == searchingFor:
                    return True
                else:
                    return False
        else:
            return False
        counter += 1


def countOccupiedSeats(lines):
    counter = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == "#":
                counter += 1
    return counter


def checkEquality(lines1, lines2):
    for i in range(0, len(lines1)):
        if lines1[i] != lines2[i]:
            return False
    return True


def getLinesFromFile(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
        return lines


if __name__ == '__main__':
    lines = getLinesFromFile("InputFiles\input_Day11.txt")
    print(partA(lines))
    # Answer is 2211
    lines = getLinesFromFile("InputFiles\input_Day11.txt")
    print(partB(lines))
    # Answer is 1995