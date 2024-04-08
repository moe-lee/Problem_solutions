def add(x, y) :
    while y > 0 :
        carry = x & y
        x ^= y
        y = carry << 1
    return x

def multiply(x, y) :
    res = 0
    while y > 0 :
        if y & 1 : res = add(res, x)
        x,y = x << 1, y >> 1
    return res

if __name__  == "__main__" :
    print(multiply(7, 5))