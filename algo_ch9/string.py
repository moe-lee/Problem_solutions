for _ in range(10) :
    t_num = input()
    target = input()
    origin = input()
    token_nums = 0
    while(origin.find(target) >= 0) :
        token_nums += 1
        origin = origin[origin.find(target) + len(target):]
    print(token_nums)
