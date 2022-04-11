import sys
from typing import List, Tuple

sys.setrecursionlimit(1001)


def solve():
    houses = int(input())

    def getHouseData(state: list[tuple[int, int, int]], index: int) -> list[tuple[int, int, int]]:
        if(index == 0):
            return state
        else:
            state.append(list(map(int, sys.stdin.readline().split(' '))))
            return getHouseData(state, index-1)

    RGB = getHouseData([], houses)

    for i in range(1, houses):
        RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2])+RGB[i][0]
        RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2])+RGB[i][1]
        RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1])+RGB[i][2]

    print(min(RGB[houses-1]))


solve()
