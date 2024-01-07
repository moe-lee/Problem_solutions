def add(x, y) :
    c = 0
    while y :
        c = x & y
        x = x ^ y
        y = c << 1
    return x

def multiply(x, y) :
    res = 0
    while y :
        res = res << 1
        if(y & 1) :
            res = add(res, x)
        y = y >> 1
    return res

print(multiply(30, 5))