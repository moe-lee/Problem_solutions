def solve() :
    parentheses = input()
    stack = []
    res = 0
    for p in parentheses :
        if p == '(' :
            stack.append(')')
        elif p == '[' :
            stack.append(']')
        else :
            x = 0
            if stack :
                k = stack.pop()
                while stack and k != ')' and k != ']' :
                    x += k
                    k = stack.pop()
                if k != p :
                    print(0)
                    return
            else :
                print(0)
                return
            stack.append((x if x != 0 else 1) * (2 if k == ')' else 3))
    for s in stack :
        if s == ')' or s == ']' :
            res = 0
            break
        res += s
    print(res)
    return

if __name__ == '__main__' :
    solve()