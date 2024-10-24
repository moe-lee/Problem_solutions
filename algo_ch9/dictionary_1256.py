import sys


def solve() :
    N, M, K = map(int, sys.stdin.readline().split())
    DP = [[0 for _ in range(N+M + 1)] for _ in range(N + 1)]
    if K == 1 :
        print('a' * N + 'z' * M)
        return
    # M이나 N이 0인 경우도 생각? X. 항상 1 이상.
    for i in range(1, M+1) : DP[1][i] = 1
    for i in range(2, N+1) : # a가 i개 있고, 시작위치가 t인 경우
        for T in range(M+i-1, i, -1) : # 제일 뒤에 a가 i개 연속 -> 단 1개임.
            for t in range(T - 1, -1, -1) :
                DP[i][T] += DP[i-1][t]
        DP[i][i] = 1
        
    def execute(length, N, K) :
        if length == 6 :
            pass
        res = ''
        if K == 1:
            res = 'a' * N + 'z' * (length - N)
            return (res, N, 0)
        comb_acc = 1
        prev_row_col = (0, 0)
        cur_cotained_a = 0
        for i in range(1, N+1) :
            for j in range((length - N + i) - 1, 0, -1) :
                prev_row_col = (i, j)
                comb_acc += DP[i][j]
                if comb_acc == K :
                    res += 'a' * (N - i) + 'z' * ((length - N) - (j - i)) + 'a' + 'z' * (j - i) + 'a' * (i-1)
                    K -= comb_acc
                    cur_cotained_a = N
                    return (res, cur_cotained_a, K)
                elif comb_acc > K :
                    # 현재 접두사인 순서에 K번째 문장이 존재.
                    res += 'a' * (N - i) + 'z' * ((length - N) - (j - i)) + 'a' # 접두사 구성
                    cur_cotained_a = (N - i + 1)
                    K -= (comb_acc - DP[prev_row_col[0]][prev_row_col[1]])
                    # 이전에 더해진게 같은 행의 값인지 다른 행의 값인지 확인하기 번거로움.
                    return (res, cur_cotained_a, K)
        return (None, None, None)
    res, cur_cotained_a = '', 0
    length = N+M
    while K>0 :
        pres, pa, K = execute(length, N - cur_cotained_a, K)
        if(pres == None) :
            print(-1)
            return
        res += pres
        cur_cotained_a += pa
        length = N+M - len(res)
        if cur_cotained_a == N :
            res += 'z' * (N+M - len(res))
            break
    print(res)
    # print(K)
    # print(cur_cotained_a)
solve()


'''
3 3 k
aaazzz
aazazz
aazzaz
aazzza

azaazz
azazaz
azazza

azza az
azza za

azzzaa

zaaazz
zaazaz
zaazza
zazaaz
zazaza
zazzaa

zzaaaz
zzaaza
zzazaa
zzzaaa

갯수는 20개
'''