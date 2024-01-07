from collections import deque as stack

def cal_rpn(ex) :
    tokens = ex.split(',')
    operations = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '/' : lambda x, y : x // y,
        'x' : lambda x, y : x * y
    }
    operands = stack()
    
    for e in tokens :
        e = e.strip()
        if e[-1].isdigit() :
            operands.append(int(e))
        else :
            op1 = operands.pop()
            op2 = operands.pop()
            operands.append(operations[e](op2,op1))
    
    return operands.pop()

def cal_pn(ex) :
    acc = None
    operators = stack()
    operate = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '/' : lambda x, y : x // y,
        'x' : lambda x, y : x * y
    }
    tokens = list(map(lambda sc: sc.strip(), ex.split(',')))
    for i in tokens :
        if i[-1].isdigit() :
            if acc is None : acc = int(i)
            else : acc = operate[operators.pop()](acc, int(i))
        else :
            operators.append(i)
    return acc

if __name__ == "__main__" :
    print(cal_pn("+, -, -7, 2, 5"))