T = int(input())
for _ in range(T) :
    t_num = input()
    scores = [0] * (101)
    for num in list(map(int, input().split())) :
        scores[num] += 1
    max_idx = 0
    for i in range(1, 101) :
        if scores[max_idx] <= scores[i] :
            max_idx = i
    print('#'+t_num, max_idx)