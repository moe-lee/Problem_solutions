import sys
sys.setrecursionlimit(20000)

def solve() :
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1) :
        args = list(map(int, sys.stdin.readline().split()))
        node, _ = args[0], args.pop()
        for i in range(1, len(args), 2) :
            tree[node].append((args[i], args[i+1]))
    visited = [False] * (N+1)
    
    def dfs(root) :
        visited[root] = True
        dist_from_subtree = []
        max_diameter_so_far = 0
        max_diameter_from_child = 0
        for v in tree[root] :
            # v는 튜플 (node_number, weight)
            if not visited[v[0]] :
                # 노드 방문, 반환값 : 최대 서브트리 경로 값과 서브트리 기준 지름
                child_values = dfs(v[0])
                max_diameter_from_child = max(max_diameter_from_child, child_values[1])
                dist_from_subtree.append(child_values[0] + v[1])
        
        if not dist_from_subtree : # leaf node인 경우
            return (0, 0)
        
        dist_from_subtree.sort()
        
        max_diameter_so_far += dist_from_subtree[-1]
        if len(dist_from_subtree) > 1 :
            max_diameter_so_far += dist_from_subtree[-2]
        
        max_diameter_so_far = max(max_diameter_so_far, max_diameter_from_child)
        
        return (max(dist_from_subtree), max_diameter_so_far)
    
    print(dfs(1)[1])
    return
solve()