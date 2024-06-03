import sys
sys.setrecursionlimit(50000)

def solve() :
    N, S, D = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        x, y = map(int, sys.stdin.readline().split())
        tree[x].append(y)
        tree[y].append(x)
    
    visited = [False] * (N+1)
    
    def DFS(root) :
        dist_from_child = []
        visited[root] = True
        for v in tree[root] :
            if not visited[v] :
                dist_from_child.append(DFS(root=v))
        
        if not dist_from_child : # leaf node
            return (0, 1)
        
        current_step, max_dist_so_far = 0, 0
        # 0 : current_step, 1 : max_dist_so_far
        for d in dist_from_child :
            if d[1] > D :
                current_step += d[0] + 1
            max_dist_so_far = max(max_dist_so_far, d[1])
        return(current_step, max_dist_so_far + 1)
    
    print(DFS(root=S)[0] * 2)

solve()