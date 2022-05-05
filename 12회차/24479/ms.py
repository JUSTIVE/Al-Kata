import sys

V, E, R = map(int, sys.stdin.readline().split())

def solution(V, E, R):
    stack = [R]
    graph = [[] for _ in range(V+1)]
    visitedN = [0 for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    cnt = 1
    
    for i in range(E):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    for i in graph:
        i.sort(reverse=True)

    while len(stack) != 0:
        node = stack.pop()
        if(not visited[node]):
            visited[node] = True
            for i in  graph[node]:
                stack.append(i)
            visitedN[node] = cnt
            cnt += 1

    for x in visitedN[1:]:
        print(x)

solution(V, E, R)
