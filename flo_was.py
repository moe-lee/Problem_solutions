
def floyd(edges, n, m) :
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for u,v,c in edges :
        dp[u][v] = c
        dp[v][u] = c
    
    for k in range(n) :
        for i in range(n):
            for j in range(n) :
                if i == j : continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for l in dp :
        print(l)

def bellman(edges, n, start, final) :
    dist = [float('inf') for _ in range(n)] # distance buffer
    dist[start] = 0
    for _ in range(n-1) : # Bellman ford algorithm. core logic.
        for u, v, c in edges : # expected input form : u(edge start), v(edge end), c(edge cost)
            dist[v] = min(dist[v], dist[u] + c) # compare the costs
            # calculate the minimum cost from start to v
    for u, v, c in edges : # detect the negative cycle
        if dist[v] > dist[u] + c :
            print("negative weighted cycle")
            return float('inf') # if it exists, return infinity value
    print(dist) # else print the matrix
    return dist[final] # return minimum cost to final

n,m = map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
bellman(edges=edges,n=n, start=0, final=-1)
