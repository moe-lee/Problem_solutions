import sys

def solve() :
    N = int(input())
    buildings = reversed(list(map(int, sys.stdin.readline().split())))
    stack = []
    res = [0] * N
    for cur_pos, cur_height in enumerate(buildings) :
        while stack and stack[-1][1] <= cur_height:
            pre_pos, _ = stack.pop()
            res[pre_pos] = cur_pos
        stack.append((cur_pos, cur_height))
    res = reversed(list(map(lambda x : (N - x)%N, res)))
    for i in res :
        print(i, end=" ")
    return

if __name__ == '__main__' :
    solve()