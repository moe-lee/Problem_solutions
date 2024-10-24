for test_case in range(1, 11) :
    N = int(input())
    heights = list(map(int, input().split()))
    tot_view = 0
    for i in range(2, N-2) :
        tot_view += max(0, heights[i] - max(heights[i-1], heights[i-2], heights[i+1], heights[i+2]))
    print('#'+str(test_case), tot_view)