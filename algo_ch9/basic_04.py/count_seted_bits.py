def countBits(x):
    count = 0
    while x > 0 :
        count += (x & 0x01)
        x = x >> 1
    return count

