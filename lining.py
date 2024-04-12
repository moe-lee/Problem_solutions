import sys

def solve() :
    N = int(input())
    stack = []
    line = []
    
    for _ in range(N) :
        line.extend(list(sys.stdin.readline().split()))
    order = sorted(line, key=lambda x : (x[0], int(x[2:])))
    
    i, h = 0, 0
    while h < len(order) :
        if not stack or stack[-1] != order[h] :
            if i >= len(line) :
                print('BAD')
                return
            stack.append(line[i])
            i += 1
        elif stack[-1] == order[h] :
            stack.pop()
            h += 1
    print('GOOD')
    return

if __name__ == '__main__' :
    solve()