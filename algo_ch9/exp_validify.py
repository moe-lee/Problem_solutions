operators ={"*", "/", "+", "-"}
for test_case in range(1, 11) :
    N = int(input())
    tree = [[] for _ in range(N+1)]
    data = [None for _ in range(N+1)]
    for _ in range(N) :
        info = input().split()
        node_num = int(info[0])
        if len(info) == 2:
            data[node_num] = info[1]
        else :
            data[node_num] = info[1]
            for i in range(2, len(info)) :
                tree[node_num].append(int(info[i]))
    
    def validify(root) :
        if not tree[root] :
            return data[root] not in operators
        else :
            if data[root] not in operators or len(tree[root]) != 2: return False
            return validify(tree[root][0]) and validify(tree[root][1])
    print('#'+str(test_case), 1 if validify(1) else 0)