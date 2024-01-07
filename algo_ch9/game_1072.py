import math

def solve1() :
    x, y = tuple(map(lambda x : int(x), input().split()))
    k = 0
    z = math.floor((y / x) * 100)
    while math.floor((((y + k)/ (x + k)) * 100)) == z: k+=1
    print(k)
    

def solve() :
    x, y = tuple(map(lambda x : int(x), input().split()))
    z = math.floor(((y / x) * 100))
    if z >= 99 : 
        print(-1)
        return
    k = math.ceil((x**2) / (99 * x - 100 * y))
    l = 0
    while(l < k) :
        m = int((k + l) / 2)
        if(math.floor((((y + m) / (x + m)) * 100)) == z) :
            l = m + 1
        else :
            k = m
    print(math.ceil(k))
    
solve()