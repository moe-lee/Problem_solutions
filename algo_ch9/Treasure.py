import sys

def solve() :
    i, w = map(int, sys.stdin.readline().split())
    items = []
    for _ in range(i) : items.append(tuple(map(int, sys.stdin.readline().split())))
    DP = [-1] * (w+1)
    DP[0] = 0
    for i in range(len(items)) :
        value, weight = items[i]
        for i in range(w, -1, -1) :
            if i + weight <= w and DP[i] != -1 :
                DP[i+weight] = max(DP[i+weight], DP[i] + value)
    print(max(DP))

def execute() :
    T = int(sys.stdin.readline())
    for _ in range(T) : solve()

execute()