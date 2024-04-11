import sys
def solution() :
    N = int(input())
    coords = []
    for _ in range(N) :
        coords.append(list(map(int, sys.stdin.readline().split())))
    coords.sort(key=lambda x : x[0])
    
    building_count = 0
    stack = []
    b = 0
    while b < N :
        if not stack or stack[-1] < coords[b][1] :
            if(coords[b][1] != 0) :
                stack.append(coords[b][1])
            b += 1
        elif stack and stack[-1] > coords[b][1] :
            stack.pop()
            building_count += 1
        else :
            b += 1
    
    building_count += len(stack)
    print(building_count)
    return

if __name__ == '__main__' :
    solution()