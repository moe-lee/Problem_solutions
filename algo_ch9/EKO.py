import sys
N,M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 0, 10 ** 9
while left < right :
    mid = (left + right) // 2
    cutted = 0
    for tree in trees :
        if cutted > M : break
        cutted += max(0, tree - mid)
    if cutted >= M : 
        left = mid + 1
    else : right = mid - 1
print(right)

'''
5 4
1 5 1 5 1

4 2
5 3 4 

5 2
1 5 6 5
'''