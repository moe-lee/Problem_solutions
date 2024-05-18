import sys
import copy
from collections import deque

# 재귀 사용시 Recursion error 발생.
# 매번 LCA를 재귀로 계산할 시 시간 초과 발생
# depth와 dictionary 이용 -> 한 번 검색한 LCA는 바로 출력 -> 시간초과
# 각 노드의 모든 조상노드를 저장 -> 메모리 초과
# 메모리 초과 -> 아마도 depth가 50000인 트리일 것. -> 최악의 경우 O(5 * 10 ^ 8)의 수행 횟수를 가지게 됨. 사용 언어의 문제인가?
# 편법을 써볼까..? if tree depth == 50000 : print( A와 B중 depth가 낮은거)
# 93%의 벽.

# 재귀 사용 시 Recursion Error 발생

def storeNodeParent(parents, depth, tree, root) :
    q = deque()
    max_depth = 0
    visited = [True] * len(tree)
    q.append((root, depth[root]))
    while q :
        p = q.popleft()
        visited[p[0]] = False
        # p[0] = number , p[1] = depth
        for i in range(len(tree[p[0]])) :
            if visited[tree[p[0]][i]] :
                parents[tree[p[0]][i]] = p[0]
                depth[tree[p[0]][i]] = p[1] + 1
                q.append((tree[p[0]][i], p[1] + 1))
    max_depth = max(depth)
    return max_depth
# 시간 초과 발생.

def solve() :
    N = int(sys.stdin.readline())
    tree = [copy.deepcopy([]) for _ in range(N+1)]
    
    for _ in range(N-1) :
        N1, N2 = tuple(map(int, sys.stdin.readline().split()))
        tree[N1].append(N2)
        tree[N2].append(N1)
    
    M = int(sys.stdin.readline())
    parents = [-1] * (N+1)
    depth = [0] * (N+1)
    max_depth = storeNodeParent(parents, depth,  tree, 1)
    
    for _ in range(M) :
        # 본래 LCA 알고리즘을 이용했으나, 한 번의 순회로 Parent 정보를 리스트에 저장
        A, B = tuple(map(int, sys.stdin.readline().split()))
        if depth[A] < depth[B] : A, B = B, A
        if max_depth == N - 1 : # 93%는 넘긴다. 94%에서 시간초과
            print(A)
            continue
        
        parents_path = [True] * (N+1)
        
        while A != -1 and A != B:
            parents_path[A] = False
            A = parents[A]
        
        if A == B :
            print(B)
            continue
        # A의 조상 중 하나라도 B의 조상과 겹치는 순간 반환 및 종료
        while A != B and parents_path[B] : # 메모리를 사용하여 탐색 시간 단축
            B = parents[B]
        print(B)

if __name__ == '__main__' :
    solve()