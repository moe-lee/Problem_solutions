def pow(x, y) :
    '''
    x ^ 15 = (((x * x) * (x * x) * (x * x) * (x * x) * (x * x) * (x * x)) * (x * x)) * x
    '''
    if y < 0 :
        y = abs(y)
        x = 1.0 / x
    res = 1
    while y :
        if y & 1 :
            res *= x
        x *= x
        y >>= 1
    return res

print(pow(2,-3))