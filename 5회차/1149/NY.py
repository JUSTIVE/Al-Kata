import re
import sys

n = int(sys.stdin.readline().rstrip())
m = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
rgb_array=[[0]*3 for _ in range(n)]
rgb_array[0][0], rgb_array[0][1], rgb_array[0][2] = m[0][0], m[0][1], m[0][2]

def rgb(i, m, n, rgb_array):
    
    if n == 1:
        return min(m[0][0], m[0][1], m[0][2])
    elif i == n-1:
        rgb_array[i][0] = min(rgb_array[i-1][1], rgb_array[i-1][2]) + m[i][0]
        rgb_array[i][1] = min(rgb_array[i-1][2], rgb_array[i-1][0]) + m[i][1]
        rgb_array[i][2] = min(rgb_array[i-1][1], rgb_array[i-1][0]) + m[i][2]
        return min(rgb_array[i][0], rgb_array[i][1], rgb_array[i][2]) 
    else:
        rgb_array[i][0] = min(rgb_array[i-1][1], rgb_array[i-1][2]) + m[i][0]
        rgb_array[i][1] = min(rgb_array[i-1][2], rgb_array[i-1][0]) + m[i][1]
        rgb_array[i][2] = min(rgb_array[i-1][1], rgb_array[i-1][0]) + m[i][2]
        return rgb(i+1, m, n, rgb_array)

if __name__=='__main__':
    result=rgb(1,m,n,rgb_array)
    print(result)

# rgb_list=[]
# for i in range(n):
#     m = list(map(int,sys.stdin.readline().split()))
#     rgb_list.append(m)

# def RGB(m):
#     =list(sys.stdin.readline().rstrip())
#     for i in range(1,n):



# if __name__=='__main__':
    
#     m = sys.stdin.readline().rstrip()
#     RGB()
#     # n= re.split('(?=[A-Z])',m)
#     # result=find_nope(n,0,0)
    
#     print(result)