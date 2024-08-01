import sys
sys.setrecursionlimit(30000)
class Node :
    def __init__(self, data = None) :
        self.data = data
        # 한 번 기록된 자식은 삭제되지 않는다.
        self.hash = dict()

visited = set()
def DFS(root, depth) : # depth of entracne = -1
    visited.add(root)
    if root.data != 'root' :
        print('--'*(depth), end='')
        print(root.data)
    children = list(root.hash.keys())
    children.sort()
    for c in children :
        if root.hash[c] not in visited :
            DFS(root.hash[c], depth=depth+1)
    return


def solve() :
    N = int(sys.stdin.readline())
    entrance = Node('root')
    

    for _ in range(N) :
        cur_node = entrance
        ipt = sys.stdin.readline().split()
        K = int(ipt[0])
        for i in range(1, K+1) :
            if ipt[i] not in cur_node.hash :
                newNode = Node(data=ipt[i])
                cur_node.hash[ipt[i]] = newNode
            cur_node = cur_node.hash[ipt[i]]
    
    DFS(entrance, -1)
solve()