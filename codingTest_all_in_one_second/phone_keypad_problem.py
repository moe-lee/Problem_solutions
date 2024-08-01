numbers = input()
array = []
hash_map = {
    '2' : ['a','b','c'],
    '3' : ['d','e','f'],
    '4' : ['g','h','i'],
    '5' : ['j','k','l'],
    '6' : ['m','n','o'],
    '7' : ['p','q','r','s'],
    '8' : ['t','u','v'],
    '9' : ['w','x','y', 'z'],
    '1' : []
}

def backTracking(index, letter) :
    if index >= len(numbers) :
        array.append(letter)
        return
    chars = hash_map[numbers[index]]
    for c in chars :
        backTracking(index=index + 1, letter=letter+c)
    return
backTracking(0, '')
print(array)