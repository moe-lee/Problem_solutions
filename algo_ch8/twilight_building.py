from collections import deque as stack
# east to west
def twilight_building(buildings) :
    possibles = stack()
    for i, n in enumerate(buildings) :
        while possibles and buildings[possibles[len(possibles)-1]] > n :
            possibles.pop()
        possibles.append(i)
    return list(possibles)


# west to east
def twilight_building2(buildings) :
    building_list = [buildings[0]]
    for i in range(1, len(buildings)) :
        if building_list[len(building_list) - 1] < buildings[i] :
            building_list.append(buildings[i])
    return building_list

if __name__ == "__main__" :
    buildings = [1,3,5,7,7,10]
    res = twilight_building2(buildings)
    print(res)