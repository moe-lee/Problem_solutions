def dailyTemperatures(temperatures) :
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_tem in enumerate(temperatures) :
        while stack and stack[-1][1] < cur_tem :
            prev_day, _ = stack.pop() # 튜플
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_tem))
    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))