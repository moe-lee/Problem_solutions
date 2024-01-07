import math
def solve() :
    t = int(input())
    for i in range(t) :
        x, y = tuple(map(lambda x : int(x), input().split()))
        
        w_right_year = 1
        jmp_cnt = 2
        x += 1
        y -= 1
        while (x + w_right_year - 1) not in [y, y - (w_right_year - 1), y - w_right_year, y - (w_right_year+1)] and (x + w_right_year) not in [y, y - (w_right_year - 1), y - w_right_year, y - (w_right_year+1)] and (x + w_right_year + 1) not in [y, y - (w_right_year - 1), y - w_right_year, y - (w_right_year+1)] :
            x += w_right_year + 1
            y -= w_right_year + 1
            jmp_cnt += 2
            w_right_year += 1
        
        if x + w_right_year == y or x + w_right_year - 1 == y or x + w_right_year + 1 == y :
            jmp_cnt += 1
        else :
            jmp_cnt +=2
        
        print(jmp_cnt)


def solve2():
    t = int(input())
    for i in range(t) :
        x, y = tuple(map(lambda x : int(x), input().split()))
        total_warping_times = 0
        n = math.floor(-1 + math.sqrt(1 + (y - x)))
        p = x + (n + 1) * (n + 2) / 2
        q = y - (n + 1) * (n + 2) / 2
        if p < q :
            total_warping_times = 2 * n + 3
        elif p >= q + n + 1 :
            total_warping_times = 2 * n + 1
        else :
            total_warping_times = 2 * n + 2
        print(total_warping_times)
solve2()