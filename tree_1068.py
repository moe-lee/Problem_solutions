import copy

def getLeafCount(tree, root, R) :
    if root == R : return 0
    leaves = [0] * len(tree[root])
    for i in range(len(leaves)) :
        leaves[i] = getLeafCount(tree, tree[root][i], R)
    
    if not tree[root] or sum(leaves) == 0 : return 1
    return sum(leaves)

def solve() :
    N = int(input())
    tree = [copy.deepcopy([]) for _ in range(N)]
    nodes = list(map(int, input().split()))
    root = 0
    for i, n in enumerate(nodes) :
        if n > -1 : tree[n].append(i)
        else : root = i
    R = int(input())
    
    print(getLeafCount(tree, root, R))

solve()