import sys

def calcOutsider() :
    n = int(sys.stdin.readline().strip())
    precedes = [0] * (n + 1)
    direction = [None]
    direction.extend(list(map(int, sys.stdin.readline().split())))
    visited = [False] * (n+1)
    outsiders = 0
    for i in range(1, n + 1) :
        if not visited[i] :
            count = 0
            precedes[i] = count
            visited[i] = True
            cur_v = i
            cycle_set = set()
            cycle_set.add(i)
            while not visited[direction[cur_v]] :
                cur_v = direction[cur_v]
                cycle_set.add(cur_v)
                count += 1
                precedes[cur_v] = count
                visited[cur_v] = True
            
            if direction[cur_v] in cycle_set :
                outsiders += precedes[direction[cur_v]]
            else :
                outsiders += precedes[cur_v] + 1
    print(outsiders)
    return

def solve() :
    T = int(input())
    for _ in range(T) : calcOutsider()

solve()