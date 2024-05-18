import sys
from copy import deepcopy as dcp

def getShortestDist(tree, root, B, visited) :
    visited.add(root)
    if root == B : return (True, 0)
    for i, n in enumerate(tree[root]) :
        if n[0] not in visited :
            child_flag, child_weight = getShortestDist(tree, n[0], B, visited)
            if child_flag :
                return (True, child_weight + n[1])
    return (False, 0)

def solve():
    N, M = tuple(map(int, input().split()))
    tree = [dcp([]) for _ in range(N + 1)] # 저장 형식은 (노드, 가중치)
    
    for _ in range(N-1) :
        P, C, D = tuple(map(int, input().split()))
        tree[P].append((C,D))
        tree[C].append((P,D))
    
    for _ in range(M) :
        dist= [sys.maxsize]*(N+1)
        A, B = tuple(map(int, input().split()))
        visited = set()
        dist = getShortestDist(tree, A, B, visited=visited)
        print(dist[1])

solve()