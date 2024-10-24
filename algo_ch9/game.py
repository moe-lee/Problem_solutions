import sys
sys.setrecursionlimit(10**5)
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    UNVISITED = -1
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    visited = [[UNVISITED for _ in range(M)] for _ in range(N)]
    onStack = [[False for _ in range(M)] for _ in range(N)]
    step_dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    #SCC가 있는지 확인하기 위해 Stack을 사용한다.
    def DFS(row, col) :
        max_move = 0
        onStack[row][col] = True
        for sr, sc in step_dir :
            nr, nc = row + (int(grid[row][col]) * sr), col + (int(grid[row][col]) * sc)
            if (0<= nr < N) and (0<= nc < M) and grid[nr][nc] != 'H' :
                if(onStack[nr][nc] == True) :
                    print(-1)
                    exit()
                if(visited[nr][nc] == UNVISITED) :
                    visited[nr][nc] = DFS(nr, nc)
                max_move = max(max_move, visited[nr][nc])
        onStack[row][col] = False
        return max_move + 1
    visited[0][0] = DFS(0, 0)
    print(visited[0][0])
solve()