priority = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}
def transform(string) :
    exp = []
    stack = []
    for s in string :
        if s.isdigit() :
            exp.append(s)
        else :
            if s == '(' or not stack or (stack and priority[stack[-1]] <= priority[s]) :
                stack.append(s)
            else :
                while stack and stack[-1] != '(' :
                    exp.append(stack.pop())
                if s == ')' :
                    stack.pop()
                else :
                    stack.append(s)
    while stack : exp.append(stack.pop())
    return exp

def calc(postfix) :
    stack = []
    operation = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '*' : lambda x, y : x * y,
        '/' : lambda x, y : x // y
    }
    
    for n in postfix :
        if n.isdigit() :
            stack.append(int(n))
        else :
            x, y = stack.pop(), stack.pop()
            stack.append(operation[n](y, x))
    return stack.pop()

for test_case in range(1, 11) :
    N = int(input())
    string = input()
    print('#'+str(test_case), calc(transform(string)))

'''
15
1*3+2-(3+6/4-2)
'''