import sys

def solve() :
    N, S = map(int, sys.stdin.readline().split())
    positions = list(map(int, sys.stdin.readline().split()))
    fuels = list(map(int, sys.stdin.readline().split()))
    connectable_cars = set()
    left_car_movable, right_car_movable = True, True
    left_car, right_car = {'pos' : S-1, 'fuel' : fuels[S-1]}, {'pos' : S-1, 'fuel' : fuels[S-1]}
    connectable_cars.add(S-1)
    # 무한루프 -> left, right 모두 끝까지 갈 것이 보장되지 않는다.
    # 종료 조건이 필요하다.
    while left_car['pos'] >= 0 and right_car['pos'] < N and (left_car_movable or right_car_movable):
        if left_car['pos'] > 0 :
            dist = positions[left_car['pos']] - positions[left_car['pos'] - 1]
            if dist <= left_car['fuel'] :
                left_car['pos'] = left_car['pos']-1
                left_car['fuel'] -= dist
                connectable_cars.add(left_car['pos'])
                left_car_movable = True
            else :
                left_car_movable = False
        else :
            left_car_movable = False
        
        if right_car['pos'] < N-1 :
            dist = positions[right_car['pos'] + 1] - positions[right_car['pos']]
            if dist <= right_car['fuel'] :
                right_car['pos'] = right_car['pos'] + 1
                right_car['fuel'] -= dist
                connectable_cars.add(right_car['pos'])
                right_car_movable = True
            else :
                right_car_movable = False
        else :
            right_car_movable = False
        right_car['fuel'] = max((right_car['fuel'], fuels[right_car['pos']], (fuels[left_car['pos']]) - (positions[right_car['pos']] - positions[left_car['pos']])))
        left_car['fuel'] = max((left_car['fuel'], fuels[left_car['pos']], (fuels[right_car['pos']]) - (positions[right_car['pos']] - positions[left_car['pos']])))
    
    res = list(sorted(connectable_cars))
    for c in res :
        print(c+1, end=' ')
    return

solve()
