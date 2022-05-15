import sys

from numpy import square

def solve():
    n = int(sys.stdin.readline())
    square = list(map(lambda x: list(map(int, sys.stdin.readline().split())), range(n)))

    num_route = list(map(lambda x: [0 for i in range(n)], range(n)))

    num_route[square[0][0]][0] = 1
    num_route[0][square[0][0]] = 1
    # num_route[0][0] = 0

    def is_reachable(line:int, index: int, line_b: int, index_b: int) -> bool:

        if index-index_b == square[line_b][index_b] or line-line_b == square[line_b][index_b]:
            return True
        else:
            return False
    
    def get_num_reachable(line:int, index: int, line_b:int, index_b:int):
        if is_reachable(line, index, line_b, index_b):
            return get_num(line_b, index_b)
        else:
            return 0

    def get_num(line: int, index: int) -> int:
        if line == 0 and index == 0:
            return 0
        
        if num_route[line][index] == 0:
            num_route[line][index] = (
                sum(list(map(lambda line_b: get_num_reachable(line,index,line_b,index), range(line))))+
                sum(list(map(lambda index_b: get_num_reachable(line,index,line,index_b), range(index))))
            )
        return num_route[line][index]
    print(get_num(n-1,n-1))

if __name__ == '__main__':
    solve()