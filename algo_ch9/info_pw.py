n, k = 10, 24
acc = 0
i = 1
while acc + i <= k :
    acc += i
    i += 1
print(n- (k - acc - 1))