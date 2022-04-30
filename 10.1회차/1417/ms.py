import sys

t = int(sys.stdin.readline())
ds = int(sys.stdin.readline())


def candidates(s, c):
    if c == 0:
        return sorted(s, reverse=True)
    else:
        s.append(int(sys.stdin.readline()))
        return candidates(s, c-1)


def solution(ds, s, c):
    if ds > c[0]:
        return s
    else:
        c[0] = c[0] - 1
        return solution(ds+1, s+1, sorted(c, reverse=True))


match t:
    case 0:
        print(0)

if(t == 1):
    print(0)
else:
    print(solution(ds, 0, candidates([], t-1)))
