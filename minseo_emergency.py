import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)

def dfs(tree, visited, anccesters, parent, root) :
    visited.add(root)
    cutting_cnt = 0
    anccesters.add(root)
    for i in range(len(tree[root])) :
        if tree[root][i] not in visited :
            cutting_cnt += dfs(tree=tree, visited=visited, anccesters=anccesters, parent=root, root=tree[root][i])
        elif tree[root][i] != parent and tree[root][i] in anccesters:
            cutting_cnt += 1
    anccesters.remove(root)
    return cutting_cnt

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]
    num_of_trees = 0
    
    for _ in range(M) :
        A, B = map(int, sys.stdin.readline().split())
        tree[A].append(B)
        tree[B].append(A)
    
    visited = set()
    cutting_cnt = 0
    for i in range(1, N+1) :
        if i not in visited :
            anccesters = set()
            num_of_trees += 1
            cutting_cnt += dfs(tree=tree,visited=visited, anccesters= anccesters, parent=0, root=i)
    
    print((num_of_trees - 1) + cutting_cnt)

solve()