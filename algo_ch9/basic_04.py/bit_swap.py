def swapBit(x, i, j) :
    if(x >> i ^ x >> j) & 0x01 :
        return (x ^ (0x01 << i | 0x01 << j))
    return x


if __name__ == "__main__" :
    print(bin(swapBit(0b100110, 1,4)))