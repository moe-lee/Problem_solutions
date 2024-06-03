import sys

'''
sys.setrecursionlimit() 는 메모리초과를 발생시킨다.
'''

def solve() :
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    
    tree[0].append(1)
    
    early_adapter = [0] * (N+1)
    visited = set()
    stack = [None]
    child_is_not_early = False
    cur_node = 1
    while cur_node is not None:
        if child_is_not_early and early_adapter[cur_node] == 0:
            early_adapter[cur_node] = 1
            child_is_not_early = False
        
        # 현재 노드에 방문했음을 표시한다.
        if cur_node not in visited :
            visited.add(cur_node)
        # 부모 노드 포인터는 제거한다.
        if tree[cur_node] and tree[cur_node][-1] in visited :
            tree[cur_node].pop()
        
        # 만약 방문안한 자식이 있다면, 방문한다.
        if tree[cur_node] :
            next_node = tree[cur_node].pop()
            if cur_node is not None:
                stack.append(cur_node)
            cur_node = next_node 
            child_is_not_early = False
        else :
            if early_adapter[cur_node] == 0 :
                child_is_not_early = True
            else :
                child_is_not_early = False
            cur_node = stack.pop()
    
    print(sum(early_adapter))
    return

solve()