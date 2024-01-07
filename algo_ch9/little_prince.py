import math

def solve():
    t = int(input())
    for tr in range(t) :
        sx, sy, ax, ay = tuple(map(lambda x : int(x), input().split()))
        access_escape_count = 0
        n = int(input())
        for i in range(n) :
            x, y, r = tuple(map(lambda x : int(x), input().split()))
            dist_to_start = math.sqrt((sx - x) ** 2 + (sy - y) ** 2)
            dist_to_arrive = math.sqrt((ax - x) ** 2 + (ay - y) ** 2)
            if(not dist_to_arrive < r and dist_to_start < r) or (dist_to_arrive < r and not dist_to_start < r) :
                access_escape_count += 1
        print(access_escape_count)
        
def main():
    solve()

main()