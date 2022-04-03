import sys

# counting sort


def solve():
    dataLen = int(sys.stdin.readline())
    bucket = [0]*10001
    for i in range(dataLen):
        bucket[int(sys.stdin.readline())] += 1

    for i in range(10001):
        for j in range(bucket[i]):
            print(i)


solve()
