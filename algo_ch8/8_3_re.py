from collections import deque as stack

def valid_form(s) :
    b_stack= stack()
    brackets = { ')' : '(', '}' : '{', ']' : '[' }
    b_key = list(brackets.keys())
    b_vals = list(brackets.values())
    for i in s :
        if(i in b_vals) : b_stack.append(i)
        if(i in b_key) :
            if(brackets[i] != b_stack.pop()) : return False
    return not(b_stack)

if __name__ == "__main__" :
    s = "([]){()[[}"
    print(valid_form(s))
