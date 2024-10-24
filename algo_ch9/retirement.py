import sys

# def solve2() :
#     N = int(input())
#     counselings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#     for _ in range(N) :
#         t, p = map(int, sys.stdin.readline().split())
#         counselings.append([t, p, 0])

#     for i in range(0, N) :
#         for j in range()
    
# def solve() :
#     N = int(input())
#     counselings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#     cache = {}
#     def DFS(day) :
#         max_cost = 0
#         for pred_day in range(day-1, -1, -1) :
#             if counselings[pred_day][0] + pred_day - 1 < day :
#                 if pred_day not in cache :
#                     cache[pred_day] = DFS(pred_day)
#                 max_cost = max(max_cost, cache[pred_day])
#         if day < N :
#             max_cost += counselings[day][1]
#         return max_cost
    
#     print(DFS(N))
#     return
# solve()

def solve3() :
    N = int(sys.stdin.readline())
    schedule = [tuple(map(int ,sys.stdin.readline().split())) for _ in range(N)]
    DP = [0] * (N+1)
    for i in range(N+1) :
        if i > 0 : DP[i] = max(DP[i], DP[i-1])
        if i < N and i + schedule[i][0] <= N :
            DP[i + schedule[i][0]] = max(DP[i + schedule[i][0]], DP[i] + schedule[i][1])
    print(DP[N])
solve3()

'''

7
3 22
5 20
1 10
1 20
2 15
4 40
2 200
'''