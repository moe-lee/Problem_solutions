import sys

def solve() :
    N, K = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    l, r = 0, N - 1
    min_d = sys.maxsize
    dcnt = 0
    while l < r:
        dist = abs(K - (nums[l] + nums[r]))
        if(dist == min_d) :
            dcnt += 1
        elif(dist < min_d) :
            dcnt = 1
            min_d = dist
        
        if(K > (nums[l] + nums[r])) :
            l += 1
        else :
            r -= 1
    print(dcnt)

if __name__ == '__main__' :
    t = int(input())
    while t :
        solve()
        t -= 1
    