T = int(input())
for testCase in range(1, T+1) :
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    transpose_cnt = 0
    transposed = False
    for i in range(N-1, -1, -1) :
        for j in range(i, -1, -1) :
            if matrix[i][j] != ((i + 1 if not transposed else j + 1) - 1 ) * N + (j + 1 if not transposed else i + 1) :
                transpose_cnt += 1
                transposed = not transposed
                break
    print(transpose_cnt)

'''
3
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
5
1 2 11 4 21
6 7 12 9 22
3 8 13 14 23
16 17 18 19 24
5 10 15 20 25
5
1 6 3 16 5
2 7 8 17 10
11 12 13 18 15
4 9 14 19 20
21 22 23 24 25
'''