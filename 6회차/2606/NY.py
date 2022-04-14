import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
stack = [graph[0]]

def virus(graph, m, n, j, stack):
    
    stack.append(graph[j])
    stack_= sum(stack,[])
    if len(stack_) != len(list(set(stack_))):
        virus(graph, m, n, j+1, [list(set(stack_))])
    else:
        return print(len(stack[0])-1)
    
    

if __name__=='__main__':
    
    result=virus(graph, m, n, 1, stack)
    print(result)

    

