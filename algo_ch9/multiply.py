import sys
sys.setrecursionlimit(10**5)
memo = {}
def mul(A, B, C) :
    if B == 1 :
        return A % C
    muls = 1
    if B % 2 == 1 :
        muls *= A
        B -= 1
    if B // 2 not in memo :
        memo[B // 2] = mul(A, B//2, C) % C
    muls *= (memo[B // 2] ** 2) % C
    return muls % C
a, b, c = map(int, sys.stdin.readline().split())
print(mul(a, b, c))