import sys

def solve():
    n = int(sys.stdin.readline())
    triangle = list(map(lambda x: list(map(int, sys.stdin.readline().split())), range(n)))
    score = list(map(lambda x: [0 for i in range(x+1)], range(n)))
    score[0][0] = triangle[0][0]
    def get_route(line: int, index: int) -> int:
        if line < index or line < 0 or index < 0:
            return 0

        if score[line][index] == 0:
            score[line][index] = max(triangle[line][index]+get_route(line-1, index -1), triangle[line][index]+get_route(line-1, index))
        return score[line][index]
    print(max([get_route(n-1, i) for i in range(n)]))
if __name__ == '__main__':
    solve()