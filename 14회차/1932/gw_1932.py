import sys

height = int(sys.stdin.readline())

def sol(ex_list: list, curr_list: list):
    for i in range(len(curr_list)):
        if i == 0:
            curr_list[i] = ex_list[i] + curr_list[i]
        elif i == len(curr_list) - 1:
            curr_list[i] = ex_list[i-1] + curr_list[i]
        else:
            curr_list[i] = max((ex_list[i-1] + curr_list[i]), (ex_list[i] + curr_list[i]))
    return curr_list

for n in range(height):
    if n == 0:
        ex_list = list(map(int,sys.stdin.readline().split(" ")))
    else:
        input_list = list(map(int,sys.stdin.readline().split(" ")))
        ex_list = sol(ex_list, input_list)

print(max(ex_list))