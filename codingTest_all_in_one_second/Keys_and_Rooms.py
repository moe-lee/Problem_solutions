from collections import deque

def keysAndRooms(rooms) :
    count = 1
    visited = [False] * len(rooms)
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue :
        cur_room = queue.pop()
        for r in rooms[cur_room] :
            if not visited[r] :
                count += 1
                queue.append(r)
                visited[r] = True
    return count == len(rooms)

print(keysAndRooms(rooms=[[1,3], [3,0,1], [2], []]))