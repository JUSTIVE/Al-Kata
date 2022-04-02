import sys
from typing import List
from functools import reduce
def main():
    KEY = sys.stdin.readline().split()[0]
    KEY = 'LOVE'
    N = int(sys.stdin.readline().split()[0])
    InputNames = []
    for i in range(N):
        InputNames.append(sys.stdin.readline().split()[0])

    ScoresList = list(map(lambda name: GetScore(KEY, name), InputNames))
    Scores = list(map(CalScore, ScoresList))
    MaxIndexes = FindMaxScoreIndex(Scores)
    print(FindMaxScoreSorted([InputNames[j] for j in MaxIndexes]))

def FindMaxScoreSorted(Names: List[str]) -> int:
    return sorted(Names)[0]

def FindMaxScoreIndex(Scores: List[int]) -> list:
    maxscore = max(Scores)
    return [i for i,x in enumerate(Scores) if x == maxscore]

def CalScore(ScoresList: List[int]):
    sums = []
    for i in range(len(ScoresList)):
        for j in range(i+1, len(ScoresList)):
            sums.append(ScoresList[i]+ScoresList[j])
    multiples = reduce(lambda x, y: x*y, sums)
    return multiples%100

def GetScore(KEY: str, Name: str) -> list:
    scores = [0]*len(KEY)
    for idx, char in enumerate(list(KEY)):
        # scores[idx] = GetCharNumber(Name, char, 0, 0)
        scores[idx] = GetCharNumber(KEY+Name, char, 0, 0)
    return scores
        
def GetCharNumber(Name: str, char: str, idx: int, number: int):
    # print(Name)
    new_idx = Name.find(char, idx)
    if new_idx == -1:
        return number
    else:
        return GetCharNumber(Name, char, new_idx+1, number+1)

if __name__ == '__main__':
    main()