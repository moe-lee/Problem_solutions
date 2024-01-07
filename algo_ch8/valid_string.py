from collections import deque as stack

def check_valid_string(s) :
    brackets = { ')':'(', '}':'{', ']':'['}
    closes = brackets.keys()
    bracket_stack = stack()
    for c in s :
        if c == '(' or c == '{' or c == '[' : bracket_stack.append(c)
        elif c in closes :
            if bracket_stack.pop() != brackets[c] : return False
    return not(bracket_stack)

if __name__ == "__main__" :
    s = "([{[{[()()]}]}])[]"
    print(check_valid_string(s))