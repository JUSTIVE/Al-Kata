def solve():
    yeonTeamName = input()
    testLength = int(input())

    def getTargetQueries(currentIndex, targetIndex, state):
        if(currentIndex == targetIndex):
            return state
        else:
            state.append(input())
            return getTargetQueries(currentIndex+1, targetIndex, state)

    targetQueries = getTargetQueries(0, testLength, [])

    def evalLoveMetric(target):
        def getCount(charTarget):
            return target.count(charTarget)
        LValue = getCount('L')
        OValue = getCount('O')
        VValue = getCount('V')
        EValue = getCount('E')
        return (
            (LValue*OValue) *
            (LValue*VValue) *
            (LValue*EValue) *
            (OValue*VValue) *
            (OValue*EValue) *
            (VValue*EValue)
        ) % 100
    # Tuple
    valued = list(map(
        lambda x: [x, evalLoveMetric(x+yeonTeamName)],
        targetQueries))
    maxValue = max(map(lambda x: x.score, valued))

    return (
        sorted(
            filter(
                lambda x: x.score == maxValue, valued),
            key=lambda x: x.value)
    )[0].value
    # 파멸의 피라미드(doom of pyramid),
    # UFCS(universal function call syntax)
    # return (res[0].value)


print(solve())
