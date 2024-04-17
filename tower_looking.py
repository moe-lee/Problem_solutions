import sys
from copy import deepcopy

def solve() :
    N = int(input())
    buildings = list(map(int, sys.stdin.readline().split()))
    view = [deepcopy([0, -1]) for _ in range(N)]
    # first pass
    stack = []
    for cur_pos, cur_height in enumerate(buildings) :
        while stack and stack[-1][1] <= cur_height :
            stack.pop()
        if stack :
            view[cur_pos][0] += len(stack)
            view[cur_pos][1] = stack[-1][0]
        
        stack.append((cur_pos, cur_height))
    stack.clear()
    
    for i in range(1, N+1) :
        while stack and stack[-1][1] <= buildings[-1 * i] :
            stack.pop()
        if stack :
            view[N-i][0] += len(stack)
            view[N-i][1] = view[N-i][1] if (view[N-i][1] != -1) and abs((N-i) - view[N-i][1]) <= abs((N-i) - stack[-1][0]) else stack[-1][0]
        stack.append((N-i, buildings[-1 * i]))
    
    for i in range(N) :
        print(view[i][0], end=' ')
        
        if view[i][0] != 0 and view[i][1] >= 0 :
            print(view[i][1] + 1, end='')
        print()

solve()