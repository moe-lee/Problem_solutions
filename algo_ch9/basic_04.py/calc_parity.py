def calcParity(s) :
    s = s ^ (s>>8)
    s = s ^ (s>>4)
    s = s ^ (s>>2)
    s = s ^ (s>>1)
    return s & 0x01

parity_table = [calcParity(i) for i in range(0, 2**16)]

def getParityBit(x) :
    return parity_table[x >> 48] ^ parity_table[(x >> 32) & 0xffff] ^ parity_table[(x >> 16) & 0xffff] ^ parity_table[x & 0xffff]

if __name__ == "__main__" :
    print(getParityBit(0b10001000))