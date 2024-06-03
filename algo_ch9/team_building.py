import sys

def solve():
    N = int(sys.stdin.readline())
    capability = list(map(int, sys.stdin.readline().split()))
    
    lower = 0
    higher = N-1
    max_team_capability = 0
    while lower < higher :
        max_team_capability = max(max_team_capability, (higher - lower - 1) * min(capability[higher], capability[lower]))
        if capability[lower] < capability[higher] :
            lower += 1
        elif capability[higher] < capability[lower] :
            higher -= 1
        else :
            if lower < higher - 2 and capability[lower + 1] > capability[higher - 1] :
                lower += 1
            else :
                higher -= 1
    print(max_team_capability)
    return


solve()