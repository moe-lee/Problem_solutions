import sys

def solve():
    stack = []
    priority = {')' : 0, '(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
    exp = sys.stdin.readline().strip()
    result = []
    for c in exp :
        if c in priority :
            if c != ')' and (c == '(' or not stack or priority[stack[-1]] < priority[c]) :
                stack.append(c)
            else :
                if c == ')' :
                    op = stack.pop()
                    while op != '(' :
                        result.append(op)
                        op = stack.pop()
                else :
                    while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[c] :
                        op = stack.pop()
                        result.append(op)
                    stack.append(c)
        else :
            result.append(c)
    while stack :
        result.append(stack.pop())
    return ''.join(result)

print(solve())