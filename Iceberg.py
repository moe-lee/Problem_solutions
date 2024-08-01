import sys
sys.setrecursionlimit(50000)

def solve() :
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n) :
        grid.append(list(map(int, sys.stdin.readline().split())))
    
    years = 0
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set()
    pos_stack = []
    
    def dfs(i, j) :
        if(grid[i][j] == 0) and (i,j) not in visited :
            grid[pos_stack[-1][0]][pos_stack[-1][1]] = max(0, grid[pos_stack[-1][0]][pos_stack[-1][1]] - 1)
            return
        else :
            visited.add((i,j))
            for s in steps :
                next_row, next_col = i + s[0], j + s[1]
                if (0 <= next_row and next_row < n) and (0 <= next_col and next_col < m) :
                    if (next_row, next_col) not in visited :
                        pos_stack.append((i,j))
                        dfs(next_row, next_col)
                        pos_stack.pop()
    num_of_iceberg = 0
    first = True
    while (num_of_iceberg == 1) or first:
        visited.clear()
        pos_stack.clear()
        num_of_iceberg = 0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] > 0 and (i,j) not in visited :
                    num_of_iceberg += 1
                    dfs(i, j)
        years += 1
        first = False
    if num_of_iceberg == 0 :
        print(0)
    else :
        print(years-1)
    return
solve()

def LCA(root, p, q) :
    if root == None :
        return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q :
        return root
    elif left and right :
        return root
    return left or right
