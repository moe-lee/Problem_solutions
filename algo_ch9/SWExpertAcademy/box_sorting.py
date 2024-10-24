T = int(input())
for testcase in range(1, T+1) :
    N = int(input())
    boxes = dict()
    container = [0] + list(map(int, input().split()))
    for i, box in enumerate(container) :
        boxes[box] = i # 어떤 박스가 있는 위치
    visited = [False] * (N+1)
    empty_count = 0
    stack = []
    for i in range(1, N+1) :
        if i != container[i] and not visited[i]: # 옮긴다.
            cur_pos = i
            next_pos = boxes[i]
            empty_count += 1
            while not visited[cur_pos] :
                visited[cur_pos] = True
                stack.append(cur_pos)
                cur_pos = next_pos
                next_pos = boxes[cur_pos]
                empty_count += 1
            stack.append(N+1)
        visited[i] = True
    print(empty_count)
    print(*stack)

'''
2
3
1 2 3
4
2 3 4 1

1
5
5 4 1 2 3
'''