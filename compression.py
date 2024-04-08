def solve():
    s = input()
    stack = []
    length = 0
    # 문자와 부분의 길이
    for p in s :
        if p != ')' :
            stack.append([p, 1])
        else :
            t = stack.pop()
            sublen = 0
            while(t[0] != '(') :
                sublen += t[1]
                t = stack.pop()
            t = stack.pop()
            stack.append(['*', sublen * (ord(t[0]) - 0x30)])
    for i in stack :
        length += i[1]
    print(length)
    return

if __name__ == '__main__' :
    solve()