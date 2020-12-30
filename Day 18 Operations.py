"""--- Day 18: Operation Order --- As you look out the window and notice a heavily-forested continent slowly appear
over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with
their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (
*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated
before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the
operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition,
the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6 3   * 3 + 4 * 5 + 6 9   + 4 * 5 + 6 13   * 5 + 6 65   + 6 71 Parentheses can override this
order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26. 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437. 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
becomes 12240. ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632. Before you can help with the homework,
you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the
resulting values?

Your puzzle answer was 12956356593940.

--- Part Two --- You manage to answer the child's questions and they finish part 1 of their homework, but get stuck
when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?

Your puzzle answer was 94240043727614.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

ADD_SUBTRACT_PRIORITY = 2
MULTIPLY_DIVIDE_PRIORITY = 1


def getSumOfAllLines(lines, withPrecedence):
    return sum([evaluate(line, withPrecedence) for line in lines])


def evaluate(line, withPrecedence):
    postFix = toPostfix(line, withPrecedence)
    # print(postFix)
    evaluated = evaluatePostFix(postFix)
    # print(evaluated)
    return evaluated


def toPostfix(infix, withPrecedence):
    stack = []
    postfix = ''

    for c in infix:
        if c == " ":
            continue
        if c not in ["+", "-", "/", "*", "(", ")"]:
            postfix += c
        elif c == "(":
            stack.append("(")
        elif c == ")":
            while len(stack) > 0 and stack[-1] != "(":
                postfix += stack[-1]
                stack.pop(-1)
            stack.pop(-1)
        elif c in ["+", "-", "*", "/"]:
            while len(stack) > 0 and stack[-1] != "(" and \
                    (getPrecedence(c) <= getPrecedence(stack[-1]) or not withPrecedence):
                postfix += stack.pop(-1)
            stack.append(c)

    while len(stack) > 0:
        postfix += stack[-1]
        stack.pop(-1)
    return postfix


def evaluatePostFix(postfix):
    result = 0
    evaluateStack = []
    for i in range(0, len(postfix)):
        char = postfix[i]
        if char not in ["+", "-", "*", "/"]:
            evaluateStack.append(int(char))
        else:
            o1 = evaluateStack.pop(-1)
            o2 = evaluateStack.pop(-1)
            if char == "+":
                result = o1 + o2
            if char == "-":
                result = o1 - o2
            if char == "*":
                result = o1 * o2
            if char == "/":
                result = o1 / o2
            evaluateStack.append(result)

    return result


def getPrecedence(char):
    if char in ["+", "-"]:
        return ADD_SUBTRACT_PRIORITY
    # if char in ["*", "/"]: # To add more operations later
    else:
        return MULTIPLY_DIVIDE_PRIORITY


def getLinesFromFile(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
        return lines


if __name__ == '__main__':
    lines = getLinesFromFile("InputFiles\input_Day18.txt")

    print(getSumOfAllLines(lines, False))
    # Answer is 12956356593940
    print(getSumOfAllLines(lines, True))
    # Answer is 94240043727614
