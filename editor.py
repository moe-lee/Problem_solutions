import sys
def solve() :
    s = input()
    n = int(input())
    postfix = []
    stack = [c for c in s];
    
    for _ in range(n) :
        op = input().split()
        if(op[0] == 'L') :
            if(stack) :
                postfix.append(stack.pop())
        elif op[0] == 'D' :
            if(postfix) :
                stack.append(postfix.pop())
        elif op[0] == 'B' :
            if(stack) :
                stack.pop()
        else :
            stack.append(op[1])
    
    for s in stack:
        print(s, end='')
    while postfix :
        print(postfix.pop(), end='')
    return

if __name__ == '__main__' :
    solve()