import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(tree, root) :
    if not tree[root] :
        return (0, 0)
    max_diameter_from_child = 0
    dist_from_leaf = [0] * len(tree[root])
    
    for i, child in enumerate(tree[root]) :
        ch = dfs(tree, child[0]) # max dia _ in sub_tree i = 0, maximum dist from leaf = 1
        max_diameter_from_child = max(max_diameter_from_child, ch[0])
        dist_from_leaf[i] = ch[1] + child[1]
    
    dist_from_leaf.sort(reverse=True)
    curr_node_dia= dist_from_leaf[0]
    if len(dist_from_leaf) > 1 :
        curr_node_dia += dist_from_leaf[1]
    
    max_dia = max(max_diameter_from_child, curr_node_dia)
    #print('root : ' , root, ' dist_from_leaf : ', dist_from_leaf, ' curr_node_dia : ', curr_node_dia, ' max_dia : ', max_dia, ' max_diameter_form_child : ', max_diameter_from_child)
    return (max_dia, dist_from_leaf[0])

def solve() :
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        p, c, w = map(int, sys.stdin.readline().split())
        tree[p].append((c, w))
    
    print(dfs(tree, 1)[0])

solve()