"""
--- Day 13: Shuttle Search ---
Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you
    discover that no ships embark from that port to your vacation island. You'll need to get from the port to the
    nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number
    that also indicates how often the bus leaves for the airport.

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in
    the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the
    airport, then various other locations, and finally returns to the sea port to repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at
    timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when
    the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could
    depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries
    that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be
    exactly one such bus.)

For example, suppose you have the following notes:

939
7,13,x,x,59,x,31,19
Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19. Near
    timestamp 939, these bus IDs depart at the times marked D:

time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .
The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need to wait
944 - 939 = 5 minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives 295.

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait
for that bus?
"""
import math


def IDTimesWaitTime(lines):
    minimumWait = -1
    busID = -1
    departureTime = int(lines[0])
    busses = lines[1].split(",")
    for bus in busses:
        # print(bus)
        if bus == "x":
            continue
        newBusID = int(bus)
        waitTime = (newBusID - departureTime % newBusID) % newBusID
        if minimumWait == -1 or minimumWait > waitTime:
            minimumWait = waitTime
            busID = newBusID

    print(busID, minimumWait)
    return busID * minimumWait


def partB(lines):
    busses = lines[1].split(",")
    busAndArrivalTarget = []
    maxTime = 0
    waitForMaxTime = 0
    for i in range(0, len(busses)):
        if busses[i] != "x":
            busses[i] = int(busses[i])
            if maxTime < busses[i]:
                maxTime = max(maxTime, busses[i])
                waitForMaxTime = i
            busAndArrivalTarget.append([busses[i], i])

    print(waitForMaxTime)
    for bus in busAndArrivalTarget:
        bus[1] -= waitForMaxTime
        print(bus[0], bus[1])

    print(doesTimeWork(busAndArrivalTarget, 1068781 + waitForMaxTime))

    timeIncrement = maxTime
    counter = maxTime
    print(busAndArrivalTarget)
    while 1:
        # print(counter)
        if doesTimeWork(busAndArrivalTarget, counter):
            return counter - waitForMaxTime
        counter += timeIncrement


def doesTimeWork(busAndArrivalOffset, counter):
    for bus in busAndArrivalOffset:
        if not busArrivesAt(counter + bus[1], bus[0]):
            # print(counter, bus[1], bus[0], (counter + bus[1]) % bus[0])
            return False
    return True


def busArrivesAt(time, frequency):
    return (time % frequency) == 0


def findArrivalAfterTime(time, frequency):
    return (frequency - time % frequency) % frequency


def findFirstOccurrence(a, b, offset):
    fa = 1
    fb = 1
    while 1:
        if (b * fb) - (a * fa) == offset:
            return a * fa
        if a * fa < b * fb:
            fa += 1
        else:
            fb += 1


def findLCM(a, b):
    c = a
    if b > a:
        c = a

    counter = c
    while counter % a != 0 or counter % b != 0:
        counter += c
    return counter


def getLinesFromFile(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
        return lines


if __name__ == '__main__':
    lines = getLinesFromFile("InputFiles\input_Day13.txt")
    print(IDTimesWaitTime(lines))
    # Answer is 261
    lines = getLinesFromFile("InputFiles\practice_Day13.txt")
    # lines = getLinesFromFile("InputFiles\input_Day13.txt")
    print(partB(lines))

    # print(findFirstOccurrence(7, 13, 1))
    #
    # a = [100, 200, 150]  # will work for an int array of any length
    # lcm = a[0]
    # for i in a[1:]:
    #     lcm = lcm * i // math.gcd(lcm, i)
    # print(lcm)
