def climbingStairs(n) :
    list = [0 for _ in range(n+1)]
    list[0] = 1
    list[1] = 1
    for i in range(2, n+1) :
        list[i] = list[i-1] + list[i-2]
    print(sum(list[n]))
    return

climbingStairs(n=3)