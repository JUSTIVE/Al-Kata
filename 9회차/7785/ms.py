import sys
sys.setrecursionlimit(1000000)


def solution(t):
    def checkRemaining(state, t):
        def resolveAttendState(state, name, attendState):
            if(attendState == 'leave'):
                del state[name]
            elif(attendState == 'enter'):
                state[name] = True
            return state

        if(t == 0):
            return state

        name, attendState = map(
            lambda x: x.strip(),
            sys.stdin.readline().split(' ')
        )
        state = resolveAttendState(state, name, attendState)
        return checkRemaining(state, t-1)

    def polish(state):
        return sorted(state.keys(), reverse=True)

    return polish(checkRemaining({}, t))


t = int(sys.stdin.readline())


def printResult(result):
    map(lambda x: print(x), result)


printResult(solution(t))
