import sys

def solve() :
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    result = 0
    for i, s in enumerate(l) :
        lv, rv = 0, n - 1
        while(lv < rv) :
            if(l[lv] + l[rv] == s) :
                result += 1
                break
            elif (i == rv or l[lv] + l[rv] > s) :
                rv -= 1
            elif (i == lv or l[lv] + l[rv] < s) :
                lv += 1
    
    return result

if __name__ == '__main__' :
    print(solve())
