import sys

n = int(sys.stdin.readline())
a = 17
if(n == 1) : print(9)
elif(n == 2) : print(a)
else :
    for i in range(3, n + 1) :
        a = (a * 2 - 2) % 1000000000
    print(a)
