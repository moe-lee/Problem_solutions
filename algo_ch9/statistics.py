import sys
n = int(sys.stdin.readline())
array = []
for i in range(n) :
    array.append(int(sys.stdin.readline()))
    
array = sorted(array)
fa = []
i, j = 0, 0
while i < n :
    j = i
    while j < n and array[j] == array[i] : j += 1
    fa.append([array[i], j - i])
    i = j

fa= sorted(fa, key=lambda x : x[1])
i = 0
while fa[i][1] != fa[-1][1] : i+=1
fa = fa[i:]

print(int(abs(sum(array) / n) + 0.5) * (1 if sum(array) > 0 else -1))
print(array[n//2])
print(fa[1%len(fa)][0])
print(array[n-1] - array[0])