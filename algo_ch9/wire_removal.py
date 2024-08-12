import sys
from collections import deque
from collections import defaultdict
# graph.순회도 아니고.. Longest Increasing Subsequence algorithm을 적용해야함.
def solve() :
    ## 어떻게 적용할 수 있을까..
    # 많이 겹치는 전깃줄을 제거해보며 가장 적은 수를 센다 -> 하나씩 전깃줄을 배치하며 겹치지 않고 둘 수 있는 최고 값을 찾는다.
    N = int(sys.stdin.readline())
    wires = [list(map(int ,sys.stdin.readline().split())) for _ in range(N)]
    wires.sort(key=lambda x : x[0])
    ans = [1] * (N)
    for k in range(1, N) :
        for j in range(0, k) :
            if wires[k][1] > wires[j][1] :
                ans[k] = max(ans[k], ans[j] + 1)
    print(N-max(ans))
    return
solve()


'''
5
1 7
2 1
3 2
4 3
5 4
-> pass

5
1 5
2 4
3 3
4 2
5 1
-> pass

8
1 3
4 2
3 5
6 4
5 7
8 6
7 9
10 8
-> pass

5
3 1
1 2
5 3
2 4
4 5

'''