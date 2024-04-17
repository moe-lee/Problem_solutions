def compress(his) :
    if not his : return []
    res = [his[0]]
    for i in range(1, len(his)) :
        if his[i] != his[i-1] :
            res.append(his[i])
    return res

def solve() :
    N, Q = tuple(map(int, input().split()))
    back_stack = []
    forward_q = []
    curr_page = None
    for _ in range(Q) :
        query = input().split()
        if query[0] == 'A' :
            if curr_page :
                back_stack.append(curr_page)
            curr_page = query[1]
            forward_q.clear()
        elif query[0] == 'B' :
            if back_stack :
                forward_q.append(curr_page)
                curr_page = back_stack.pop()
        elif query[0] == 'F' :
            if forward_q :
                back_stack.append(curr_page)
                curr_page = forward_q.pop()
        else :
            back_stack = compress(back_stack)
    print(curr_page)
    if not back_stack :
        print(-1, end='')
    else :
        while back_stack :
            print(back_stack.pop(), end=' ')
    print()
    if not forward_q :
        print(-1, end='')
    else :
        while forward_q :
            print(forward_q.pop(), end=' ')
    return

if __name__ == '__main__' :
    solve()