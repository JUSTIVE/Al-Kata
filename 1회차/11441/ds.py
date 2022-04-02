import sys
from typing import List
from functools import reduce

def main():
    InputLength = int(sys.stdin.readline().split()[0])
    InputList = GetNumbers(sys.stdin.readline(), InputLength)

    iteration = int(sys.stdin.readline().split()[0])
    for i in range(iteration):
        section = GetNumbers(sys.stdin.readline(), 2)
        Sum = GetSum(section, InputList)
        print(Sum)

def GetSum(section: List[int], InputList:List[int]) -> int:
    # return sum(InputList[section[0]-1:section[1]])
    return reduce(lambda x, y: x+y, InputList[section[0]-1:section[1]])

def GetNumbers(Input: str, InputLength: int) -> List[int]:
    return list(map(int, Input.split()))[0:InputLength]

if __name__ == '__main__':
    main()