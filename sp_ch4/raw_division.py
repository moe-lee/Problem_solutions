def division_in_low_level(x, y) :
    quotient = 0
    power = 32
    while x >= y :
        if x >= y << power :
            x = x - (y << power)
            quotient |= 1 << power
        power >>= 1
    
    return quotient, x

print(division_in_low_level(35, 6))