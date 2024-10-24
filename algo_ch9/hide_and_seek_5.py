import sys
from collections import deque

# aruarian dance - nujabes
def solve() :
    N, K = map(int, sys.stdin.readline().split())
    even_odd = [[float('inf') for _ in range(500001)] for _ in range(2)]
    even_odd[0][N] = 0
    
    queue = deque()
    queue.append((N, 0))
    while queue :
        cpos, ceta = queue.popleft()
        if cpos - 1 >= 0 and (even_odd[(ceta + 1) % 2][(cpos - 1)] == float('inf')):
            even_odd[(ceta + 1) % 2][(cpos - 1)] = ceta + 1
            queue.append((cpos - 1, ceta + 1))
        if cpos + 1 <= 500000 and (even_odd[(ceta + 1) % 2][(cpos + 1)] == float('inf')):
            even_odd[(ceta + 1) % 2][(cpos + 1)] = ceta + 1
            queue.append((cpos + 1, ceta + 1))
        if cpos * 2 <= 500000 and (even_odd[(ceta + 1) % 2][(cpos * 2)] == float('inf')):
            even_odd[(ceta + 1) % 2][cpos * 2] = ceta + 1
            queue.append((cpos * 2, ceta + 1))
    i = 0
    while (K + (i*(i+1)) // 2 <= 500000) :
        if (even_odd[0][K + (i*(i+1)) // 2] <= i and i % 2 == 0) or (even_odd[1][K + (i*(i+1)) // 2] <= i and i % 2 == 1) :
            print(i)
            return
        i += 1
    print(-1)
solve()

'''
500000 1
'''