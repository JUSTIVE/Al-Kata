import sys 

def baechu(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if s[x][y]==1:
        # 해당 노드 방문처리 
        s[x][y] = 0
        #상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        baechu(x-1, y)
        baechu(x,y-1)
        baechu(x+1, y)
        baechu(x, y+1)
        return True
    return False 
    
case_number= int(sys.stdin.readline())

result_=[]
for _ in range(case_number):
    n, m, k = map(int, sys.stdin.readline().split())
    s=[[0]*n for i in range(m)]
    result=0
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        s[b][a] =1
    for i in range(m):
        for j in range(n):
            if baechu(i,j):
                result+=1
    result_.append(result)
for p in range(len(result_)):
    print(result_[p])
#     result_.append(result)
# print(result_)

