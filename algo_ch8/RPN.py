from collections import deque as stack

def calculate(r1, op, r2) :
    return eval(str(r1)+op+str(r2))

def s_to_i(s) :
    i = 0
    sign = 1
    if s[i] == '-' :
        sign = -1
        i += 1
    mid_sum = 0
    while i < len(s) :
        if s[i].isnumeric() :
            mid_sum = mid_sum * 10 + int(s[i])
        i+=1
    return sign * mid_sum

def cal_rpn(ex) :
    operations = {
        "x" : lambda a, b : a * b,
        "+" : lambda a, b : a + b,
        "-" : lambda a, b : a - b,
        "/" : lambda a, b : a // b
    }
    operand = stack()
    idx1, idx2 = 0, 0
    while idx1 < len(ex):
        idx2 = idx1
        while idx2 < len(ex) and ex[idx2] != ',' : idx2 +=1
        if ex[idx2-1].isnumeric() :
            operand.append(s_to_i(ex[idx1:idx2]))
        else :
            orand1 = operand.pop()
            orand2 = operand.pop()
            operand.append(operations[ex[idx2-1]](orand2, orand1))
        idx1 = idx2 + 1
    return operand.pop()

if __name__ == "__main__" :
    print(cal_rpn("-10, 20, x, -4, 20, +, -"))
    