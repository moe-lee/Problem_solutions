codes = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())
for test_case in range(1,T+1) :
    n, m = map(int, input().split())
    line = ''
    code = []
    nums = [0] * 8
    for i in range(n) :
        line = input()
        if line.find('1') != -1 and not code:
            left, right = line.find('1'), line.rfind('1')
            code.append('0' * (56 - (right - left) - 1) + line[left:right+1])
            code.append(line[left:right+1] + '0' * (56 - (right-left) - 1))
        line = ''
    print('#'+str(test_case)+' ',end='')
    if code[0][:7] in codes :
        even, odd, tot = 0, 0, 0
        for i in range(8) :
            num = codes[code[0][i*7:i*7+7]]
            if (i+1) % 2 == 0 : even += num
            else : odd += num
            tot += num
        if (odd * 3 + even) % 10 == 0 :
            print(tot)
            continue
    if code[1][:7] in codes :
        even, odd, tot = 0, 0, 0
        for i in range(8) :
            num = codes[code[1][i*7:i*7+7]]
            if (i+1) % 2 == 0 : even += num
            else : odd += num
            tot += num
        if (odd * 3 + even) % 10 == 0 :
            print(tot)
            continue
    print(0)