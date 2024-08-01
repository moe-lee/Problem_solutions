def dailyTemperatures(temperatures) :
    answer = [0 for _ in range(len(temperatures))]
    stack = []
    for cur_day, cur_temp in enumerate(temperatures) :
        while stack and stack[-1][1] < cur_temp :
            past_day, _ = stack.pop()
            answer[past_day] = cur_day - past_day
        stack.append((cur_day, cur_temp))
    return answer

print(dailyTemperatures(temperatures=[73,71,69,67,72,76]))