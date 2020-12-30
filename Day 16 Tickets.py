"""--- Day 16: Ticket Translation --- As you're walking to yet another connecting flight, you realize that one of the
legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a
language you don't understand. You should probably figure out what it says before you get to the train station after
the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure
out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the
same train service (via the airport security cameras) together into a single document you can reference (your puzzle
input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of
values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is
named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field,
but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in
the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------. | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        | | ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? | '--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,
302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case,
you've extracted just the numbers in such a way that the first number is always the same specific field, the second
number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid
for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets: 7,3,47 40,4,50 55,2,20 38,6,12 It doesn't matter which position corresponds to which field; you can
identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field.
In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the
other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the
invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

Your puzzle answer was 29851.

--- Part Two --- Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use
the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent
between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets: 3,9,18 15,1,5 5,14,9 Based on the nearby tickets in the above example, the first position must be
row, the second position must be class, and the third position must be seat; you can conclude that in your ticket,
class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure.
What do you get if you multiply those six values together?

Your puzzle answer was 3029180675981.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

SEARCH_FOR = 'departure'


class Rule:
    def __init__(self, ruleName, ID, r1, r2):
        self.name = ruleName
        self.ID = int(ID)
        range1 = [int(v) for v in r1.split("-")]
        self.low1 = range1[0]
        self.high1 = range1[1]
        range2 = [int(v) for v in r2.split("-")]
        self.low2 = range2[0]
        self.high2 = range2[1]
        self.orderNumber = -1
        self.possibleOrders = []

    def isValid(self, value):
        if self.low1 <= value <= self.high1 or self.low2 <= value <= self.high2:
            # print(value, "is valid for", self.getRange())
            return True
        # print(value, "is NOT valid for", self.getRange())
        return False

    def getRange(self):
        return str(self.low1) + "-" + str(self.high1) + ", " + str(self.low2) + "-" + str(self.high2)

    def getOrder(self):
        return self.orderNumber

    def setOrder(self, order):
        self.orderNumber = order

    def removePossibleOrder(self, ID):
        self.possibleOrders[ID] = False

    def getFirstPossibleOrder(self):
        for i in range(0, len(self.possibleOrders)):
            if self.possibleOrders[i]:
                return i
        return -1

    def populateOrders(self, value):
        self.possibleOrders = [True for _ in range(0, value)]


def getSumOfErrors(lines):
    rules = []
    viewingNearby = False
    sumOfInvalidValues = 0
    for line in lines:
        if "or" in line:
            name = line.split(": ")[0]
            ranges = line.split(": ")[1].split(" or ")
            range1 = ranges[0]
            range2 = ranges[1]
            rules.append(Rule(name, 0, range1, range2))

        if "nearby tickets:" in line:
            viewingNearby = True
        elif viewingNearby:
            ticketValues = [int(v) for v in line.split(",")]
            for value in ticketValues:
                if not isValueValid(value, rules):
                    sumOfInvalidValues += value

    return sumOfInvalidValues


def partB(lines):
    rules = []
    viewingMine = False
    viewingNearby = False
    validTickets = []
    counter = 0
    for line in lines:
        if "or" in line:
            name = line.split(": ")[0]
            ranges = line.split(": ")[1].split(" or ")
            range1 = ranges[0]
            range2 = ranges[1]
            rules.append(Rule(name, counter, range1, range2))
            counter += 1

        if "your ticket:" in line:
            viewingMine = True
        elif viewingMine:
            myTicket = [int(v) for v in line.split(",")]
            viewingMine = False

        if "nearby tickets:" in line:
            viewingNearby = True
        elif viewingNearby:
            ticketValues = [int(v) for v in line.split(",")]
            if isTicketValid(ticketValues, rules):
                validTickets.append(ticketValues)

    for rule in rules:
        rule.populateOrders(len(rules))

    for ticket in validTickets:
        for i in range(0, len(ticket)):
            for rule in rules:
                if not rule.isValid(ticket[i]):
                    rule.removePossibleOrder(i)

    completed = False
    while not completed:
        for rule in rules:
            if rule.possibleOrders.count(True) == 1:
                toChange = rule.getFirstPossibleOrder()
                for ruleChange in rules:
                    if rule.ID != ruleChange.ID:
                        ruleChange.removePossibleOrder(toChange)
                completed = oneOption(rules)

    # # For debugging
    # for rule in rules:
    #     print(rule.ID, rule.possibleOrders)

    product = 1
    for rule in rules:
        if SEARCH_FOR in rule.name:
            value = rule.getFirstPossibleOrder()
            product *= myTicket[value]
            # print(myTicket[value])
    return product


def oneOption(rules):
    for rule in rules:
        if rule.possibleOrders.count(True) > 1:
            return False
    return True


def isTicketValid(ticketValues, rules):
    for value in ticketValues:
        if not isValueValid(value, rules):
            return False
    return True


def isValueValid(value, rules):
    for rule in rules:
        if rule.isValid(value):
            return True
    return False


def getLinesFromFile(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
        return lines


if __name__ == '__main__':
    # lines = getLinesFromFile("InputFiles\practice_Day16.txt")
    lines = getLinesFromFile("InputFiles\input_Day16.txt")
    print(getSumOfErrors(lines))
    # Answer is 29851
    print(partB(lines))
    # Answer is 3029180675981
