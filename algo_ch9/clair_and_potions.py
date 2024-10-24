import sys
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    possible_list = []
    dispensed = [False] * (N+1)
    graph = [[] for _ in range(N+1)] # 그래프랑,, 진입차수 여러개(레시피 번호가 매핑)
    indegrees = [dict() for _ in range(N+1)]
    rel_num = 1
    for _ in range(M):
        line = list(map(int, sys.stdin.readline().split()))
        for i in range(1, len(line) - 1) :
            graph[line[i]].append((line[-1], rel_num))
        indegrees[line[-1]][rel_num] = line[0]
        rel_num += 1
    # 간선마다 rel_num을 부여 -> to edge의 indegree 딕셔너리에 rel_num : 진입차수 저장.
    # 이후 간선의 rel_num에 대응되는 대상 노드 indegree[rel_num] 감소 시킴.
    _ = sys.stdin.readline()
    clairs = deque()
    for potion in list(map(int, sys.stdin.readline().split())) :
        possible_list.append(potion)
        dispensed[potion] = True
        clairs.append(potion)
    
    while clairs :
        potion = clairs.popleft()
        for dedicated_to, rel_num in graph[potion] :
            indegrees[dedicated_to][rel_num] -= 1
            if indegrees[dedicated_to][rel_num] == 0 and not dispensed[dedicated_to]:
                possible_list.append(dedicated_to)
                dispensed[dedicated_to] = True
                clairs.append(dedicated_to)
    possible_list.sort()
    print(len(possible_list))
    print(*possible_list)
solve()

'''
6 3
3 1 2 3 6
2 2 4 6
2 2 5 6
2
2 4

'''