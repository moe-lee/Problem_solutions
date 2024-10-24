for test_case in range(1, 11) :
    N = int(input())
    origin = input().split()
    M = int(input())
    inst = input().split()
    idx = 0
    while idx < len(inst) :
        if inst[idx] == 'I' :
            x, y = int(inst[idx+1]), int(inst[idx+2])
            for i in range(y) : origin.insert(x+i, inst[idx+3+i])
            idx += 3 + y
        elif inst[idx] == 'D' :
            x, y = int(inst[idx+1]), int(inst[idx+2])
            temp = origin[:x] + origin[x+y:]
            origin = temp
            idx += 3
        elif inst[idx] == 'A' :
            y = int(inst[idx+1])
            origin.extend(inst[idx + 2: idx+2+y])
            idx += 2 + y
    print('#'+str(test_case), *origin[:10])

'''
5
1 2 3 4 5
1
D 3 1
'''