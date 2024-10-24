import sys
K, N = map(int, sys.stdin.readline().split())
wires = [int(sys.stdin.readline().strip()) for _ in range(K)]
left, right = 1, (2**31)
while left < right :
    mid = (left + right) // 2
    wire_cnt = 0
    for wire in wires :
        if wire_cnt > N : break
        wire_cnt += wire // mid
    if wire_cnt >= N :
        left = mid + 1
    else :
        right = mid
print(left - 1)

'''
3 3 
11
9
9

1 1
2147483647

3 5
15
15
8
'''