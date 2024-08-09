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

result = []
s = "abcd"
def iterSubset() :
    stack = [(0, "")]
    while stack :
        cur_level, letter = stack.pop()
        if cur_level == len(s) :
            result.append(letter)
            continue
        stack.append((cur_level + 1, letter[:] + s[cur_level]))
        stack.append((cur_level + 1, letter[:]))

ip = list("abcd")
def permutation(index, letters) :
    if index == len(ip) :
        result.append(letters[:])
        return
    for i in range(0, len(ip)) :
        if ip[i] not in letters:
            permutation(index+1, letters+ip[i])

def permutation2(index, letters) :
    if index == len(ip) :
        result.append("".join(letters))
        return
    for i in range(index , len(ip)) :
        letters[i], letters[index] = letters[index], letters[i]
        permutation2(index + 1, letters[:])
iterSubset()
result.sort()
print(result)
print(len(result))