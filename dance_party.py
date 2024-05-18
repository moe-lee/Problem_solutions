import sys
# N 

def getProperPairs(men, women, mi, wi) :
    num_of_pairs = 0
    while mi < len(men) and wi >= 0 and men[mi] < 0 and women[wi] > 0 :
        if abs(men[mi]) > abs(women[wi]) :
            num_of_pairs += 1
            mi += 1
            wi -= 1
        elif abs(men[mi]) <= abs(women[wi]) :
            wi -= 1
    return num_of_pairs

def solve() :
    N = int(sys.stdin.readline())
    men = list(map(int, sys.stdin.readline().split()))
    women = list(map(int, sys.stdin.readline().split()))
    men.sort()
    women.sort()

    num_of_pairs = getProperPairs(men, women, 0, N-1)
    num_of_pairs += getProperPairs(women, men, 0, N-1)
    print(num_of_pairs)
    
solve()
