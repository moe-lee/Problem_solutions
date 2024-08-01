import sys
from collections import deque
def solve() :
    N, K = map(int, sys.stdin.readline().split())
    queue = deque()
    visited = dict()
    queue.append((N, 0))
    visited[N] = 0
    rels_and_weights = ((lambda x : 2*x, 0), (lambda x : x + 1, 1), (lambda x : x - 1, 1))
    
    while queue :
        cur_pos, cur_time = queue.popleft()
        if cur_pos in visited and visited[cur_pos] < cur_time :
            continue
        
        if cur_pos > K :
            next_pos = cur_pos - 1
            if next_pos == K :
                visited[K] = min(visited[K] if K in visited else sys.maxsize, cur_time + 1)
            elif next_pos not in visited :
                visited[cur_pos] = cur_time + 1
                queue.append((next_pos, cur_time + 1))

        elif cur_pos <= 0 :
            next_pos = cur_pos + 1
            if next_pos == K :
                visited[K] = min(visited[K] if K in visited else sys.maxsize, cur_time + 1)
            elif next_pos not in visited  :
                visited[cur_pos] = cur_time + 1
                queue.append((next_pos, cur_time + 1))
        else :
            for rel, weight in rels_and_weights :
                if rel(cur_pos) == K :
                    visited[K] = min(visited[K] if K in visited else sys.maxsize, cur_time + weight)
                elif rel(cur_pos) not in visited :
                    visited[rel(cur_pos)] = cur_time + weight
                    queue.append((rel(cur_pos), cur_time + weight))
                elif visited[rel(cur_pos)] > cur_time + weight :
                    visited[rel(cur_pos)] = cur_time + weight
                    queue.append((rel(cur_pos), cur_time + weight))
    
    return visited[K]

print(solve())