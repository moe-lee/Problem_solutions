a, b = 1, 1
n = int(input())
while n > 1 :
    b, a, n = a, (a+b) % 10007, n - 1
print(a)