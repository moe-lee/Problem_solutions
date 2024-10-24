for test_case in range(1, 11) :
    tokens = input().split()
    n, string = int(tokens[0]), list(tokens[1])
    stack = []
    for i in range(0, n) :
        char = string[i]
        if stack and stack[-1] == char :
            stack.pop()
        else :
            stack.append(char)
    print('#'+str(test_case)+" ", end="")
    for c in stack:
        print(c, end='')
    print()