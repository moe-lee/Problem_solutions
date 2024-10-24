import sys
from collections import defaultdict
from collections import deque

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    costs = list(map(int,sys.stdin.readline().split()))
    entry_cnt = [0] * (N+1)
    graph = defaultdict(list)
    DP = [0 for _ in range(N+1)]
    for _ in range(K) :
        u, v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        entry_cnt[v] += 1
    target = int(sys.stdin.readline())
    
    def topSort() :
        queue = deque()
        for i in range(1, N+1) :
            if entry_cnt[i] == 0 :
                queue.append((i, costs[i-1]))
                DP[i] = costs[i-1]

        while queue :
            cv, cc = queue.popleft()
            for nv in graph[cv] :
                entry_cnt[nv] -= 1
                DP[nv] = max(DP[nv], cc + costs[nv - 1])
                if entry_cnt[nv] == 0 :
                    queue.append((nv, DP[nv]))
    
    topSort()
    print(DP[target])
    return

def run() :
    T = int(sys.stdin.readline())
    for _ in range(T) :
        solve()
run()

'''
1
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
'''

'''
1
4 4
1 10 3 2
1 2
1 3
2 4
4 3
3

-> 16
ans : 10

1 -> 3 : 10
1 -> 2 -> 4 -> 3 : 5 + 10
3: 동시 진행.
'''

'''
1
4 3
1 1 1 1
1 2
3 2
1 4
4
'''

'''
1
5 8
5 10 20 30 10000
3 4
2 4
2 3
1 4
1 3
1 2
1 5
5 4
4

1
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4

'''

'''
test02 : 필요없는 노드
1
7 6
1 10 2 3 4 5 20
1 3
2 3
3 4
4 5
5 6
7 5
4
ans : 15
comment : 7번 노드는 진입차수 0이지만, 4번 노드 생성을 위해 지을 필요 없다.
'''

'''
test0 : 비용상 뒤로 밀어야 하는 경우
1
6 5
10 10 1000 25 33 1000
1 3
2 3
3 4
4 5
6 4
5
ans : 1068
comment : 6번 노드는 진입차수 0이지만 처음이 아닌 3번 노드와 함께 지어야 최소가 됨.
'''