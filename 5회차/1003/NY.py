import re
import sys


def fibo_memo(x):
    if x == 0:
        memo[x] = [1,0]
        return memo[x]
    elif x == 1:
        memo[x] = [0,1]
        return memo[x]
    elif x in memo:
        return memo[x]
    else:
        a = fibo_memo(x-1)[0] + fibo_memo(x-2)[0]
        b = fibo_memo(x-1)[1] + fibo_memo(x-2)[1]
        memo[x] = [a,b]
        return memo[x]



t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    memo = {}
    f = fibo(n)
    print(f[0],f[1])
    # m[0]=0
    # m[1]=1

    # for i in range(n):
    #     number = sys.stdin.readline().rstrip()
    
    
    # return m[i-1]+m[i-2]
