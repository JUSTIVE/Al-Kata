import sys
from typing import Dict

sys.setrecursionlimit(1000000)

def main():
    memo: Dict[int:int] = {
        1:0,
        2:1,
        3:1
    }

    def solve(N: int):
        N = int(N)
        if not N in memo:
            memo[N] = min(solve(N//2) + N%2, solve(N//3) + N%3) + 1

        
        # if not N in memo:
        #     if N%2 and N%3: # 2, 3 둘다 나누어 떨어지지 않음
        #         memo[N] = solve(N-1) + 1
        #     else:
        #         if not(N%2 or N%3):
        #             memo[N] = min(solve(N/2), solve(N/3), solve(N-1)) + 1
        #         elif not N%2:
        #             memo[N] = min(solve(N-1), solve(N/2)) + 1
        #         elif not N%3:
        #             memo[N] = min(solve(N-1), solve(N/3)) + 1

        # if not N in memo:
        #     if N%2 and N%3: # 2, 3 둘다 나누어 떨어지지 않음
        #         memo[N] = solve(N-1) + 1
        #     else:
        #         if not(N%2 or N%3):
        #             memo[N] = min(solve(N/2), solve(N/3)) + 1
        #              # 2,3 둘다 나누어 떨어짐
        #         elif not N%2:
        #             memo[N] = solve(N/2) + 1
        #         elif not N%3:
        #             memo[N] = solve(N/3) + 1
        return memo[N]
    
    N = int(sys.stdin.readline())
    print(solve(N))


if __name__ == '__main__':
    main()