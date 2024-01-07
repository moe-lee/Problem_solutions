from collections import deque as stack

def sun_set_buildings(buildings) :
    possible_buldings = stack()
    for i,h in enumerate(buildings) :
        while possible_buldings and buildings[possible_buldings[-1]] <= h : possible_buldings.pop()
        possible_buldings.append(i)
    return list(possible_buldings)

def sun_set_buildings_w_to_e(buildings) :
    max_h = buildings[0]
    possibles = [0]
    for i in range(1, len(buildings)) :
        if buildings[i] > max_h : possibles.append(i)
        max_h = max(buildings[i], max_h)
    return possibles

if __name__ == "__main__" :
    res = sun_set_buildings_w_to_e([3,3,6,7,5,4,3])
    print(res)