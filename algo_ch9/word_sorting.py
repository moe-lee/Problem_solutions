import sys
n = int(sys.stdin.readline())
words = []
word_map = dict()
for i in range(n) :
    s = input()
    if not word_map.get(s, False) :
        word_map[s] = True
        words.append(s)
        
words = sorted(words)
words = sorted(words, key=lambda x: len(x))

for s in words : print(s)