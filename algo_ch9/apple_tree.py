import sys
sys.setrecursionlimit(30000)
def solve() :
    N = int(sys.stdin.readline())
    binary_traversal = sys.stdin.readline().strip()
    A, B = map(int, sys.stdin.readline().split())
    wormed = [False] * (N+1)
    tree = [[] for _ in range(N + 1)]
    zero_one = [[-1, -1] for _ in range(N + 1)]
    
    last_apple = 1
    cur_node = 0
    stack = []
    for i, b in enumerate(binary_traversal) :
        if b == "0" :
            tree[cur_node].append((last_apple))
            zero_one[last_apple][0] = i+1
            if i + 1 in (A, B) :
                wormed[last_apple] = True
            stack.append(cur_node)
            cur_node = last_apple
            last_apple += 1
        else :
            zero_one[cur_node][1] = i + 1
            if i + 1 in (A, B) :
                wormed[cur_node] = True
            cur_node = stack.pop()
    
    def LCA(root) :
        if wormed[root] :
            return root
        wormed_descendents = None
        for c in tree[root] :
            c_res = LCA(c)
            if c_res and wormed_descendents :
                wormed_descendents = root
            elif c_res :
                wormed_descendents = c_res
        return wormed_descendents
    lca = LCA(0)
    print(zero_one[lca][0], zero_one[lca][1])
solve()