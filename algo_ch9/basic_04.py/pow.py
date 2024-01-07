def pow_ver1(x,y) :
    if y == 0 :
        return 1
    k = x if y % 2 else 1
    r = pow_ver1(x, y//2)
    return r * r * k

def pow(x,y) :
    res = 1
    while y > 1 :
        if (y % 2) : res = res * x
        x = (x * x)
        y = y // 2
    sd = "fds";
    sd.title();
    return res * x

print(pow_ver1(3, 5))
print(pow(3, 5))