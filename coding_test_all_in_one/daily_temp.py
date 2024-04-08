def dailyTemperature(temperatures) :
    answer = [0] * len(temperatures)
    stack = []
    for cur_pos, cur_tem in enumerate(temperatures) :
        while stack and stack[-1][1] < cur_tem :
            pre_pos, _ = stack.pop()
            answer[pre_pos] = cur_pos - pre_pos
        stack.append((cur_pos, cur_tem))
    return answer

if __name__ == '__main__' :
    print(dailyTemperature(temperatures=[30, 40, 50, 60]))
    