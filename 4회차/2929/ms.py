import re


def solve(value):
    def splitter():
        return re.findall(r'[A-Z]{1}[a-z]*', value)

    def calcRest(value):
        modDigit = len(value) % 4
        return 0 if modDigit == 0 else 4 - modDigit

    return sum(map(calcRest, splitter()[:-1]))


print(solve(input()))
