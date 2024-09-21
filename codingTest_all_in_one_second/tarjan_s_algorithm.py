# tarjan's algorithm 
# 방향 그래프 내에 포함된 SCC(Strongly Connected Component)들을 탐지한다.
# DFS를 이용하여 넘버링하고 도달 가능한 노드 중 최소 노드 번호를 저장한 것을 low-link value 라고 한다.
# low-link value는 DFS를 어느 노드에서 시작하느냐 또는 어떤 순서로 방문하느냐에 따라 달라질 수 있다.
# 일반적으로 low-link value를 이용해 SCC를 구분할 수 있으나, DFS 순회 순서에 과하게 의존하기 때문에
# 전체 SCC 갯수와 일치하지 않는 low-link value들이 발생할 수 있다.

# tarjan's algorithm은 한 SCC가 다른 SCC에 의해 방해받지 않도록 관리해주며
# 앞서 언급한 방식은 DFS 후에 low-link value를 업데이트 하는 것과 다르게
# DFS를 하면서 동시에 low-link value를 갱신한다. 이는 O(V+E)의 시간 복잡도가 된다.
# 즉, self-contained cycle(완결된 사이클)은 DFS를 수행하면서 발견 가능하므로
# 발견과 동시에 low-link value를 할당하여 이후 SCC 내의 노드가 사이클 밖의 노드에 도달할 수 있음으로써 발생하는 오류를 제거한다.

# tarjan's algorithm은 임의의 노드 방문 순서에 대처하기 위해 stack을 사용한다.
# stack에는 현재 SCC인지 판단하기 위해 방문한 노드들이 기록된다.
# 방문한 노드들에는 방문 표시를 한다.
# 처음 방문한 노드는 번호, 번호랑 같은 값을 low-link value로 할당하고 stack에 넣는다.
# 만약 다음노드를 방문했고 stack에 있다면 현재 노드 low-link value를 다음 노드 값으로 갱신한다.
# backtracking을 통해 현재 노드 번호와 low-link value가 동일하다면 SCC를 시작한 노드(SCC의 Representative)이므로
# 하나의 완결된 SCC를 탐색하였음을 나타낸다. 따라서 stack에서 현재 노드 번호가 나올때까지 pop 연산을 수행한다.
# 이것을 모든 노드가 방문될 때까지 반복한다.

UNVISITED = -1
n = 7
graph = [ [],
[2, 5], [3, 5], [], [5], [6], [], [4]
]

max_id = 0
sccCount = 0
ids = [0] * (n)
low = [0] * (n)
onStack = [False] * (n)
stack = []

def findScc() :
    for i in range(n) : ids[i] = UNVISITED
    for i in range(n) :
        if ids[i] == UNVISITED :
            dfs(i)
    return low

def dfs(at) :
    stack.append(at)
    onStack[at] = True
    ids[at] = low[at] = max_id
    max_id += 1
    
    for to in graph[at] :
        if ids[to] == UNVISITED : dfs(to)
        if onStack[to] : low[at] = min(low[at],low[to])
    
    if(ids[at] == low[at]) :
        node = stack.pop()
        while stack :
            onStack[node] = False
            low[node] = ids[at]
            if node == at : break
        sccCount += 1
    return sccCount