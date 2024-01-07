def solve():
    k_map = [0, 1, 2, 3]
    n, r, c = tuple(map(lambda x : int(x), input().split()))
    i = 1
    num_of_trav = 0
    col_p, row_p = 0, 0
    
    while n - i > 0 :
        col_p = c // (2 ** (n-i))
        row_p = r // (2 ** (n-i))
    
        k = k_map[row_p * 2 + col_p]
        num_of_trav += k * ((2 ** (n-i)) ** 2)
    
        c = c - (2 ** (n-i)) if c - (2 ** (n-i)) >= 0 else c
        r = r - (2 ** (n-i)) if r - (2 ** (n-i)) >= 0 else r
        i+=1
    
    num_of_trav += k_map[r * 2 + c]
    print(num_of_trav)

solve()