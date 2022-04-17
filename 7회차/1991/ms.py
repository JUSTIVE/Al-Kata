import sys


def solve():
    def genTree(state, n):
        if n == 0:
            return state
        else:
            p, l, r = sys.stdin.readline().split()
            state[p] = [l, r]
            return genTree(state, n-1)
    tree = genTree({}, int(sys.stdin.readline()))

    def preOrder(tree, node):
        if node == ".":
            return
        else:
            print(node, end='')
            preOrder(tree, tree[node][0])
            preOrder(tree, tree[node][1])

    def inOrder(tree, node):
        if node == ".":
            return
        else:
            inOrder(tree, tree[node][0])
            print(node, end='')
            inOrder(tree, tree[node][1])

    def postOrder(tree, node):
        if node == ".":
            return
        else:
            postOrder(tree, tree[node][0])
            postOrder(tree, tree[node][1])
            print(node, end='')

    preOrder(tree, 'A')
    print()
    inOrder(tree, 'A')
    print()
    postOrder(tree, 'A')


if __name__ == "__main__":
    solve()
