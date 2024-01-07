def solve() :
    n = int(input())
    A = sorted(list(map(lambda x : int(x), input().split())), reverse=True)
    B = sorted(list(map(lambda x : int(x), input().split())))
    S = 0
    for i in range(n) :
        S += A[i] * B[i]
    print(S)
solve()