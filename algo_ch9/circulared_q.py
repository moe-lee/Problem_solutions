from collections import deque

def solve() :
    n, m = tuple(map(lambda x : int(x), input().split()))
    positions = list(map(lambda x : int(x), input().split()))
    queue = deque(range(1, n+1))
    total_shift = 0
    for i in positions :
        size = len(queue)
        count = 0
        t = queue.popleft()
        while t != i :
            count += 1
            queue.append(t)
            t = queue.popleft()
        total_shift += min(count, size - count)
    
    print(total_shift)

solve()
