import math
import heapq
T = int(input())
def getFee(p1, p2, E) :
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) * E

for test_case in range(1, T+1) :
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    tot_fee = 0
    num_of_groups = N + 1
    included = [False] * (N)
    pq = [(0, 0)]
    while num_of_groups > 1 :
        fee, node = heapq.heappop(pq)
        if not included[node] :
            included[node] = True
            num_of_groups -= 1
            tot_fee += fee
            for i in range(0, N) :
                if i == node or included[i]: continue
                con_fee = getFee((X[node], Y[node]), (X[i], Y[i]), E)
                heapq.heappush(pq, (con_fee, i))
    print('#'+str(test_case), int(tot_fee+0.5))