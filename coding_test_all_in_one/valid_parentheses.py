def isValid(s) :
    stack = []
    for p in s :
        if p == '(' :
            stack.append(')')
        elif p == '{' :
            stack.append('}')
        elif p == '[' :
            stack.append(']')
        else :
            if(not stack or stack.pop() != p) :
                print('NO')
                return
    
    if(stack) :
        print('NO')
    else :
        print('YES')

def solve() :
    s = input()
    stack = []
    sticks = 0
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append('(')
        else :
            stack.pop()
            if(s[i-1] == '('):
                sticks += len(stack)
            else :
                sticks += 1
    return sticks

if __name__ == '__main__' :
    print(solve())