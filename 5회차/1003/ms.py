from typing import List, Tuple
import sys


def preCalculate(zeros, ones, iterator) -> tuple[list[int], list[int]]:
    if(iterator == 0):
        return (zeros, ones)
    else:
        zeros.append(zeros[-1] + zeros[-2])
        ones.append(ones[-1] + ones[-2])
        return preCalculate(zeros, ones, iterator - 1)


memo = preCalculate([1, 0, 1], [0, 1, 1], 40)
# precalculation done


def handle(value: int) -> tuple[int, int]:
    return list(map(lambda x: x[value], memo))


def printFibCall(value: tuple[int, int]):
    print(f'{value[0]} {value[1]}')


def solve(value: int) -> int:
    if(value == 0):
        return
    else:
        printFibCall(handle(int(sys.stdin.readline())))
        solve(value-1)


solve(int(sys.stdin.readline()))
