import sys
from typing import Dict, List

N = int(sys.stdin.readline().split()[0])
numbers = list(map(lambda x: sys.stdin.readline().split()[0], range(N)))
numbers = list(map(int,numbers))
MemoFibo = {
    0:[1,0],
    1:[0,1]
    }

def fibonacci(n: int) -> Dict[int, List[int]]:
    try:
        result = MemoFibo[n]
    except KeyError:
        result = [fibonacci(n-1)[i] + fibonacci(n-2)[i] for i in range(2)]
        MemoFibo[n] = result
    return result

fibonacci(max(numbers))

[print(MemoFibo[i][0], MemoFibo[i][1]) for i in numbers]