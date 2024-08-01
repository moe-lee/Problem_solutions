import sys

def solve() :
    N = int(sys.stdin.readline())
    weights = list(map(lambda x : (x-20) // 2, map(int, sys.stdin.readline().split())))
    stack = []
    cur_weights = 0
    weight_change = 0
    disk_moved = 0
    
    get_movements = lambda x : x // 20 * 2 +  (x % 20) // 15 * 2 + x % 20 % 15 // 10 * 2 + x % 20 % 15 % 10 //5 * 2
    
    for w in weights :
        if not stack or cur_weights < w:
            stack.append(w - cur_weights)
            cur_weights = w
        else :
            diff = cur_weights - w
            reduction = 0
            top = 0
            while diff > 0 :
                top = stack.pop()
                reduction += min(top, diff)
                disk_moved += get_movements(min(top, diff))
                tmp = top
                top -= diff
                diff -= tmp
            
            weight_change += (reduction * 2)
            cur_weights -= reduction
            if top > 0 : stack.append(top)
    
    for s in stack :
        weight_change += 2 * s
        disk_moved += get_movements(s)
    
    
    print(weight_change * 2, disk_moved * 2)
solve()