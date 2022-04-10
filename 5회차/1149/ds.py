import sys
from typing import List

sys.setrecursionlimit(10000)

N = int(sys.stdin.readline().split()[0])
numbers = list(map(lambda x: sys.stdin.readline().split(), range(N)))

def convert2int(strlist:List[str]) -> List[int]:
    return list(map(int, strlist))

numbers = list(map(convert2int, numbers))
ValueList = {
    0: numbers[0]
}

def calValue(index: int) -> List[int]:
    try:
        result = ValueList[index]
    except KeyError:
        result = [
            min(numbers[index][0]+calValue(index-1)[1], numbers[index][0]+calValue(index-1)[2]),
            min(numbers[index][1]+calValue(index-1)[0], numbers[index][1]+calValue(index-1)[2]),
            min(numbers[index][2]+calValue(index-1)[0], numbers[index][2]+calValue(index-1)[1])
            ]
        ValueList[index] = result
    return result

print(min(calValue(N-1)))