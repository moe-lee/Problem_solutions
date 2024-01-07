def solve():
    package_min = 1001
    min_per_string = 1001
    m_r = 0
    
    n, m = tuple(map(lambda x : int(x), input().split()))
    for i in range(m) :
        p, s = tuple(map(lambda x: int(x), input().split()))
        package_min = min(package_min, p)
        min_per_string = min(min_per_string, s)
    
    package_min = min(package_min, min_per_string * 6)
    
    m_r += (n // 6) * package_min
    m_r += min(package_min, (n % 6) * min_per_string)
    print(m_r)

solve()