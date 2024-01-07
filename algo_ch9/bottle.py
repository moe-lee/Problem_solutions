def solve() :
    n, k = tuple(map(lambda x : int(x), input().split()))
    adj_bottles = [0] * 32;
    
    ab_index = 0
    while n > 0 :
        mask = 1;
        i = 0
        while i < 32 and mask << i <= n : i+=1
        i -= 1
        adj_bottles[ab_index] = mask << i
        ab_index += 1
        n -= (mask << i)
        
    additional_bottle = 0
    for i in range(k, ab_index) :
        additional_bottle += adj_bottles[i]
    if additional_bottle :
        print(adj_bottles[k-1] - additional_bottle)
    else : print(0)
    
solve()