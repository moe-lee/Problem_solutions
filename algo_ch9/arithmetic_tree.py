operator = {
    "+" : lambda x, y : x + y,
    "-" : lambda x, y : x - y,
    "*" : lambda x, y : x * y,
    "/" : lambda x, y : x / y
}

for test_case in range(1, 11) :
    N = int(input())
    data = [None for _ in range(N+1)]
    tree = [{} for _ in range(N+1)]
    for _ in range(N) :
        info = input().split()
        node_num = int(info[0])
        if len(info) == 2:
            data[node_num] = int(info[1])
        else :
            data[node_num] = info[1]
            for i in range(2, len(info)) :
                tree[node_num]["L" if i == 2 else "R"] = int(info[i])
    
    def calc(root) :
        if not tree[root] :
            return data[root]
        else :
            left = calc(tree[root]["L"])
            right = calc(tree[root]["R"])
            return operator[data[root]](left ,right)
    print('#'+str(test_case), int(calc(1)))