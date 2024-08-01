numbers = [1,2,3,4]
result = []

k = 0
def backTracking(index, cur_set):
    if index == k :
        result.append(cur_set[:])
        return
    
    for ni in range(index, len(numbers)) :
        cur_set.append(numbers[ni])
        backTracking(ni+1, cur_set)
        cur_set.pop()
    return

s = 'abcd'
def backTracking2(index, letter) :
    if index >= len(s) :
        result.append(''.join(letter))
        return
    letter.append(s[index])
    backTracking2(index=index+1, letter=letter)
    letter.pop()
    backTracking2(index=index+1, letter=letter)

# iterative model, ^ is DFS
def backtracking3() :
    stack = [(0, "")]
    while stack :
        level, letter = stack.pop()
        if level == len(s) :
            result.append(letter)
            continue
        stack.append((level + 1, letter))
        stack.append((level + 1, letter + s[level]))

def permutation(index, letter) :
    if index == len(s) :
        result.append(''.join(letter))
        return
    for c in s :
        if c not in letter:
            letter.append(c)
            permutation(index+1, letter)
            letter.pop()

def permutation_swap(index, letter) :
    if index == len(s) - 1:
        result.append(''.join(letter))
        return
    for i in range(index, len(s)) :
        letter[index], letter[i] = letter[i], letter[index]
        permutation_swap(index + 1, letter)
permutation_swap(0,list(s))
print(result)