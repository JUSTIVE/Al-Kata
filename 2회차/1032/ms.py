def solve():  # -> string
    testLength = int(input())

    def getTargetQueries(currentIndex, targetIndex, state):
        if(currentIndex == targetIndex):
            return state
        else:
            state.append(input())
            return getTargetQueries(currentIndex+1, targetIndex, state)

    targetQueries = getTargetQueries(0, testLength, [])
    # 표본을 뽑지 않고, reduce로 풀 수 있는 방법도 있음.
    sample = targetQueries[0]

    def checkWord(index, char):
        def checkChar():  # void->Boolean
            return (sum(map(
                    # 1 logics per line
                    lambda x: 1 if x[index] == char else 0,
                    targetQueries))
                    == testLength)
        return char if checkChar() else '?'

    return (
        "".join(list(map(
            lambda x: checkWord(x[0], x[1]),
            enumerate(list(sample))))))


print(solve())
