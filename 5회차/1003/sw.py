def memorization():
    zero = [1, 0, 1]
    one = [0, 1, 1]
    for i in range(3, 41):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i-2]+one[i-1])
    return zero, one

N = int(input())
zero, one = memorization()

def fibonacci(idx:int):
    print('{} {}'.format(zero[idx], one[idx]))
    
for _ in range(N):
    fibonacci(int(input()))


# %%
