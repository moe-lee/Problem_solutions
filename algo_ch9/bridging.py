def solve():
    t = int(input())
    for i in range(t) :
        N, M = tuple(map(lambda x : int(x), input().split()))
        denomi = 1
        numer = 1
        denomi_start = max(M-N+1, N+1)
        numer_end = min(M-N, N)
        for k in range(denomi_start, M+1) :
            denomi *= k
        for k in range(1, numer_end + 1) :
            numer *= k
        
        print(denomi // numer)

def main() :
    solve()

main()