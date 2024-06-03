from collections import deque

def canVisitAllRooms(rooms) :
    visited = [False] * len(rooms)

    def dfs(v) :
        visited[v] = True
        for next_v in rooms[v] :
            if not visited[next_v] :
                dfs(next_v)
    
    def bfs(v) :
        visited[v] = True
        queue = deque()
        queue.append(v)
        while queue :
            cur_v = queue.popleft()
            for next_v in rooms[cur_v] :
                if not visited[next_v] :
                    visited[next_v] = True
                    queue.append(next_v)
    
    dfs(0)
    return all(visited)

def keysAndRooms(rooms) :
    n = len(rooms)
    room_cnt = 1
    queue = deque()
    queue.append(0)
    visited = [False] * n
    visited[0] = True
    
    while queue :
        cur_room = queue.popleft()
        
        for v in rooms[cur_room] :
            if not visited[v] :
                visited[v] = True
                room_cnt += 1
                queue.append(v)
    return room_cnt == n

print(keysAndRooms(rooms=[[1,3],[2,4],[0],[4],[],[3,4]]))