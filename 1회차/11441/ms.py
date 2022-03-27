import sys
dataLen = int(sys.stdin.readline())

rawData = list(map(int, sys.stdin.readline().split(" ")))
data = [0, rawData[0]]
for i in range(1, len(rawData)):
    data.append(data[i]+rawData[i])

testLength = int(sys.stdin.readline())

for i in range(testLength):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(data[b]-data[a-1])
