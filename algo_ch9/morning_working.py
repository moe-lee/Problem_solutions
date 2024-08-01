import sys
sys.setrecursionlimit(10**5)
def solve() :
    N = int(sys.stdin.readline())
    A = sys.stdin.readline().strip()
    tree = [[[], dict()] for _ in range(N+1)]
    for _ in range(N-1) :
        u, v = map(int, sys.stdin.readline().split())
        tree[u][0].append(v)
        tree[v][0].append(u)
    
    def calcIndoors(root, pred) :
        if pred is not None and A[root-1] == '1' :
            return 1
        sum = 0
        for c in tree[root][0] :
            if c == pred : continue
            if c not in tree[root][1] :
                tree[root][1][c] = calcIndoors(c, root)
            sum += tree[root][1][c]
        return sum
    ans = 0
    for i in range(1, N+1) :
        if A[i-1] == '1':
            ans += calcIndoors(i, None)
    print(ans)
solve()

'''
15
000000011111111
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15

'''