import sys
import heapq
# 일반적인 DP 접근법을 위해 입력을 선형적으로 적용시켜보기
def solve() :
    N = int(sys.stdin.readline())
    wires = [0 for _ in range(501)]
    cross_info = [[0, []] for _ in range(501)]
    for _ in range(N) : # 100회
        u, v = map(int, sys.stdin.readline().split())
        wires[u] = v
    pq = []
    for i in range(1, 501) : # 2.5e+5회
        if wires[i] != 0 :
            cnt = 0
            for j in range(1, 501) :
                if wires[j] != 0 and (i - j) * (wires[i] - wires[j]) < 0 :
                    cnt += 1
                    cross_info[i][1].append(j)
            cross_info[i][0] = cnt
            heapq.heappush(pq, (-cnt, i))
    ans = 0
    removed = [False] * (501)
    while pq :
        cnt, cur_port = heapq.heappop(pq)
        cnt = -cnt
        if cross_info[cur_port][0] == cnt and cross_info[cur_port][0] > 0 :
            ans += 1
            removed[cur_port] = True
            for np in cross_info[cur_port][1] :
                if not removed[np] :
                    cross_info[np][0] -= 1
                    heapq.heappush(pq, (-1 * cross_info[np][0], np))
    print(ans)
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