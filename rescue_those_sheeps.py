import sys

def solve() :
    n = int(sys.stdin.readline())
    tree = [[] for _ in range(n+1)]
    island = [[0,0] for _ in range(n+1)]
    for i in range(2, n+1) :
        t, a, p = sys.stdin.readline().split()
        a = int(a)
        p = int(p)
        if t == 'W' : a *= -1
        island[i][0] = a
        tree[i].append(p)
        tree[p].append(i)
    
    visited= [False for _ in range(n+1)]
    recursive_stack = [0]
    curr_node = 1
    while curr_node :
        visited[curr_node] = True
        if tree[curr_node] and visited[tree[curr_node][-1]] :
            tree[curr_node].pop()
        
        if tree[curr_node] :
            recursive_stack.append(curr_node)
            curr_node = tree[curr_node].pop()
        else :
            sheeps_so_far = max(0, sum(island[curr_node]))
            island[recursive_stack[-1]][1] += sheeps_so_far
            curr_node = recursive_stack.pop()
    
    print(island[0][1])
    return

if __name__ == '__main__' :
    solve()