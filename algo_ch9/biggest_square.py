import sys
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    DP_width = [[0 for _ in range(M)] for _ in range(N)]
    DP_height = [[0 for _ in range(M)] for _ in range(N)]
    DP_square = [[0 for _ in range(M)] for _ in range(N)]
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    max_side = 0
    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 1 :
                DP_width[i][j], DP_height[i][j] = 1, 1
                if (j-1 >= 0) : DP_width[i][j] += DP_width[i][j-1]
                if (i-1 >= 0) : DP_height[i][j] += DP_height[i-1][j]
                cur_side = min(DP_width[i][j], DP_height[i][j], (DP_square[i-1][j-1]+1) if (i-1 >= 0 and j-1 >= 0) else 1)
                DP_square[i][j] = cur_side
                max_side = max(max_side, cur_side)
    print(max_side ** 2)
solve()

'''
4 7
1110110
1110111
0111101
0000111

3 3
111
000
000
'''
