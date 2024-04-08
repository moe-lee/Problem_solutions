import sys
import copy
def solve() :
    N, P = tuple(map(int, sys.stdin.readline().split()))
    strings = [copy.deepcopy([]) for _ in range(7)]
    movement = 0
    for _ in range(N) :
        s, p = tuple(map(int, sys.stdin.readline().split()))
        while(strings[s] and strings[s][-1] > p) :
            strings[s].pop()
            movement += 1
        if not strings[s] or strings[s][-1] != p :
            strings[s].append(p)
            movement += 1
    print(movement)
    return


if __name__ == '__main__' :
    solve()