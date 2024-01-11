import sys
n = int(sys.stdin.readline())
wine = [0] * (n+1)
for i in range(1, len(wine)) :
    wine[i] = int(sys.stdin.readline())

max_wines = [[0,0], [wine[1], 0]]
for i in range(2, n+1) :
    wine_step = [0, 0]
    wine_step[0] = max(max_wines[i-1][1], max_wines[i-2][1] + wine[i-1]) + wine[i]
    wine_step[1] = max(max_wines[i-1][0], max_wines[i-1][1])
    max_wines.append(wine_step)

print(max(max_wines[n][0], max_wines[n][1]))
