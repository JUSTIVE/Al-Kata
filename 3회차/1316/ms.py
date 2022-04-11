import sys
import re


def solve():
    testLength = int(sys.stdin.readline())

    def getTargetQueries(currentIndex, targetIndex, state):
        if(currentIndex == targetIndex):
            return state
        else:
            state.append(sys.stdin.readline())
            return getTargetQueries(currentIndex+1, targetIndex, state)

    targetQueries = getTargetQueries(0, testLength, [])

    def validateGroupWord(value):
        def reduceDuplicateChar(value):
            return re.sub(r'(.)\1', r'$1', value)
        print(">", reduceDuplicateChar(value))

    return len(filter(list(map(validateGroupWord, targetQueries))))


print(solve())
