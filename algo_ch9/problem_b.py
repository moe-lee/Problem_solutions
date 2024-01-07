def main() :
    n, b, a = tuple(map(lambda x : int(x), input().split()))
    prices = list(map(lambda x : int(x), input().split()))
    sum_bottom_up = [0 for i in prices]
    prices.sort()
    for i in range(n) :
        if i != 0: sum_bottom_up[i] = sum_bottom_up[i-1] + prices[i]
        else : sum_bottom_up[i] = prices[i]

    i = 0
    ## 할인이 없는 경우. 하나씩 더하기.
    if a == 0:
        while i < n and sum_bottom_up[i] <= b : i += 1
        print(i)
        return;
    
    if sum_bottom_up[a-1] / 2 == b : 
        print(a)
        return
    
    if sum_bottom_up[a-1] / 2 > b or n == a:
        i = 0
        while i < n and sum_bottom_up[i]/2 <= b : i+=1
        print(i)
        return
    
    i = 1
    while i+a <= len(prices):
        print(i, i+a)
        if (sum_bottom_up[a-1 + i] + sum_bottom_up[i-1]) / 2 > b :
            break
        i+=1
    print(a + i - 1)
main()