import sys
sys.setrecursionlimit(30000)
def solve() :
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    step = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    dist = [[0 for _ in range(N)] for _ in range(N)]
    
    def getMaxPath(cur_row, cur_col) :
        if dist[cur_row][cur_col] :
            return dist[cur_row][cur_col]
        dist[cur_row][cur_col] = 1
        for s in step :
            next_row, next_col = cur_row + s[0], cur_col + s[1]
            if 0 <= next_row < N and 0 <= next_col < N and grid[next_row][next_col] > grid[cur_row][cur_col] :
                dist[cur_row][cur_col] = max(dist[cur_row][cur_col], getMaxPath(cur_row = next_row, cur_col = next_col) + 1)
        return dist[cur_row][cur_col]
    total_max = 0
    for i in range(N) :
        for j in range(N) :
            total_max = max(total_max, getMaxPath(cur_row=i, cur_col=j))
    print(total_max)
solve()


'''

4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
4

5
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
25

4
3 15 15 15
4 10 11 15
5 9 12 13
20 19 18 17
12
'''