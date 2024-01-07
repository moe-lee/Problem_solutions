from collections import deque
import copy

def BFS(mat, x, y) :
    ac_nodes = deque()
    ac_nodes.append((y,x))
    while ac_nodes :
        node = ac_nodes.popleft()
        mat[node[0]][node[1]] = 0
        if(node[1] > 0 and mat[node[0]][node[1]-1] == 1) :
            mat[node[0]][node[1]-1] = 2
            ac_nodes.append([node[0],node[1]-1])
        if(node[1] < len(mat[0]) - 1 and mat[node[0]][node[1]+1] == 1) :
            mat[node[0]][node[1]+1] = 2
            ac_nodes.append([node[0],node[1]+1])
        if(node[0] > 0 and mat[node[0]-1][node[1]]) :
            mat[node[0]-1][node[1]] = 2
            ac_nodes.append([node[0]-1, node[1]])
        if(node[0] < len(mat) - 1 and mat[node[0]+1][node[1]]) :
            mat[node[0]+1][node[1]] = 2
            ac_nodes.append([node[0]+1, node[1]])

def solve() :
    t = int(input())
    for i in range(t) :
        bucket = deque()
        M, N, K = tuple(map(lambda x : int(x), (input()).split()))
        mat = [copy.deepcopy([0] * M) for i in range(N)]
        for j in range(K) :
            X, Y = tuple(map(lambda x : int(x), (input()).split()))
            bucket.append(M * Y + X)
            mat[Y][X] = 1
        union_count = 0
        
        while bucket :
            pos = bucket.pop()
            if(mat[pos//M][pos%M]) :
                union_count += 1
                BFS(mat, pos%M, pos//M)
        print(union_count)

def main() :
    solve()
main()