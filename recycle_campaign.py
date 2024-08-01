import sys

def solve() :
    N, X = map(int, sys.stdin.readline().split())
    cosmetics = list(map(int, sys.stdin.readline().split()))
    cosmetics.sort()
    l, r = 0, N-1
    full_bottles = 0
    bottles_too_shallow = 0
    while l <= r :
        if l == r :
            if cosmetics[r] == X :
                full_bottles += 1
            else :
                bottles_too_shallow += 1
            break
        elif cosmetics[r] >= X :
            full_bottles += 1
            r -= 1
        elif cosmetics[r] + cosmetics[l] >= X / 2 :
            full_bottles += 1
            l += 1
            r -= 1
        else :
            bottles_too_shallow += 1
            l += 1
    
    full_bottles += (bottles_too_shallow) // 3
    print(full_bottles)

solve()