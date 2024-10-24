def check(string) :
    stack = []
    for p in string :
        if p == '(' :
            stack.append(')')
        elif p == '[' :
            stack.append(']')
        elif p == '{' :
            stack.append('}')
        elif p == '<' :
            stack.append('>')
        else :
            if not stack or stack.pop() != p:
                return 0
    return 1 if not stack else 0

for test_case in range(1, 11) :
    n = int(input())
    string = input()
    print('#'+str(test_case), check(string))