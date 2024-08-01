import sys
sys.setrecursionlimit(40000)
class Node :
    def __init__(self, name, depth) :
        self.name = name
        self.childs = {}
        self.depth = depth

def solve() :
    n = int(sys.stdin.readline())
    root = Node('root',-1)
    root.depth = -1
    
    for i in range(n) :
        parent = root
        path = input().split('\\')
        for token in path :
            if token not in parent.childs :
                parent.childs[token] = Node(token, parent.depth + 1)
            parent = parent.childs[token]
    
    def dfs(root, keys) :
        if keys == None : 
            return
        for c in keys :
            print(f'{" "*root.childs[c].depth}{root.childs[c].name}')
            dfs(root=root.childs[c], keys= sorted(list(root.childs[c].childs.keys())))
    dfs(root=root, keys = sorted(list(root.childs.keys())))
solve()