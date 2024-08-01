import sys
sys.setrecursionlimit(50000)
def solve() :
    M, N = map(int, sys.stdin.readline().split())
    grid = []
    num_of_path = dict()
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for _ in range(M) :
        grid.append(list(map(int,sys.stdin.readline().split())))
    def dfs(row, col) :
        if (row, col) == (0, 0) :
            num_of_path[(row, col)] = 1
            return 1
        possible_paths = 0
        for step in steps :
            next_row = row + step[0]
            next_col = col + step[1]
            if next_row >= 0 and next_row < M and next_col >= 0 and next_col < N :
                if grid[next_row][next_col] > grid[row][col] :
                    if (next_row, next_col) in num_of_path :
                        possible_paths += num_of_path[(next_row, next_col)]
                    else :
                        possible_paths += dfs(next_row, next_col)
        num_of_path[(row, col)] = possible_paths
        return num_of_path[(row, col)]
    print(dfs(M-1, N-1))
solve()

'''
1 2
1 1

2 3
5 4 1
4 3 2

4 4
16 9 8 1
15 10 7 2
14 11 6 3
13 12 5 4

3 3
9 4 3
8 5 2
7 6 1

3 5
55 99 49 48 47
54 99 50 99 46
53 52 51 99 45

4 4
9 8 7 6
8 7 6 5
7 6 5 4
6 5 4 3

7 7
100 33 58 59 61 31 30
74 31 55 62 70 70 29
73 98 49 47 11 10 36
62 59 56 45 44 8 7
59 58 54 53 41 7 3
56 32 29 18 40 4 3
34 31 26 40 39 73 1
'''
'''

5 5
27 26 25 24 23
28 29 30 31 22
17 18 19 20 21
16 32 33 34 35
15 14 13 12 11

4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

2 18
98 91 89 80 76 74 65 58 50 49 44 32 26 23 17 15 14 8
95 91 83 82 70 67 65 55 54 50 41 27 22 20 14 10 7 3
'''

