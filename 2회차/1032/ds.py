from functools import reduce
import sys
from typing import List
from functools import reduce

def main():
    N = int(sys.stdin.readline().split()[0])
    # InputFileNames = list(map(lambda x: sys.stdin.readline().split(), range(N)))
    InputFileNames = []
    for l in range(N):
        InputFileNames.append(sys.stdin.readline().split())
    ResultStringSplit = InputFileNames.pop()[0]
    ResultStringSplit_list = list(ResultStringSplit)
    
    for i in range(len(InputFileNames)):
        InputFileNameSplit = list(InputFileNames[i][0])
        for j in range(len(InputFileNameSplit)):
            if ResultStringSplit_list[j] == '?':
                continue
            ResultStringSplit_list[j] = CompareChar(ResultStringSplit[j], InputFileNameSplit[j])
    ResultStringSplit = ''.join(ResultStringSplit_list)
    print(ResultStringSplit)

def CompareStr(InputFileNames: List[str]) -> str:
    ResultString = []    
    for i in range(len(InputFileNames)-1):
        for j in range(len(InputFileNames[0])):
            ResultString[j] = CompareChar(InputFileNames[i+1][j], InputFileNames[i])
        # resultstring = reduce(lambda src, dst: CompareChar(src,dst), )

# def CompareString(src: str, dst: str) -> str:


def CompareChar(src: str, dst: str) -> str:
    if src == dst:
        return src
    else:
        return '?'


if __name__ == '__main__':
    main()