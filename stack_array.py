def solve() :
    N = int(input())
    t = []
    stack = [1]
    i = 2
    j = 0
    res = '+'
    
    for _ in range(N) :
        t.append(int(input()))
    
    while j < N :
        if(stack and stack[-1] == t[j]) :
            stack.pop()
            res += '-'
            j += 1
        elif (not stack or stack[-1] < t[j]) :
            stack.append(i)
            i += 1
            res += '+'
        else :
            print('NO')
            return
    for c in res :
        print(c)


if __name__ == '__main__' :
    solve()