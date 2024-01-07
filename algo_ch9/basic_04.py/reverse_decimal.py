def reverse(x) :
    sign = x // abs(x)
    x = abs(x)
    m = 0
    while x > 0 :
        m = m * 10 + (x % 10)
        x = x // 10
    return m * sign

if __name__ == "__main__" :
    print(reverse(-1011324))