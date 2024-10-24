for test_case in range(1, 11) :
    N = int(input())
    character = ['' for _ in range(N+1)]
    tree = [{} for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(N) :
        info = input().split()
        node_num = int(info[0])
        character[node_num] = info[1]
        for i in range(2, len(info)) :
            tree[node_num]["L" if i == 2 else "R"] = int(info[i])
            indegree[int(info[i])] += 1
    root = 1
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            root = i
            break
    
    def DFS(root) :
        left, right = '', ''
        if "L" in tree[root] :
            left = DFS(tree[root]["L"])
        
        if "R" in tree[root] :
            right = DFS(tree[root]["R"])
        return left + character[root] + right
    print('#'+str(test_case), DFS(root))