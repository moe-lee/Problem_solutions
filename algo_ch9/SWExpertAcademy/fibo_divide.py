fibo_divisions = [None, None, 'BA', "BBA", None]
for i in range(5, 101) :
    if fibo_divisions[i-3] : fibo_divisions.append(fibo_divisions[i-3] + 'BBA')
    else : fibo_divisions.append(None)
test_case = int(input())
for _ in range(1, test_case + 1) :
    N = int(input())
    if fibo_divisions[N] : print(fibo_divisions[N])
    else : print('impossible')