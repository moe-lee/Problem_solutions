from bit_swap import swapBit

def calcPartialReversedBits(x) :
    for i in range(0, 8) :
        x = swapBit(x, i, 15-i)
    return x

reversed_table = [calcPartialReversedBits(x) for x in range(0, 2**16)]

def getReverseBinary(x) :
    return reversed_table[x & 0xffff] << 48 | reversed_table[(x>>16) & 0xffff] << 32 | reversed_table[(x>>32) & 0xffff] << 16 | reversed_table[(x>>48) & 0xffff]

print(bin(getReverseBinary(0b1110000000000001)))