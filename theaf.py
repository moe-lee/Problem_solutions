import sys

def solve() :
    T = int(input())
    for _ in range(T) :
        N, M, K = tuple(map(int, sys.stdin.readline().split()))
        houses = list(map(int, sys.stdin.readline().split()))
        cnt = 0
        money = sum(houses[:M])
        if(money < K) : cnt += 1
        tail, head = 0, M
        while(N != M and head < N + M - 1) :
            money = money - houses[tail % N] + houses[head % N]
            if(money < K) : cnt += 1
            tail += 1
            head += 1
        print(cnt)
    
    return

if __name__ == '__main__' :
    solve()