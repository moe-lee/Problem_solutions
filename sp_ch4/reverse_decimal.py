def rd(x) :
    res = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x :
        res = res * 10 + x % 10
        x = x // 10
    return sign * res

print(rd(-20))