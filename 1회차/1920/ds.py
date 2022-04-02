import sys
from typing import List

def main():
    N = int(sys.stdin.readline().split()[0])
    TargetNumbers = GetNumbers(sys.stdin.readline(), N)

    M = int(sys.stdin.readline().split()[0])
    SearchNumbers = GetNumbers(sys.stdin.readline(), M)

    Results = GetOutput(SearchNumbers, TargetNumbers)
    [print(result) for result in Results]
    
    # map(print, Results)

def GetOutput(SearchNumbers: List[int], TargetNumbers: List[int]) -> List[int]:
    return list(map(int, map(lambda x: x in TargetNumbers, SearchNumbers)))

# def GetOutput(SearchNumbers: List[int], TargetNumbers: List[int]) -> List[int]:
#     return list(map(int,[NumberExist(SearchNumber, TargetNumbers) for SearchNumber in SearchNumbers]))

# def NumberExist(SearchNubmer: int, TargetNumbers: List[int]):
#     return SearchNubmer in TargetNumbers

def GetNumbers(Input: str, InputLength: int) -> List[int]:
    return list(map(int, Input.split()))[0:InputLength]

if __name__ == '__main__':
    main()