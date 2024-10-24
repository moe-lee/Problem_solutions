import sys
sys.setrecursionlimit(10**5)
def solve() :
    N = int(sys.stdin.readline())
    populations = list(map(int, sys.stdin.readline().split()))
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)
    def DFS(parent, cur_node) :
        selected, not_selected = populations[cur_node - 1], 0
        for nv in tree[cur_node] :
            if nv == parent : continue
            child_ns, child_s = DFS(parent=cur_node, cur_node=nv)
            not_selected += max(child_ns, child_s)
            selected += child_ns
        return (not_selected, selected)
    
    print(max(DFS(0, 1)))
    return
#solve()

import bisect
import math
T = int(input())

for test_case in range(1, T + 1) :
    N = int(input())
    ints = []
    fracs = []
    for _ in range(N) :
        num = input()
        if num.find('.') == -1 : ints.append(int(num))
        else : fracs.append(float(num))
    cases = 0
    if len(ints) > 1:cases += math.comb(len(ints), 2)
    elif len(ints) == 0 :
        print(0)
        continue
    ints.sort()
    for f in fracs :
        cases += (len(ints) - bisect.bisect_right(ints, 1 / f))
    print(cases)
'''
2
3
1
2
3
5
0.03
0.3
7
90
1100

'''


'''
6
100 1000 100 100 1000 1000
1 2
1 3
1 4
3 5
4 6

7
100 1 1 100 1 1 100
1 2
2 3
3 4
3 5
5 6
5 7

6
1 100 1 1 1 1
1 3
2 1
3 4
4 5
5 6

5
5000 1 1 3000 1
1 2
2 3
2 4
2 5

5
1 100 100 1 100
1 2
1 3
2 4
5 4
'''