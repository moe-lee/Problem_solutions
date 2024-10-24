memo = {}
def exp(x, y) :
    if y == 1 : return x
    if (x,y) not in memo :
        memo[(x, y)] = exp(x, y//2) ** 2 * (1 if y % 2 == 0 else x)
    return memo[(x, y)]
for test_case in range(1, 11) :
    t_num = input()
    x, y = map(int, input().split())
    print('#'+t_num, exp(x, y))