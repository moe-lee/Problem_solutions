import sys
from collections import deque

def solve() :
    s = sys.stdin.readline().strip()
    exp = sys.stdin.readline().strip()
    ans = deque()
    dq = deque()
    exp_len = len(exp)
    for c in s :
        if dq and exp[dq[-1][1]] == c :
            dq.append((c, dq[-1][1] + 1))
        elif c == exp[0] :
            dq.append((c, 1))
        else :
            while dq :
                ans.append(dq.popleft())
            ans.append((c, -1))
        if dq and dq[-1][1] == exp_len :
            for _ in range(exp_len) : dq.pop()
    while dq :
        ans.append(dq.popleft())
    
    if len(ans) == 0 :
        print("FRULA")
    else :
        for c, _ in ans :
            print(c, end="")

solve()