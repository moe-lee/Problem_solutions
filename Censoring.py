def solve():
    s = input()
    t = input()
    stack = [] # 문자 + 부분길이
    for c in s :
        if not stack :
            if c == t[0] :
                stack.append([c, 1])
            else :
                stack.append([c, 0])
        else :
            if c == t[stack[-1][1]] :
                stack.append([c, stack[-1][1] + 1])
            else :
                tmp = stack[-1][1] - 1
                while tmp > 0 :
                    if t[tmp] != c :
                        tmp -= 1
                    else :
                        s = tmp - 1
                        while s >= 0:
                            if stack[-1 * (tmp - s)][0] != t[s] :
                                break
                            s -= 1
                        if s >= 0 :
                            tmp -= 1
                        else :
                            for i in range(1, tmp + 1) :
                                stack[-1 * i][1] = tmp + 1 - i
                            break
                stack.append([c, tmp + 1])
        if stack[-1][1] == len(t) :
            for _ in range(len(t)) : stack.pop()
    for i in range(len(stack)) :
        print(stack[i][0], end='')
    return

solve()