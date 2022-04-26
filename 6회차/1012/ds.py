import sys
from typing import List

def main():
    T = int(sys.stdin.readline().split()[0])
    
    for i in range(T):
        solve()

def solve():
    M, N, K = list(map(int, sys.stdin.readline().split()))
    def split_list():
        return list(map(int, sys.stdin.readline().split()))
    coord_list = list(map(lambda x: split_list(), range(K)))
    worm = 0

    def baechu_exsist(coord_list, coord):
        return True if coord in coord_list else False

    def make_searching_list(coord) -> list:
        coord_list = []
        coord_list.append([coord[0]-1, coord[1]])
        coord_list.append([coord[0], coord[1]-1])
        coord_list.append([coord[0]+1, coord[1]])
        coord_list.append([coord[0], coord[1]+1])
        for coord_ in coord_list:
            if coord_[0] < 0 or M-1 < coord_[0] or coord_[1] < 0 or N-1 < coord_[1]:
                coord_list.remove(coord_)
        return coord_list

    def baechu_boom_chain(coord):
        coord_visited = []
        coord_visited.append(coord)
        def baechu_boom(coord):
            coord_list_ = make_searching_list(coord)
            for coord_ in coord_list_:
                if baechu_exsist(coord_list, coord_):
                    coord_visited.append(coord_)
                    coord_list.remove(coord_)
                else:
                    pass
        while len(coord_visited):
            target = coord_visited.pop(0)
            baechu_boom(target)

    while len(coord_list):
        target = coord_list.pop(0)
        baechu_boom_chain(target)
        worm += 1
    print(worm)

if __name__ == '__main__':
    main()