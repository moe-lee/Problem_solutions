def solve() :
    N = int(input())
    s = input()
    stack = []
    
    for p in s :
        if p == '(' :
            stack.append(')')
        else :
            sub_len = 0
            while stack and stack[-1] != p and stack[-1] != '*':
                sub_len += stack.pop()
            if not stack or stack[-1] == '*':
                stack.append(sub_len)
                stack.append('*')
            else :
                stack.pop()
                stack.append(sub_len + 2)
    
    max_len, sub_len = 0, 0
    for i in stack :
        if i != ')' and i != '*' :
            sub_len += i
        else :
            max_len = max(max_len, sub_len)
            sub_len = 0
    max_len = max(max_len, sub_len)
    print(max_len)
    return

solve()