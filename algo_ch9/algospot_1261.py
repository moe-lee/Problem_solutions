import sys
import heapq

def solve() :
    n, m = map(int, sys.stdin.readline().split())
    dist_mat = [[float('inf') for _ in range(n)] for _ in range(m)]
    board = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    pq = [(0,0,0)]
    dist_mat[0][0] = 0
    while pq :
        cur_dist, cur_row, cur_col = heapq.heappop(pq)
        if cur_row == m-1 and cur_col == n-1 :
            print(cur_dist)
            return
        for s in steps :
            next_row, next_col = cur_row + s[0], cur_col + s[1]
            if next_row >= 0 and next_row < m and next_col >= 0 and next_col < n :
                if dist_mat[next_row][next_col] > cur_dist + board[cur_row][cur_col] :
                    dist_mat[next_row][next_col] = cur_dist + board[cur_row][cur_col]
                    heapq.heappush(pq, (dist_mat[next_row][next_col], next_row, next_col))
    
    print(dist_mat[m-1][n-1])
solve()