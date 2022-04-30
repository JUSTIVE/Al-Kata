import sys

value = int(sys.stdin.readline())

def solution(s, t):
    if t in s:
        return s[t]
    else:
        cnt = 1 + min(solution(s,t//3) + t % 3, solution(s,t//2) + t % 2)
        s[t] = cnt
        return cnt

print(solution({1:0,2:1},value))