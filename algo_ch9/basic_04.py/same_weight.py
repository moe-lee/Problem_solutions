def find_same_weight(x) :
    i = 1
    while (x>>i & 1) == (x>>(i-1) & 1) :
        x = x>>1
    return x ^ (0x03<<(i-1))

def find_same_weight2(x) :
    t = x
    if x & 1 :
        t = ~t
    t = t &~(t-1)
    t = t | (t>>1)
    return x ^ t

print(find_same_weight2(92))
