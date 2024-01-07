def getDifference(weights) :
    left_arm, right_arm = 0, 0
    for i in range(len(weights)):
        if left_arm > right_arm :
            right_arm += weights[i]
        else :
            left_arm += weights[i]
    return abs(left_arm -right_arm)

def main() :
    weights = [1, 2, 5, 10, 20, 50, 100]
    wei_cnt = 0
    n = int(input())
    weights_input = list(map(lambda x: int(x), input().split()))
    diff = getDifference(weights_input)
    
    #print(diff, wei_cnt)
    # 가까운 값 찾기
    while diff > 0 :
        i = 0
        while i < len(weights) and weights[i] <= diff : i+=1
        i -= 1
        tmp = diff // weights[i]
        diff -= tmp * weights[i]
        wei_cnt += tmp
    print(wei_cnt)
    
main()


'''
7
3 1 4 1 5 9 2
2

4
2 4 6 4
0

5
2 5 3 1 2
1
'''