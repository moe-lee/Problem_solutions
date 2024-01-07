import math

def solve() :
    t = int(input())
    for i in range(t) :
        x1, y1, r1, x2, y2, r2 = tuple(map(lambda x : int(x), input().split()))
        distance = math.sqrt(((x2-x1) ** 2 + (y2-y1) ** 2))
        r1, r2 = max(r1, r2), min(r1, r2)
        if (x1 == x2 and y1 == y2) :
            if r1 == r2 :
                print(-1)
            else :
                print(0)
        else :
            if( distance > (r1 + r2)) :
                print(0)
            elif(distance == (r1 + r2)) :
                print(1)
            else :
                if(max(r1, r2) == min(r1, r2) + distance) :
                    print(1)
                elif(max(r1, r2)  > distance + min(r1, r2)) :
                    print(0)
                else :
                    print(2)
    
def main() :
    solve()
    
main()