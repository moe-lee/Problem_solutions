import sys
from collections import deque

def BFS(start_row, start_col, fuel, grid, dest_set, passenger_in) : # 반환값 -> 현재 도착지(row, col), 현재 연료량, 성공여부
    if(start_row, start_col) in dest_set :
        return (start_row, start_col, fuel, True) # 시작 위치가 목적지와 같다면, 바로 리턴
    
    taxi = deque()
    taxi.append((start_row, start_col))
    fuel_gauge = fuel
    steps = ((-1, 0), (0, -1), (0, 1), (1, 0)) # 탐색 방향 상, 좌, 우, 하
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    visited[start_row][start_col] = True
    psg_queue = []
    while(fuel_gauge > 0) :
        move_to = deque() # 다음 칸 저장
        for cr, cc in taxi : 
            for sr, sc in steps : # 현재 택시 위치들에 대해 이동방향을 순서대로 적용           
                nr, nc, nf = cr + sr, cc + sc, fuel_gauge - 1
                if(1<=nr<len(grid) and 1<=nc<len(grid)) and grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if(nr, nc) in dest_set :
                        fuel_remained = nf
                        if passenger_in : fuel_remained += (fuel - nf) * 2 # 손님을 도착지에 데려다 준 경우 연료 채움
                        psg_queue.append((nr, nc, fuel_remained, True))
                    else :
                        move_to.append((nr, nc))
        if psg_queue :
            psg_queue.sort()
            return psg_queue[0]
        fuel_gauge -= 1
        taxi = move_to
    return (-1, -1, 0, False) # 택시가 중간에 멈춘경우

def solve() :
    N, M, F = map(int, sys.stdin.readline().split())
    grid = [[0 for _ in range(N+1)]]
    for _ in range(N) :
        tmp = [0]
        tmp.extend(list(map(int, sys.stdin.readline().split())))
        grid.append(tmp)
    taxi_row, taxi_col = map(int, sys.stdin.readline().split())
    passengers = {} # 승객 위치 : 도착지
    for _ in range(M) :
        pr, pc, qr, qc = map(int, sys.stdin.readline().split())
        passengers[(pr, pc)] = (qr, qc)
    
    fuel = F
    arrival_cnt = 0
    driving = True
    passenger_in = False
    target_set = passengers
    while(driving) :
        # 순회 방법 : double queue based bfs
        if not passenger_in : # 손님 태우러 갈 때
            dr, dc, fuels, hit = BFS(taxi_row, taxi_col, fuel, grid, target_set, False)
            if hit and fuels > 0 : # 손님을 태우고 연료량이 0보다 큼 -> 이행 가능
                passenger_in = True
                taxi_row, taxi_col, fuel = dr, dc, fuels
                target_set = {passengers[(taxi_row, taxi_col)]} # 택시 목표지는 손님 도착지로 설정
                passengers.pop((dr, dc)) # 태운 손님을 제거해야함 => 무한 루프 가능성
            # 손님을 못 태우거나 태웠어도 연료가 0이면, 운행 불가. 종료
            else:
                driving = False
        else : # 손님 태우고 운행할 때
            dr, dc, fuels, hit = BFS(taxi_row, taxi_col, fuel, grid, target_set, True)
            if hit : # 성공한 경우 = 연료가 남아있음(채워주기 때문). 실패한 경우 = 연료가 바닥 -> 운행 종료
                arrival_cnt += 1
                taxi_row, taxi_col, fuel = dr, dc, fuels
                target_set = passengers # 목표지를 다시 승객들로 변경
                passenger_in = False
                if arrival_cnt == M :
                    break
            else :
                driving = False
    print(fuel if (arrival_cnt == M) else -1)
solve()

'''
test #1: 손님을 태웠지만 연료가 0
3 1 2
0 0 0
0 0 0
0 0 0
1 1
1 3 3 1
ans = -1

test #2: 벽에 막혀 갈 수 없음.
3 2 100
0 1 0
0 1 1
0 0 0
1 1
2 1 3 1
4 1 1 3
ans = -1

test #3 : 탐색 우선순위
5 2 20
0 1 1 1 0
0 0 0 0 0
0 1 0 1 0
0 1 0 1 1
0 1 0 0 0
4 3
2 1 5 1
2 5 3 5
ans = 13

test #4 : 모두 완료한 뒤 연료 채우기 전 연료가 0이 된 경우
3 1 2
0 0 0
0 0 0
0 0 0
1 1
1 2 1 3
ans = 2



3 1 500
0 1 0
1 0 0
0 0 0
1 1
1 3 3 3

3 1 500
0 1 0
1 0 0
0 0 0
1 3
1 1 3 3

3 1 500
0 1 0
1 0 0
0 0 0
1 3
3 3 1 1

test #5 : 탐색 우선순위 (왼쪽 아래 vs 2칸 오른쪽)
5 2 10
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
4 2
5 1 1 1
4 4 5 4


4 2 10
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 2
1 1 1 4
1 4 1 1
ans = 15

3 9 10
0 0 0
0 0 0
0 0 0
2 2
2 2 1 1
1 1 1 2
1 2 3 3
3 3 3 2
3 2 3 1
3 1 1 3
1 3 2 1
2 1 2 3
2 3 2 2
ans = 28

5 2 10
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
0 1 0 1 0
0 0 0 0 0
5 3
3 2 1 1
4 1 1 1
'''