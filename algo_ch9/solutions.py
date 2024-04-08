import sys

def solve() : # the application form of two sum
    n = int(sys.stdin.readline())
    solutions = list(map(int, sys.stdin.readline().split()))
    l,r = 0, n - 1
    res = [1000000000, 1000000000]
    while( l < r ) :
        if(abs(solutions[l] + solutions[r]) < abs(res[0] + res[1])) :
            res[0], res[1] = solutions[l], solutions[r]
            if(res[0] + res[1] == 0) : 
                break
        if(abs(solutions[l]) > abs(solutions[r])) :
            l += 1
        elif(abs(solutions[l]) < abs(solutions[r])) :
            r -= 1
    
    print(res[0], res[1])
    return


if __name__ == '__main__' :
    solve()