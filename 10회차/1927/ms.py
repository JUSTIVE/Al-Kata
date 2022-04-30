import sys
import heapq

sys.setrecursionlimit(1000000)
heap = []


def solution(t):
    if(t == 0):
        return None
    else:
        value = int(sys.stdin.readline())
        if value != 0:
            heapq.heappush(heap, value)
        else:
            try:
                print(heapq.heappop(heap))
            except:
                print(0)
        return solution(t-1)


solution(int(sys.stdin.readline()))
