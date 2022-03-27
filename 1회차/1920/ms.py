import sys
dataLen = int(sys.stdin.readline())
rawData = sorted(list(map(int, sys.stdin.readline().split(" "))))
searchTargetLength = int(sys.stdin.readline())
searchTargets = list(map(int, sys.stdin.readline().split(" ")))


def binarySearch(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        print("low", data[low], "high", data[high], "mid", data[mid])
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


searchResult = list(
    map(lambda x: 1 if binarySearch(rawData, x) != -1 else 0, searchTargets))
for x in searchResult:
    print(x)
